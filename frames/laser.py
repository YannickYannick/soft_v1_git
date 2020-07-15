#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 18:38:44 2020

@author: melinapannier
"""

import tkinter as tk
from tkinter import ttk

class Laser(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(**kwargs)
        
        container = ttk.Frame(self, padding=10, height=400, width=1200,
                              style="Frame.TFrame")
        container.grid(row=0, column=0, sticky="NESW")
        container.grid_propagate(0)
        
        title_frame = ttk.Label(container, text="LASER CONTROL", style="Title.TLabel")
        title_frame.grid(column=0, row=0, sticky ="NESW")
        
        
        
        left_container= ttk.Frame(container, padding=10, style="Frame.TFrame")
        left_container.grid(row=1, column=0, columnspan=1, sticky="NESW")
        left_container.rowconfigure((0, 1, 2, 3, 4), weight=1)
        
        mode_label = ttk.Label(left_container, text="Mode", style="Label.TLabel")
        mode_label.grid(column=0, row=0, sticky="NSEW")
        selected_mode = tk.StringVar(value="Mode")
        mode = ttk.Combobox(left_container, textvariable=selected_mode)
        mode["values"] = ("Burst", "Continued")
        mode.grid(column=1, row=0, pady=5, sticky="NESW")
        
        rate_label = ttk.Label(left_container, text="Repetition rate", style="Label.TLabel")
        rate_label.grid(column=0, row=1, sticky="NSEW")
        selected_repetition_rate = tk.StringVar(value="Repetition Rate")
        repetition_rate = ttk.Combobox(left_container, textvariable=selected_repetition_rate)
        repetition_rate["values"] = ("Burst", "Continued")
        repetition_rate.grid(column=1, row=1, pady=5, sticky="NESW")
        
        pulse_label = ttk.Label(left_container, text="Pulse", style="Label.TLabel")
        pulse_label.grid(column=0, row=2, sticky="NSEW")
        selected_pulse_rate = tk.StringVar(value="Pulse Rate")
        pulse_rate = ttk.Combobox(left_container, textvariable=selected_pulse_rate)
        pulse_rate["values"] = ("Burst", "Continued")
        pulse_rate.grid(column=1, row=2, pady=5, sticky="NESW")
        
        frequency_label = ttk.Label(left_container, text="Frequency", style="Label.TLabel")
        frequency_label.grid(column=0, row=3, sticky="NSEW")
        selected_frequency = tk.StringVar(value="Frequency")
        frequency = ttk.Combobox(left_container, textvariable=selected_frequency)
        frequency["values"] = ("10000", "20000")
        frequency.grid(column=1, row=3, pady=5, sticky="NESW")
        
        power_label = ttk.Label(left_container, text="Power", style="Label.TLabel")
        power_label.grid(column=0, row=4, sticky="NSEW")
        selected_power = tk.StringVar(value="Power")
        power = ttk.Combobox(left_container, textvariable=selected_power, text="Power")
        power["values"] = ("Burst", "Continued")
        power.grid(column=1, row=4, pady=5, sticky="NESW")
        
        
        
        right_container= ttk.Frame(container, padding=10, style="Frame.TFrame")
        right_container.grid(row=1, column=1, columnspan=1, sticky="NESW")
        right_container.rowconfigure((0, 1), weight=1)
        
        dialogue_value = tk.StringVar(value="dialogue window")
        dialogue_window = ttk.Entry(right_container, textvariable=dialogue_value)
        dialogue_window.grid(column=0, row=0, sticky="NESW")
        
        play_button = ttk.Button(right_container, text="Play", padding=10, style="Button.TButton")
        play_button.grid(column=0, row=1)

