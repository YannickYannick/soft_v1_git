#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 15:33:46 2020

tk frames and tk subframes related to the oven for the repeated flash 
experiment GUI

@author: melinapannier
"""

import tkinter as tk
from tkinter import ttk
from tools import Gauge




class OvenSeparate(ttk.Frame):
    def __init__(self, container, main_app, **kwargs):
        super().__init__(container,**kwargs)
        
        self.main_app = main_app
        
        self.rowconfigure((1), weight=1)
        self.columnconfigure((0), weight=1)
        

        self.title_label = ttk.Label(self, 
                                     text="OVEN CONTROL",
                                     style="Title.TLabel"
                                     )
        self.title_label.grid(row=0, column=0, sticky="W")
        
        
        sub_container = ttk.Frame(self,
                                  padding=10,
                                  style='Frame.TFrame'
                                  )
        sub_container.grid(row=1, column=0, sticky="NSEW")       
        sub_container.rowconfigure((0,1), weight=1)
        sub_container.columnconfigure((0,1), weight=1)
        
        
        left_container = LeftContainer(sub_container,
                        lambda: self.show_frame(self.manual_bot_container),
                        lambda: self.show_frame(self.auto_bot_container),
                        self
                        )
        left_container.grid(row=0, column=0)
        
        
        right_container = RightContainer(sub_container, self)
        right_container.grid(row=0, column=1)
        
        
        self.manual_bot_container = ManualTemperature(sub_container)
        self.manual_bot_container.grid(row=1, column=0, columnspan=2)
        
        self.auto_bot_container= AutoTemperature(sub_container,left_container, self)
        self.auto_bot_container.grid(row=1, column=0, columnspan=2)
        
        self.select_advice = SelectAdvice(sub_container)
        self.select_advice.grid(row=1, column=0, columnspan=2)
        
        
        
        for child in sub_container.winfo_children():
            child.grid_configure(padx=5, pady=5, sticky="NSEW")
            child["padding"]=10
            if isinstance(child, tk.ttk.Frame) == True :
                child["style"]='Frame.TFrame'
            if isinstance(child, tk.ttk.LabelFrame) == True :
                child["style"]='Label.TLabelframe'

                
    def show_frame(self,frame):
        frame.tkraise()
    


 
       
        
class LeftContainer(ttk.Frame):
    def __init__(self, container, show_manual, show_auto, oven_frame, **kwargs):
        super().__init__(container, **kwargs)
        
        self.oven_frame = oven_frame
        
        self.show_manual = show_manual
        self.show_auto = show_auto
        
        self.rowconfigure((0,1), weight=1)
        self.columnconfigure((0), weight=1)
        
        vcmd = (self.register(self.onValidate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        
        self.gauge_value = tk.DoubleVar(value=0.0) 
        self.gauge = Gauge(
            self,
            width=300, 
            height=150,
            min_value=0,
            max_value=1200,
            divisions=5,
            label='Current Temperature',
            units='°C',
            bg="#D3E2F1"
        )
        self.gauge.grid(column=0, row=0, sticky ="NESW") 
        
        self.gauge.set_value(0)
        self.set_temperature()
        
        
        selection_temp_container= ttk.LabelFrame(self,
                                text="Target Temperatures Entry Mode",
                                style="Label.TLabelframe"
                                )
        selection_temp_container.grid(row=1, column=0, sticky="NESW")
        selection_temp_container.rowconfigure((0,1), weight=1)
        selection_temp_container.columnconfigure((0), weight=1)
        
        
        
        target_temp_mode_container= ttk.Frame(selection_temp_container, 
                                                   style="Frame.TFrame"
                                                   )
        target_temp_mode_container.grid(row=0, column=0, sticky="NESW")
        target_temp_mode_container.rowconfigure((0), weight=1)
        target_temp_mode_container.columnconfigure((0,1,2), weight=1)
        
        temperature_selection = tk.StringVar()
        linear_temperature = ttk.Radiobutton(
            target_temp_mode_container, 
            text="Linear", 
            variable=temperature_selection, 
            value="linear",
            command =  lambda : self.auto_selected(),
            #takefocus=False
        )
        linear_temperature.grid(row=0, column=0)
        
        log_temperature = ttk.Radiobutton(
            target_temp_mode_container, 
            text="Logarithmic", 
            variable=temperature_selection, 
            value="log",
            command =  lambda : self.auto_selected(),
            #takefocus=False
        )
        log_temperature.grid(row=0, column=1)
        
        manual_temperature = ttk.Radiobutton(
            target_temp_mode_container, 
            text="Manual", 
            variable=temperature_selection, 
            value="manual",
            command =  lambda : self.manual_selected(),
            #takefocus=False
        )
        manual_temperature.grid(row=0, column=2)
        
        for child in target_temp_mode_container.winfo_children():
            #child.grid_configure(padx=5, pady=5, sticky="NSEW")
            child["style"]="Radiobutton.TRadiobutton"
            #child["padding"]=10
            
            
            
        auto_temperature_container= ttk.Frame(selection_temp_container, 
                                         style="Frame.TFrame")
        auto_temperature_container.grid(row=1, column=0, sticky="NESW")
        auto_temperature_container.rowconfigure((0,1,2), weight=1)
        auto_temperature_container.columnconfigure((1), weight=1)

        
        number_point_label= ttk.Label(auto_temperature_container, 
                                      text="Number of points : ", 
                                      )
        number_point_label.grid(row=2, column=0)  
        self.number_point_value = tk.StringVar(value=12)
        self.number_point = ttk.Spinbox(
                                auto_temperature_container,
                                from_=2,
                                to=120,
                                increment=1,
                                textvariable=self.number_point_value
        )
        self.number_point.grid(column=1, row=2) 
        
        
        
        temperature_min_label= ttk.Label(auto_temperature_container, 
                                         text="Min. Temperature (°C) : ", 
                                         )
        temperature_min_label.grid(row=0, column=0)        
        self.temperature_min_value = tk.StringVar(value=0)
        self.temperature_min = ttk.Spinbox(
                                   auto_temperature_container,
                                   from_=0,
                                   to=120,
                                   increment=1,
                                   textvariable=self.temperature_min_value
        )
        self.temperature_min.grid(column=1, row=0)
        
        
        
        temperature_max_label= ttk.Label(auto_temperature_container, 
                                         text="Max.Temperature (°C) : ", 
                                         )
        temperature_max_label.grid(row=1, column=0)        
        self.temperature_max_value = tk.StringVar(value=200)
        self.temperature_max = ttk.Spinbox(
                                   auto_temperature_container,
                                   from_=0,
                                   to=120,
                                   increment=1,
                                   textvariable=self.temperature_max_value
        )
        self.temperature_max.grid(column=1, row=1)
        
        
        for child in auto_temperature_container.winfo_children():
            child.grid_configure(pady=5)
            if isinstance(child, tk.ttk.Label) == True :
                child.grid_configure(sticky="W")
                child["style"]='Label.TLabel'
            if isinstance(child, tk.ttk.Spinbox) == True :
                child.grid_configure(sticky="EW")
                child["justify"] = "center"
                child["validate"] = "key"
                child["validatecommand"] = vcmd
                child["style"]="Spinbox.TSpinbox"
                
    def onValidate(self, d, i, P, s, S, v,V, W):        
        # Disallow anything but numbers 
        if S.isdigit():
            return True
        elif S==".":
            return True
        else:
            self.bell()
            return False
        
                    
    def auto_selected(self):
        self.show_auto()
        self.number_point['state']='normal'
        self.temperature_max['state']='normal'
        self.temperature_min['state']='normal'
        
        
    def manual_selected(self):
        self.show_manual()
        self.number_point['state']='disabled'
        self.temperature_max['state']='disabled'
        self.temperature_min['state']='disabled'
        
        
    def set_temperature(self):
        coucou = self.oven_frame.main_app.communication_oven.real_temperaturee*10
        print("set_temperature", coucou)
        print("type", type(coucou))
        self.gauge.set_value(float(coucou))
#        current_temperature = 60
#        final_temperature = 60
#        remain=self.remain_time.get()
#        if current_temperature == final_temperature :
#            seconds = int(remain)
#            if seconds > 0 :
#                remain = seconds - 1
           
        
        self.gauge_value.set(f"{coucou}")    
        self._timer_decrement_job1 = self.after(1000, self.set_temperature)
        
        
    
    

      
        
class RightContainer(ttk.Frame):
    def __init__(self, container, oven_frame, **kwargs):
        super().__init__(container,**kwargs)
        self.oven_frame = oven_frame
        self.rowconfigure((0,1,2), weight=1)
        self.columnconfigure((0), weight=1)
        
        vcmd = (self.register(self.onValidate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        
       
        spinbox_container= ttk.Frame(self, 
                                      #padding=10, 
                                      style="Frame.TFrame")
        spinbox_container.grid(row=0, column=0, 
                               #rowspan=4, 
                               sticky="NESW"
                               )
        spinbox_container.rowconfigure((0,1,2,3), weight=1)
        spinbox_container.columnconfigure((1), weight=1)
        
        
        
        rise_rate_label= ttk.Label(spinbox_container, 
                                    text="Rise Rate (°C/min) : ", 
                                    style="Label.TLabel"
                                    )
        rise_rate_label.grid(row=0, column=0)       
        rise_rate_value = tk.StringVar()
        rise_rate = ttk.Spinbox(spinbox_container,
                                from_=0,
                                to=120,
                                increment=1,
                                textvariable=rise_rate_value
        )            
        rise_rate.grid(row=0, column=1)
        
        
        
        accuracy_label= ttk.Label(spinbox_container, 
                                  text="Accuracy (°C) : ", 
                                  style="Label.TLabel")
        accuracy_label.grid(row=1, column=0)       
        accuracy_value = tk.StringVar()
        accuracy = ttk.Spinbox(spinbox_container,
                                from_=0,
                                to=120,
                                increment=1,
                                textvariable=accuracy_value
        )
        accuracy.grid(row=1, column=1)
        
        
        
        annealing_label= ttk.Label(spinbox_container, 
                                    text="Annealing time (s) : ", 
                                    style="Label.TLabel")
        annealing_label.grid(row=2, column=0, 
                              sticky ="W")        
        self.annealing_value = tk.StringVar()
        annealing = ttk.Spinbox(spinbox_container,
                                from_=0,
                                to=120,
                                increment=1,
                                textvariable=self.annealing_value
        )
        annealing.grid(row=2, column=1)
        
        
        
        annealing_remain_label= ttk.Label(spinbox_container, 
                                          text="Remaining (s) : ", 
                                          style="Label.TLabel"
                                          )
        annealing_remain_label.grid(row=3, column=0, sticky ="W")        
        self.remain_time = tk.StringVar()
        self._timer_decrement_job = None
        annealing_remain = ttk.Label(spinbox_container,
                                    textvariable=self.remain_time,
        )
        annealing_remain.grid(column=1, row=3, 
                              sticky ="EW")
        
        
        for child in spinbox_container.winfo_children():
            child.grid_configure(pady=5)
            if isinstance(child, tk.ttk.Label) == True :
                if child != annealing_remain:
                    child.grid_configure(sticky="W")
                    child["style"]='Label.TLabel'
            if isinstance(child, tk.ttk.Spinbox) == True :
                child.grid_configure(sticky="EW")
                child["justify"] = "center"
                child["validate"] = "key"
                child["validatecommand"] = vcmd
                
                
                
        
        button_container = ttk.Frame(self, 
                                     #padding=5, 
                                     style="Frame.TFrame"
                                     )
        button_container.grid(row=1, column=0, sticky="NSEW")
        button_container.rowconfigure((0), weight=1)
        button_container.columnconfigure((0,1,2), weight=1)

        
        
        play_button = ttk.Button(button_container, text="Play", width=6, 
                                  style="Button.TButton", command=self.play)
        play_button.grid(row=0, column=0)
        
        stop_button = ttk.Button(button_container, text="Stop", width=6, 
                                  style="Button.TButton")
        stop_button.grid(row=0, column=2)
        
        next_button = ttk.Button(button_container, text="Next", width=6, 
                                  style="Button.TButton",  command=self.next_temperature)
        next_button.grid(row=0, column=1)
        
        
        dialogue_box_container= ttk.LabelFrame(self, 
                                               padding=10, 
                                               text="Dialogue Box",
                                               style="Label.TLabelframe"
                                               )
        dialogue_box_container.grid(row=2, column=0,
                                    sticky="NSEW"
                                    )        
        dialogue_value = tk.StringVar()
        dialogue_box = ttk.Label(dialogue_box_container, 
                                 textvariable=dialogue_value,
                                 style="Label.TLabel"
                                 )
        dialogue_box.grid(row=0, column=0)
        
        
    def play (self):
        self.play_pressed = True
        value = self.annealing_value.get()
        self.remain_time.set(f"{value}") 
        self.remaining_time()
        
    def next_temperature (self) :
        self.oven_frame.main_app.communication_oven.temperature_iterator += 1
        self.oven_frame.main_app.communication_oven.next_temperature()
        print ("order",self.oven_frame.main_app.communication_oven.order_temperature)
        
    def remaining_time(self):
        current_temperature = 60
        final_temperature = 60
        remain=self.remain_time.get()
        if current_temperature == final_temperature :
            seconds = int(remain)
            if seconds > 0 :
                remain = seconds - 1
            
            self.remain_time.set(f"{remain}")    
            self._timer_decrement_job = self.after(1000, self.remaining_time)

             
    def onValidate(self, d, i, P, s, S, v,V, W):        
      # Disallow anything but numbers 
        if S.isdigit():
            return True
        elif S==".":
            return True
        else:
            self.bell()
            return False
        

    
        
class ManualTemperature(ttk.LabelFrame):
    
    def __init__(self, parent, **kwargs):        
        super().__init__(parent)
        
        self.rowconfigure((0,1), weight=1)
        self.columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12), weight=1)
        
        self["style"] = "Label.TLabelframe"
        self["text"] = "Target Temperatures"
        
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
    
    def __init__(self, parent, controller, oven_frame, **kwargs):       
        super().__init__(parent,**kwargs)
        
        self.rowconfigure((0,1), weight=1)
        self.columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12), weight=1)
        
        self["style"] = "Label.TLabelframe"
        self["text"] = "Target Temperatures"
        
        
        self.width=4
        self.controller = controller
        self.oven_frame = oven_frame
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
               
        validation_button = ttk.Button(self, text="Enter", width=8, padding=0,
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
        
        
        for i in range(0,24):
            self.temperature_value[i].set(" ")
        
        for i in range(0,int(number_point)):
            temperature.append(0)
            temperature[i] = round(int(temperature_min)+
                (((int(temperature_max)-int(temperature_min))/
                  (int(number_point)-1))*i))
            self.temperature_value[i].set(f"{temperature[i]}")
        self.oven_frame.main_app.communication_oven.list_temperatures_ordered = f"{temperature}"
        self.oven_frame.main_app.communication_oven.update_temperatures()
     
            
    def clear(self):
        for i in range(0,24):
            self.temperature_value[i].set(" ")
            
            
            
class SelectAdvice(ttk.LabelFrame):    
    def __init__(self, parent, **kwargs):
        super().__init__(parent,**kwargs)
        
        self.rowconfigure((0), weight=1)
        self.columnconfigure((0), weight=1)
        
        self["style"] = "Label.TLabelframe"
        self["text"] = "Target Temperatures"

        
        advice = ttk.Label(self,text="Please select a temperature entry mode",
                         padding=10,
                         borderwidth=2, relief="ridge")
        
        advice.place(anchor='center',relx=0.5, rely=0.2)