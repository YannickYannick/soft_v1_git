#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 18:39:04 2020

@author: melinapannier
"""

import tkinter as tk
from tkinter import ttk
from applications import PicoscopeFrame
#import time


class Oscilloscope(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(**kwargs)
        
        self.update_val  = 0
        container = ttk.Frame(self, padding=10, height=450, width=800,
                              style="Frame.TFrame")
        container.grid(row=0, column=0, sticky="NESW")
        container.grid_propagate(0)

        title_frame = ttk.Label(container, text="OSCILLOSCOPE CONTROL", 
                                style="Title.TLabel")
        title_frame.grid(column=0, row=0, sticky ="NESW")
        
        
        data_plot = ttk.Label(container, text="plot")
        data_plot.grid(column=0, row=1, sticky="NESW")
        
        
        left_container= ttk.Frame(container, padding=10, style="Frame.TFrame")
        left_container.grid(row=1, column=1, columnspan=1, sticky="NESW")
        left_container.rowconfigure((0, 1, 2, 3, 4), weight=1)        
        
        dialogue_value = tk.StringVar(value="dialogue window")
        dialogue_window = ttk.Entry(left_container, 
                                    textvariable=dialogue_value)
        dialogue_window.grid(row=0, column=0, pady=5, sticky="NESW")
        
        oscilloscope_selection = tk.StringVar()
        oscillo1 = ttk.Radiobutton(
            left_container, 
            text="Picoscope 1 (2204A)", 
            variable=oscilloscope_selection, 
            value="pico1",
            style="Radiobutton.TRadiobutton"
        )
        oscillo1.grid(column=0, row=1, sticky="NESW")
        
        oscillo2 = ttk.Radiobutton(
            left_container, 
            text="Picoscope 2 (9000)", 
            variable=oscilloscope_selection, 
            value="pico2",
            style="Radiobutton.TRadiobutton"
        )
        oscillo2.grid(column=0, row=2, sticky="NESW")


         
        spinbox_container= ttk.Frame(left_container, padding=10, 
                                     style="Frame.TFrame")
        spinbox_container.grid(row=3, column=0, sticky="NESW")
        spinbox_container.columnconfigure((0, 1), weight=1)
        
        
        time_scale_label = ttk.Label(spinbox_container, text="Time Scale", 
                                     style="Label.TLabel")
        time_scale_label.grid(column=0, row=0, sticky="NESW")
               
        self.time_scale_value = tk.StringVar()
        time_scale_input = ttk.Spinbox(
            spinbox_container,
            from_=0,
            to=120,
            increment=1,
            justify="center",
            textvariable=self.time_scale_value,
            width=10,
        )
        time_scale_input.grid(column=1, row=0, sticky="NESW")
        time_scale_input.bind('<KeyRelease>',self.entry_in_timespinbox)
        
   
        average_label = ttk.Label(spinbox_container, text="Average", 
                                  style="Label.TLabel") 
        average_label.grid(column=0, row=1, sticky="NESW")
        
        self.average_value = tk.StringVar(value=0.0)
        
        
        average_scale = ttk.Scale(left_container, orient="horizontal", 
                                  from_=0, to=5000000, variable = self.average_value)
        average_scale.grid(column=0, row=5, sticky="NESW")
        #average_scale.bind('<Motion>',self.motion_in_scale)
        
        # round_average_value = tk.StringVar()
        # average = self.average_value.get()
        # round_average = round(float(average))
        # print(round_average)
        # round_average_value.set(f"{round_average}") 
        
        average_display = ttk.Label(spinbox_container, textvariable=self.average_value, width=8) 
        average_display.grid(column=1, row=1, sticky="NESW")
        print("avant")
        #self.CommunicationPicoscope()
        
        test = PicoscopeFrame(container, self)
        test.grid(column=0, row=1, sticky="NESW")
        
    def motion_in_scale(self,event):
        #print("Mouse position: (%s %s)" % (event.x, event.y))
        received_average = self.average_value.get()
        #self.update_val  = 1
        #print(received_average)
        
    def entry_in_timespinbox(self,event):
        received_time_scale = self.time_scale_value.get()
        self.update_val  = 1
        self.CommunicationPicoscope()
        #print(received_time_scale)
        

    #def CommunicationPicoscope(self):


        # self.strdata = [1,2,3,4,5]
        # self.data = [1,2,3,4,5]
        
        # for i in range(2000):
        #     print("self.update_val",self.update_val)
        #     time.sleep(1)
        #     if self.update_val == 1 :
        #         received_time_scale = self.time_scale_value.get()
        #         print(received_time_scale,i)
                
                
#         ############# MODEL #############
#         self.COMRCW = win32com.client.Dispatch("PicoScope9000.COMRC") # create COM object   
#         self.COMRCW.ExecCommand("Gui:Control:Invisible")
#         self.COMRCW.ExecCommand("Header Off")
#         # Set up measurements
#         self.COMRCW.ExecCommand("TB:ScaleA? 1m")  
#         self.COMRCW.ExecCommand("Meas:Display:Param")
#         self.COMRCW.ExecCommand("Meas:DisplSrc:Ch1")
#         self.COMRCW.ExecCommand("Meas:Mode:Single")
#         self.COMRCW.ExecCommand("Meas:Ch1:XParam:Freq 1")
#         self.COMRCW.ExecCommand("Meas:Ch1:XParam:Rise 1")
#         self.COMRCW.ExecCommand("Meas:Ch1:YParam:Max 1")
#         self.COMRCW.ExecCommand("Meas:Ch1:YParam:Min 1")
#         self.COMRCW.ExecCommand("Meas:Ch1:YParam:PP 1")
#         self.COMRCW.ExecCommand("Trig:Mode Trig")
# #        self.COMRCW.ExecCommand("Trig:Source? Direct")
#         self.COMRCW.ExecCommand(" ACQuire:CH1:MODE AVGSTAB;NAVG 20")
        #self.data = range(512)
#         self.update_val  = 0
#         self.start()

    
 
        
    #     for i in range(2000):
    #         pythoncom.CoInitialize()

    #         self.COMRCW = win32com.client.Dispatch("PicoScope9000.COMRC") # create COM object 
    #         if update_val == 1 :
    #             self.COMRCW.ExecCommand(self.application.reglage_1) #update time scale
    #             self.COMRCW.ExecCommand(self.application.reglage_3)
    #             self.update_val  = 0
            
    #         self.strdata = self.COMRCW.ExecCommand("Wfm:Data?") 
    #         print (self.strdata )
    #         self.strdata = str(self.strdata)
           
    #         self.strdata = self.strdata.split(',')
           
    #         self.strdata = np.asarray(self.strdata)
            
    #         self.data = self.strdata.astype(np.float)
            
      
    #         self.axe_yy = self.data
            
    #         time.sleep(0.2)
    
    
            
        

# #demo:
# window = tk.Tk()
# test_frame = Oscilloscope(window)
# test_frame.grid()


# window.mainloop()