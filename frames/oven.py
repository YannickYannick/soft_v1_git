#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 18:38:24 2020

@author: melinapannier
"""
 
import tkinter as tk
from tkinter import ttk
from tools import Gauge
#from tools import NumEntry


class Oven(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(**kwargs)
        
        
        container = ttk.Frame(self, padding=10, height=470, width=800,
                              style="Frame.TFrame")
        container.grid(row=0, column=0, sticky="NESW")
        container.grid_propagate(0)
    
        title_frame = ttk.Label(container, text="OVEN CONTROL", 
                                style="Title.TLabel")
        title_frame.grid(column=0, row=0, sticky ="NESW")
        
        
        
        left_container= ttk.Frame(container, style="Frame.TFrame")
        left_container.grid(row=1, column=0, columnspan=1, sticky="NESW")
        

        gauge = Gauge(
            left_container,
            #text="Temperature (°C)",
            width=300, 
            height=150,
            min_value=0,
            max_value=1200,
            divisions=5,
            label='Current Temperature',
            units='°C',
            bg="#D3E2F1"
        )
        gauge.grid(column=0, row=0, sticky ="NESW") 
        gauge.set_value(800)
        
                
        selection_temp_container= ttk.LabelFrame(left_container, padding=0, 
                                         text="Temperature Entry Mode",
                                         height = 30, width = 250,
                                         style="Label.TLabelframe")
        selection_temp_container.grid(row=1, column=0)
        
        selection_temperature_container= ttk.Frame(selection_temp_container, 
                                         style="Frame.TFrame")
        selection_temperature_container.grid(row=0, column=0, sticky="NESW")
        
        temperature_selection = tk.StringVar()
        linear_temperature = ttk.Radiobutton(
            selection_temperature_container, 
            text="Linear", 
            variable=temperature_selection, 
            value="linear",
            style="Radiobutton.TRadiobutton",
            command =  lambda : self.show_auto(auto_frame),
            takefocus=False
        )
        linear_temperature.grid(column=0, row=0, padx=5, sticky="NESW")
        
        log_temperature = ttk.Radiobutton(
            selection_temperature_container, 
            text="Logarithmic", 
            variable=temperature_selection, 
            value="log",
            style="Radiobutton.TRadiobutton",
            command =  lambda : self.show_auto(auto_frame),
            takefocus=False
        )
        log_temperature.grid(column=1, row=0, padx=5, sticky="NESW")
        
        manual_temperature = ttk.Radiobutton(
            selection_temperature_container, 
            text="Manual", 
            variable=temperature_selection, 
            value="manual",
            style="Radiobutton.TRadiobutton",
            command =  lambda : self.show_manual(manual_frame),
            takefocus=False
        )
        manual_temperature.grid(column=2, row=0, padx=5, sticky="NESW")
                
                    
        temperature_container= ttk.Frame(selection_temp_container, 
                                         style="Frame.TFrame")
        temperature_container.grid(row=1, column=0, sticky="NESW")

        
        number_point_label= ttk.Label(temperature_container, 
                                  text="Number of points", 
                                  style="Label.TLabel")
        number_point_label.grid(row=2, column=0, pady=5, sticky ="NESW")  
        vcmd = (self.register(self.onValidate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.number_point_value = tk.StringVar(value=12)
        self.number_point = ttk.Spinbox(
            temperature_container,
            from_=2,
            to=120,
            increment=1,
            justify="center",
            textvariable=self.number_point_value,
            width=5,
            style="Spinbox.TSpinbox",
            validate="key",
            validatecommand=vcmd
        )
        self.number_point.grid(column=1, row=2, pady=5, sticky ="NESW") 
        
        
        
        temperature_min_label= ttk.Label(temperature_container, 
                                  text="Min. Temperature (°C)", 
                                  style="Label.TLabel")
        temperature_min_label.grid(row=0, column=0, pady=5, sticky ="NESW")        
        self.temperature_min_value = tk.StringVar(value=0)
        self.temperature_min = ttk.Spinbox(
            temperature_container,
            from_=0,
            to=120,
            increment=1,
            justify="center",
            textvariable=self.temperature_min_value,
            width=8,
            style="Spinbox.TSpinbox",
            validate="key",
            validatecommand=vcmd
        )
        self.temperature_min.grid(column=1, row=0, pady=5, sticky ="NESW")
        
        temperature_max_label= ttk.Label(temperature_container, 
                                  text="Max.Temperature (°C)", 
                                  style="Label.TLabel")
        temperature_max_label.grid(row=1, column=0, pady=5, sticky ="NESW")        
        self.temperature_max_value = tk.StringVar(value=200)
        self.temperature_max = ttk.Spinbox(
            temperature_container,
            from_=0,
            to=120,
            increment=1,
            justify="center",
            textvariable=self.temperature_max_value,
            width=8,
            style="Spinbox.TSpinbox",
            validate="key",
            validatecommand=vcmd
        )
        self.temperature_max.grid(column=1, row=1, pady=5, sticky ="NESW")
        
        
        # manual_temp_container= ttk.Frame(container, padding=10, 
        #                                   style="Frame.TFrame")
        # manual_temp_container.grid(row=2, column=0,columnspan=2, sticky="NESW")
        
        manual_frame = ManualTemperature(container, padding=10)
        manual_frame.grid(row=2, column=0, columnspan=2, pady=5, sticky="NESW")
        
        auto_frame = AutoTemperature(container, self)
        auto_frame.grid(row=2, column=0, columnspan=2, pady=5, sticky="NESW")
        
        select_advice = SelectAdvice(container, padding=10)
        select_advice.grid(row=2, column=0, columnspan=2, sticky="NESW")
    
        
        


        
        
        
        right_container= ttk.Frame(container, 
                                   style="Frame.TFrame", 
                                   height=350)
        right_container.grid(row=1, column=1, sticky="NESW")
        
        spinbox_container= ttk.Frame(right_container, padding=10, 
                                     style="Frame.TFrame")
        spinbox_container.grid(row=0, column=0, columnspan=1,rowspan=4, 
                               sticky="NESW")
        spinbox_container.rowconfigure((0, 1, 2, 3), weight=1)
        spinbox_container.columnconfigure((0, 1), weight=1)
        
        
        
        temperature_rise_rate_label= ttk.Label(spinbox_container, 
                                               text="Rise Rate (°C/min)", 
                                               style="Label.TLabel")
        temperature_rise_rate_label.grid(row=0, column=0, pady=5, 
                                         sticky ="NESW")       
        rise_rate_value = tk.StringVar()
        temperature_rise_rate = ttk.Spinbox(
            spinbox_container,
            from_=0,
            to=120,
            increment=1,
            justify="center",
            textvariable=rise_rate_value,
            width=10,
            validate="key",
            validatecommand=vcmd
        )            
        temperature_rise_rate.grid(column=1, row=0, pady=5, sticky ="NESW")
        
        
        accuracy_label= ttk.Label(spinbox_container, 
                                  text="Accuracy (°C)", 
                                  style="Label.TLabel")
        accuracy_label.grid(row=1, column=0, pady=5, sticky ="NESW")        
        accuracy_value = tk.StringVar()
        accuracy = ttk.Spinbox(
            spinbox_container,
            from_=0,
            to=120,
            increment=1,
            justify="center",
            textvariable=accuracy_value,
            width=10,
            validate="key",
            validatecommand=vcmd
        )
        accuracy.grid(column=1, row=1, pady=5, sticky ="NESW")
        
        annealing_label= ttk.Label(spinbox_container, 
                                   text="Annealing time (s)", 
                                   style="Label.TLabel")
        annealing_label.grid(row=2, column=0, pady=5, sticky ="NESW")        
        self.annealing_value = tk.StringVar()
        annealing = ttk.Spinbox(
            spinbox_container,
            from_=0,
            to=120,
            increment=1,
            justify="center",
            textvariable=self.annealing_value,
            width=10,
            validate="key",
            validatecommand=vcmd
        )
        annealing.grid(column=1, row=2, pady=5, sticky ="NESW")
        
        
        annealing_remain_label= ttk.Label(spinbox_container, 
                                          text="Remaining (s)", 
                                          style="Label.TLabel")
        annealing_remain_label.grid(row=3, column=0, pady=5, sticky ="NESW")        
        self.remain_time = tk.StringVar()
        self._timer_decrement_job = None
        annealing_remain = ttk.Label(
            spinbox_container,
            textvariable=self.remain_time,
            width=10,
        )
        annealing_remain.grid(column=1, row=3, pady=5, sticky ="NES")
        
        
        
        button_container = ttk.Frame(right_container, padding=5, 
                                     style="Frame.TFrame")
        button_container.grid(pady=0)
        
        
        play_button = ttk.Button(button_container, text="Play", width=6, 
                                 style="Button.TButton", command=self.play)
        play_button.grid(row=0, column=0, padx=3)
        
        stop_button = ttk.Button(button_container, text="Stop", width=6, 
                                 style="Button.TButton")
        stop_button.grid(row=0, column=2, padx=3)
        
        next_button = ttk.Button(button_container, text="Next", width=6, 
                                 style="Button.TButton")
        next_button.grid(row=0, column=1, padx=3)
        
        
        
        dialogue_box_container= ttk.LabelFrame(right_container, padding=0, 
                                         text="Dialogue Box",
                                         #height = 30, width = 250,
                                         style="Label.TLabelframe")
        dialogue_box_container.grid(ipady=30, sticky="NESW")
        
        dialogue_value = tk.StringVar()
        dialogue_window = ttk.Label(dialogue_box_container, 
                                    textvariable=dialogue_value )
        dialogue_window.grid(sticky ="NESW")
        
    def onValidate(self, d, i, P, s, S, v,V, W):        
        # Disallow anything but numbers 
        if S.isdigit():
            return True
        elif S==".":
            return True
        else:
            self.bell()
            return False

     
    def play (self):
        self.play_pressed = True
        value = self.annealing_value.get()
        self.remain_time.set(f"{value}") 
        self.remaining_time()
        
    def remaining_time(self):
        current_temperature = 60
        final_temperature = 60
        remain=self.remain_time.get()
        #print(self.remain_time.get())
        if current_temperature == final_temperature :
            seconds = int(remain)
            if seconds > 0 :
                remain = seconds - 1
            
            self.remain_time.set(f"{remain}")    
            self._timer_decrement_job = self.after(1000, self.remaining_time)
            
    def show_manual(self,frame):
        frame.tkraise()
        self.number_point['state']='disabled'
        self.temperature_max['state']='disabled'
        self.temperature_min['state']='disabled'
        
    def show_auto(self,frame):
        frame.tkraise()
        self.number_point['state']='normal'
        self.temperature_max['state']='normal'
        self.temperature_min['state']='normal'
 
            
 
class ManualTemperature(ttk.LabelFrame):
    
    def __init__(self, parent, **kwargs):        
        super().__init__(parent)
        
        self["style"] = "Label.TLabelframe"
        self["text"] = "Target Temperatures"
        #self["padding"] = 10
        
        self.width=4  
        
        self.temperature = []
        self.temperature_value = []

        vcmd = (self.register(self.onValidate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        
        for i in range(0,12):
            self.temperature_value.append(0)
            self.temperature.append(0)
            self.temperature_value[i] = tk.StringVar()
            self.temperature[i] = ttk.Entry(self, width=self.width, 
                            textvariable=self.temperature_value[i],
                            validate="key", validatecommand=vcmd)
            self.temperature[i].grid(column=i, row=0, sticky="NESW")
            
        for i in range(12,24):
            self.temperature_value.append(0)
            self.temperature.append(0)
            self.temperature_value[i] = tk.StringVar()
            self.temperature[i] = ttk.Entry(self, width=self.width, 
                            textvariable=self.temperature_value[i],
                            validate="key", validatecommand=vcmd)
            self.temperature[i].grid(column=i-12, row=1, sticky="NESW")
            
        clear_button = ttk.Button(self, text="Clear", width=8, padding=0,
                                  style="Button.TButton", command=self.clear)
        clear_button.grid(row=0, column=13, rowspan=2, padx=5)
            
    def onValidate(self, d, i, P, s, S, v,V, W):        
        # Disallow anything but numbers 
        if S.isdigit():
            return True
        elif S==".":
            return True
        else:
            self.bell()
            return False
            
        
    def clear(self):
        for i in range(0,24):
            self.temperature_value[i].set(" ")

        
class AutoTemperature(ttk.LabelFrame):
    
    def __init__(self, parent, controller, **kwargs):       
        super().__init__(parent,**kwargs)
        
        self["style"] = "Label.TLabelframe"
        self["text"] = "Target Temperatures"
        
        self.width=4
        self.controller = controller
        self.temperature = []
        self.temperature_value = []

        for i in range(0,12):
            self.temperature_value.append(0)
            self.temperature.append(0)
            self.temperature_value[i] = tk.StringVar()
            self.temperature[i] = ttk.Label(self, width=self.width, 
                            textvariable=self.temperature_value[i],
                            borderwidth=2, relief="ridge", padding=0)
            self.temperature[i].grid(column=i, row=0, sticky="NESW")
            
        for i in range(12,24):
            self.temperature_value.append(0)
            self.temperature.append(0)
            self.temperature_value[i] = tk.StringVar()
            self.temperature[i] = ttk.Label(self, width=self.width, 
                            textvariable=self.temperature_value[i],
                            borderwidth=2, relief="ridge", padding=0)
            self.temperature[i].grid(column=i-12, row=1, sticky="NESW")
               
        validation_button = ttk.Button(self, text="Enter", width=8,  padding=0,
                                 style="Button.TButton", command=self.validate)
        validation_button.grid(row=0, column=13, padx=5)
        
        clear_button = ttk.Button(self, text="Clear", width=8, padding=0,
                                 style="Button.TButton", command=self.clear)
        clear_button.grid(row=1, column=13, padx=5)
        
        
    def validate(self):
        number_point = self.controller.number_point_value.get()
        temperature_min = self.controller.temperature_min.get()
        temperature_max = self.controller.temperature_max.get()
        temperature=[]
        
        for i in range(0,int(number_point)):
            temperature.append(0)
            temperature[i] = round(int(temperature_min)+
                (((int(temperature_max)-int(temperature_min))/(int(number_point)-1))*i))
            self.temperature_value[i].set(f"{temperature[i]}")
            
    def clear(self):
        for i in range(0,24):
            self.temperature_value[i].set(" ")

        
        
class SelectAdvice(ttk.Frame):    
    def __init__(self, parent, **kwargs):
        super().__init__(parent,**kwargs)
        
        self["style"] = "Frame.TFrame"
        
        advice = ttk.Label(self, text="Please select a temperature entry mode",
                         borderwidth=2, relief="ridge")
        
        advice.place(anchor='center',relx=0.5, rely=0.7)
        
        #advice.grid(row=0, column=0, sticky="NEWS")
        

        

        
        
    





        