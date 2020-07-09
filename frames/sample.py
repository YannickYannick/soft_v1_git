#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 18:39:25 2020

@author: melinapannier
"""

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class SampleParametres(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(**kwargs)
        
        container = ttk.Frame(self, padding=10, height=400, width=800,
                              style="Frame.TFrame")
        container.grid(row=0, column=0, sticky="NESW")
        container.grid_propagate(0)
        
        title_frame = ttk.Label(container, text="SAMPLE PARAMETRES",
                                style="Title.TLabel")
        title_frame.grid(column=0, row=0, sticky ="NESW")
        
        
        
        left_container= ttk.Frame(container, padding=10, style="Frame.TFrame")
        left_container.grid(row=1, column=0, columnspan=1, sticky="NESW")
        left_container.rowconfigure((0, 1, 2, 3, 4), weight=1)
        
        material_label = ttk.Label(left_container, text="Material",
                                   style="Label.TLabel")
        material_label.grid(column=0, row=0, sticky="NSEW")
        selected_material = tk.StringVar()
        material = ttk.Combobox(left_container, 
                                textvariable=selected_material)
        material["values"] = ("Burst", "Continued")
        material.grid(column=1, row=0, pady=5, sticky="NESW")
        
        sample_name_label = ttk.Label(left_container, text="Sample Name", 
                                      style="Label.TLabel")
        sample_name_label.grid(column=0, row=1, sticky="NSEW")
        selected_sample_name = tk.StringVar()
        sample_name = ttk.Combobox(left_container, 
                                   textvariable=selected_sample_name)
        sample_name["values"] = ("Burst", "Continued")
        sample_name.grid(column=1, row=1, pady=5, sticky="NESW")
        
        width_label = ttk.Label(left_container, text="Sample Width", 
                                style="Label.TLabel")
        width_label.grid(column=0, row=2, sticky="NSEW")
        selected_sample_width = tk.StringVar()
        sample_width = ttk.Combobox(left_container, 
                                    textvariable=selected_sample_width)
        sample_width["values"] = ("Burst", "Continued")
        sample_width.grid(column=1, row=2, pady=5, sticky="NESW")
        
        text_box_value = tk.StringVar()
        text_box= ttk.Entry(left_container, width=10, 
                            textvariable=text_box_value)
        text_box.grid(column=0, row=3, columnspan=2, sticky="NESW")
        
        
        
        right_container= ttk.Frame(container, padding=10, 
                                   style="Frame.TFrame")
        right_container.grid(row=1, column=1, columnspan=1, sticky="NESW")
        right_container.rowconfigure((0, 1), weight=1)
        
        dialogue_value = tk.StringVar(value="dialogue window")
        dialogue_window = ttk.Entry(right_container, 
                                    textvariable=dialogue_value)
        dialogue_window.grid(column=0, row=0, sticky="NESW")
        
        
        logo_image = Image.open("./logo.png").resize((130, 80))
        logo_photo = ImageTk.PhotoImage(logo_image)
        logo_label = ttk.Label(right_container, image=logo_photo, padding=20,
                               style="Label.TLabel")
        logo_label.grid(column=0, row=1, sticky="NESW")

        logo_label.image = logo_photo