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

        self.steps_label.config(text=f"
