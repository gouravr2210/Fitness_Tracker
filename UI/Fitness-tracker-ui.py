import tkinter as tk
from tkinter import messagebox
import json
import threading
import time

class FitnessTrackerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fitness Tracker")
        self.geometry("400x300")

        self.steps_label = tk.Label(self, text="Steps: 0")
        self.steps_label.pack(pady=10)

        self.distance_label = tk.Label(self, text="Distance: 0.0")
        self.distance_label.pack(pady=10)

        self.location_label = tk.Label(self, text="Location: (0, 0)")
        self.location_label.pack(pady=10)

        self.heart_rate_label = tk.Label(self, text="Heart Rate: 0")
        self.heart_rate_label.pack(pady=10)

        self.wifi_status_label = tk.Label(self, text="Wi-Fi: Disconnected")
        self.wifi_status_label.pack(pady=10)

        self.start_button = tk.Button(self, text="Start Tracking", command=self.start_tracking)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self, text="Stop Tracking", command=self.stop_tracking)
        self.stop_button.pack(pady=10)

        self.running = False

    def start_tracking(self):
        self.running = True
        self.update_ui()
        self.start_services()

    def stop_tracking(self):
        self.running = False
        self.stop_services()

    def update_ui(self):
        if not self.running:
            return

        steps = self.read_step_count()
        distance, location = self.read_location_data()
        heart_rate = self.read_heart_rate()
        wifi_connected = self.read_wifi_status()

        self.steps_label.config(text=f"Steps: {steps}")
        self.distance_label.config(text=f"Distance: {distance:.2f} km")
        self.location_label.config(text=f"Location: {location}")
        self.heart_rate_label.config(text=f"Heart Rate: {heart_rate} bpm")
        self.wifi_status_label.config(text=f"Wi-Fi: {'Connected' if wifi_connected else 'Disconnected'}")

        self.after(1000, self.update_ui) 

    def read_step_count(self):
        try:
            with open('/tmp/step_count.json', 'r') as f:
                return json.load(f).get('steps', 0)
        except FileNotFoundError:
            return 0

    def read_location_data(self):
        try:
            with open('/tmp/location_data.json', 'r') as f:
                data = json.load(f)
                return data.get('distance', 0), tuple(data.get('location', (0, 0)))
        except FileNotFoundError:
            return 0, (0, 0)

    def read_heart_rate(self):
        try:
            with open('/tmp/heart_rate.json', 'r') as f:
                return json.load(f).get('heart_rate', 0)
        except FileNotFoundError:
            return 0

    def read_wifi_status(self):
        try:
            with open('/tmp/wifi_status.json', 'r') as f:
                return json.load(f).get('wifi_connected', False)
        except FileNotFoundError:
            return False

    def start_services(self):
        commands = [
            "sudo systemctl start step_counter.service",
            "sudo systemctl start location_tracker.service",
            "sudo systemctl start ble_heart_rate.service",
            "sudo systemctl start wifi_status.service"
        ]
        for cmd in commands:
            threading.Thread(target=self.run_command, args=(cmd,)).start()

    def stop_services(self):
        commands = [
            "sudo systemctl stop step_counter.service",
            "sudo systemctl stop location_tracker.service",
            "sudo systemctl stop ble_heart_rate.service",
            "sudo systemctl stop wifi_status.service"
        ]
        for cmd in commands:
            threading.Thread(target=self.run_command, args=(cmd,)).start()

    def run_command(self, command):
        subprocess.run(command, shell=True)

if __name__ == "__main__":
    app = FitnessTrackerApp()
    app.mainloop()

        
