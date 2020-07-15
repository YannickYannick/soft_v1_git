import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

import tkinter as tk
from tkinter import *


import win32com.client
import numpy as np
import matplotlib.pyplot as plt
import time
import threading
import pythoncom


#import widgets_picoscope

class CommunicationPicoscope(threading.Thread):
    def __init__(self, application):
        threading.Thread.__init__(self)
        self.picoscope_properties = {"self.average":0, "self.time_scale":0}
        
        
        self.application = application
        self.strdata = [1,2,3,4,5]
        self.data = [1,2,3,4,5]
# comment deletting
        ############ MODEL #############
        self.COMRCW = win32com.client.Dispatch("PicoScope9000.COMRC") # create COM object   
        self.COMRCW.ExecCommand("Gui:Control:Invisible")
        self.COMRCW.ExecCommand("Header Off")
        
        self.COMRCW.ExecCommand(" ACQuire:CH1:MODE AVGSTAB")
        self.picoscope_properties["self.average"] = self.COMRCW.ExecCommand("ACQuire:CH1:NAVG?")
        self.picoscope_properties["self.time_scale"] = self.COMRCW.ExecCommand("TB:ScaleA?") 

        
         # Set up measurements
        self.COMRCW.ExecCommand("TB:ScaleA? 1m")  
        self.COMRCW.ExecCommand("Meas:Display:Param")
        self.COMRCW.ExecCommand("Meas:DisplSrc:Ch1")
        self.COMRCW.ExecCommand("Meas:Mode:Single")
        self.COMRCW.ExecCommand("Meas:Ch1:XParam:Freq 1")
        self.COMRCW.ExecCommand("Meas:Ch1:XParam:Rise 1")
        self.COMRCW.ExecCommand("Meas:Ch1:YParam:Max 1")
        self.COMRCW.ExecCommand("Meas:Ch1:YParam:Min 1")
        self.COMRCW.ExecCommand("Meas:Ch1:YParam:PP 1")
        self.COMRCW.ExecCommand("Trig:Mode Trig")
 #        self.COMRCW.ExecCommand("Trig:Source? Direct")
        
        
        self.data = range(512)
        self.update_val  = 0
        self.average_before = self.picoscope_properties["self.average"] # nouvelle variable -> ctrl+f : déclenchement lors d'un changement de valeur
        self.start()

    
 
        


        
        
    def run(self):
        for i in range(10):
            pythoncom.CoInitialize()
            self.COMRCW = win32com.client.Dispatch("PicoScope9000.COMRC")
            
            
            #déclenchement lors d'un changement de valeur
            if self.average_before != self.picoscope_properties["self.average"] :
                
                print("niveau 1 = ok") #niveau 1
                print("melina",self.picoscope_properties["self.average"]) #niveau 2
                
                
                #niveau 3
                self.command = "ACQuire:CH1:NAVG " + self.picoscope_properties["self.average"]
                self.COMRCW.ExecCommand(self.command) #update time scale
               
             
                           
                self.average_before = self.picoscope_properties["self.average"]
                
            self.strdata = self.COMRCW.ExecCommand("Wfm:Data?")
            self.strdata = str(self.strdata)
            self.strdata = self.strdata.split(',')
            self.strdata = np.asarray(self.strdata)   
            self.data = self.strdata.astype(np.float)
            
        
            time.sleep(1) #1 second = un peu lent
            
 
        
        
  
  
CommunicationPicoscope(1)


class ApplicationPicoscope(threading.Thread):
    
    def __init__(self, parent, **kwargs):  
        #super().__init__(self)
        threading.Thread.__init__(self)
        self.main_windows = parent
        
        
        self.reglage_1 = "coou"
        #print("============================================================!",self.reglage_1)

        
        
      
   

        self.start()
        
        
    def run(self):
        for i in range(60):
            #self.reglage_1 = self.main_windows.widgets_picoscope.reglage_amplitude.consigne_picoscope
            self.reglage_1 = self.main_windows.controller.average_value.get()
            #self.reglage_3 = self.main_windows.widgets_picoscope.reglage_temps_unite.consigne_picoscope
            
         
            time.sleep(1)
        
        
    def update(self):
        
        self.communication_picoscope.update()  

        
        
        
class PicoscopeFrame(tk.Frame):
    
    
    def __init__(self, fenetre, controller, **kwargs):
        
        tk.Frame.__init__(self, fenetre, width=300, height=200, bg='red', **kwargs)
        self.pack(fill=tk.BOTH)
    
        self.controller = controller
        #self.average = self.controller.average_value 
        #self.consigne_picoscope = self.parametre_consigne + " " + str(self.param_value) + self.parametre_unite
        
        # self.widgets_picoscope = widgets_picoscope.WidgetsOscilloscope(self, "oscilloscope")
        
       
        self.application_picoscope = ApplicationPicoscope(self)
        
        
        
    def update(self):
        self.application_picoscope.update()

