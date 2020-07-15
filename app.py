#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 08:32:01 2020

@author: melinapannier
"""
import tkinter as tk
from tkinter import ttk
from frames import Oven, Laser, Oscilloscope, SampleParametres
from applications.picoscope9000 import CommunicationPicoscope


def set_dpi_awareness(): # à tester
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass

set_dpi_awareness()



COLOR_TITLE = "#2e3f4f"
COLOR_LIGHT_BACKGROUND = "#D3E2F1"
COLOR_DARK_BACKGROUND = "#2e3f4f"
COLOR_ACTIVE_BACKGROUND = "#86C0F5"
COLOR_PRESSED_BACKGROUND = "#4390D5"


class RepeatedFlashExperiment(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.reglage_1 = "coou"
        
        self["background"] = COLOR_DARK_BACKGROUND
        
        
        self.title("Repeated Flash Experiment")
        
        
        container = ttk.Frame(self, padding=10 )
        container.grid()
        container.columnconfigure((0, 1), weight=1)
        container.rowconfigure((0, 1), weight=1)
        
        height_frames_1 = 470
        height_frames_2 = 350
        width_frames = 1200
        
        
        
        oven_frame = Oven(container, padding=10, height=height_frames_1, 
                          width=width_frames, style="Main.TFrame") 
        oven_frame.grid(row=0, column=0, sticky="NESW")
        oven_frame.grid_propagate(0)
        
        
        laser_frame = Laser(container, padding=10, height=height_frames_2,
                            width=width_frames, style="Main.TFrame")
        laser_frame.grid(row=1, column=0, sticky="NESW")
        laser_frame.grid_propagate(0)
        
        self.communication_picoscope = CommunicationPicoscope(self)
        oscillo_frame = Oscilloscope(container, self, padding=10, 
                                      height=height_frames_1, 
                                      width=width_frames,style="Main.TFrame")
        oscillo_frame.grid(row=0, column=1, sticky="NESW")
        oscillo_frame.grid_propagate(0)
        
        
        sample_frame = SampleParametres(container, padding=10, 
                                        height=height_frames_2, 
                                        width=width_frames, 
                                        style="Main.TFrame")
        sample_frame.grid(row=1, column=1, sticky="NESW")
        sample_frame.grid_propagate(0)
      


app = RepeatedFlashExperiment()

style = ttk.Style()
style.theme_use("clam")

style.configure("Title.TLabel", foreground=COLOR_TITLE, 
                background=COLOR_LIGHT_BACKGROUND, font="Helvetica 20 bold")
style.configure("Main.Tframe", background=COLOR_DARK_BACKGROUND)
style.configure("Frame.TFrame", background=COLOR_LIGHT_BACKGROUND)
style.configure("Label.TLabel", background=COLOR_LIGHT_BACKGROUND)
style.configure("Button.TButton", background=COLOR_LIGHT_BACKGROUND,
                foreground=COLOR_DARK_BACKGROUND,font="Helvetica 14 bold")
style.configure("Radiobutton.TRadiobutton", background=COLOR_LIGHT_BACKGROUND)
style.configure("Spinbox.TSpinbox")
 
style.map("Button.TButton",background=[('pressed', COLOR_PRESSED_BACKGROUND), 
                                  ('active', COLOR_ACTIVE_BACKGROUND)])
style.map("Spinbox.TSpinbox",background=[('disabled', COLOR_PRESSED_BACKGROUND)])
style.map("Radiobutton.TRadiobutton",background=[('active', COLOR_ACTIVE_BACKGROUND)])
# style.configure("Alert.TLabel", foreground=COLOR_TITLE, 
#                 background=COLOR_LIGHT_BACKGROUND, font="Helvetica bold")
style.configure("Label.TLabelframe.Label", background=COLOR_LIGHT_BACKGROUND,
                foreground=COLOR_DARK_BACKGROUND)
style.configure("Label.TLabelframe", background=COLOR_LIGHT_BACKGROUND,
                labeloutside=False,labelmargins=10)

app.mainloop()