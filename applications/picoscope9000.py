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
        
        self.application = application
        self.strdata = [1,2,3,4,5]
        self.data = [1,2,3,4,5]
# comment deletting
        ############ MODEL #############
        self.COMRCW = win32com.client.Dispatch("PicoScope9000.COMRC") # create COM object   
        self.COMRCW.ExecCommand("Gui:Control:Invisible")
        self.COMRCW.ExecCommand("Header Off")
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
        self.COMRCW.ExecCommand(" ACQuire:CH1:MODE AVGSTAB;NAVG 20")
        self.data = range(512)
        self.update_val  = 0
        self.reglage_1_moins_un = '0.0' # nouvelle variable -> ctrl+f : déclenchement lors d'un changement de valeur
        self.start()

    
 
        
    # def run(self):
    #     for i in range(2000):
    #         

    #          # create COM object 
    #         
            
    #         self.strdata = self.COMRCW.ExecCommand("Wfm:Data?") 
    #         print (self.strdata )
    #         self.strdata = str(self.strdata)
           
    #         self.strdata = self.strdata.split(',')
           
    #         self.strdata = np.asarray(self.strdata)
            
    #         self.data = self.strdata.astype(np.float)
            
      
    #         self.axe_yy = self.data
            
    #         time.sleep(0.2)
            
    # def update(self):
    #     # probleme lorsqu'on sort de la boucle
    #     #pythoncom.CoInitialize()
    #     #self.COMRCW = win32com.client.Dispatch("PicoScope9000.COMRC") 
    #     self.update_val = 1
        

        
        
    def run(self):
        for i in range(50):
            pythoncom.CoInitialize()
            self.COMRCW = win32com.client.Dispatch("PicoScope9000.COMRC")
            print(self.reglage_1_moins_un, self.application.reglage_1 )
            print(self.COMRCW.ExecCommand("TB:ScaleA?"))
            
            #déclenchement lors d'un changement de valeur
            if self.reglage_1_moins_un != self.application.reglage_1 :
                
                print("niveau 1 = ok") #niveau 1
                print("melina",self.application.reglage_1) #niveau 2
                
                
                #niveau 3
                #command random, influant sur l'echelle de temps (meme si le widget est toujours prévu pour moyenne)     
                self.command = "TB:ScaleA?" + self.application.reglage_1 + "n"
                self.COMRCW.ExecCommand(self.command) #update time scale
             
                #self.update_val  = 0                  
                self.reglage_1_moins_un = self.application.reglage_1 
                
            self.strdata = self.COMRCW.ExecCommand("Wfm:Data?")
            self.strdata = str(self.strdata)
            self.strdata = self.strdata.split(',')
            self.strdata = np.asarray(self.strdata)   
            self.data = self.strdata.astype(np.float)
            
            time.sleep(2)
            
 
        
        
"""

class LivePlotting(plt.Figure):
    def __init__(self, fenetre, application):
        plt.Figure.__init__(self, figsize=(5,4), dpi=200)
        self.application = application
        figure = self
        self.line = self.add_subplot(1,1,1)
        self.axe_x = range(512)       
        self.axe_y = range(512)
        
        self.iterator = 0
        
        self.canvas = FigureCanvasTkAgg(self, master=fenetre)
        self.canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        
        
        self.start()
        
    def update(self, i):
        self.iterator += 1
        self.line.clear()
    
        self.axe_y = self.application.communication_picoscope.data
 
      
        self.line.plot(self.axe_x, self.axe_y, label='consigne', color='green' )
        
        
        
        # Format plot
        
    def start(self):
        self.ani = animation.FuncAnimation(self, self.update, interval=100)
        plt.show()
 """    
  
class LivePlotting(tk.Frame):
    def __init__(self, parent, application, **kwargs):
        tk.Frame.__init__(self, parent, width=768, height=576, bg='red', **kwargs)
        self.pack(fill=tk.BOTH)
        
        self.application = application

        self.graph = plt.Figure(figsize=(5,4), dpi=200)
        

        self.line = self.graph.add_subplot(1,1,1)
        
        
        self.axe_x = range(5)
        #self.axe_x = range(512)       
        self.axe_y = range(512)
        
        self.iterator = 0
        
        self.canvas = FigureCanvasTkAgg(self.graph, master=self)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH)
        
        
        self.start()
        
    def update(self, i):
        self.iterator += 1
        self.line.clear()
    
        self.axe_y = self.application.communication_picoscope.data
        #pb au niveau des dimensions, pas important pour melinda, il me semble 
        self.line.plot(self.axe_y, self.axe_y, label='consigne', color='green' )
        
        
        
        # Format plot
        
    def start(self):
        self.graph.ani = animation.FuncAnimation(self, self.update, interval=100)
        plt.show()


class ApplicationPicoscope(threading.Thread):
    
    def __init__(self, parent, **kwargs):  
        #super().__init__(self)
        threading.Thread.__init__(self)
        self.main_windows = parent
        
        
        self.reglage_1 = "coou"
        #print("============================================================!",self.reglage_1)

        
        self.communication_picoscope = CommunicationPicoscope(self)
      
        self.courbe = LivePlotting(self.main_windows, self)
        self.courbe.place(relx=0.02, rely=0.45, relwidth=0.96, relheight=0.48)

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

# root = tk.Tk()
# PicoscopeFrame(root)
# root.mainloop()

"""
COMRCW.ExecCommand("*RunControl:Single")  # Set running mode of scope
time.sleep(2)
COMRCW.ExecCommand("Header Off") # Turn off headers for returned values

strdata = COMRCW.ExecCommand("Wfm:Data?")       # Get wfm data for ch1

YU = COMRCW.ExecCommand("Wfm:Preamb:YU?")       # Get y scale units
XU = COMRCW.ExecCommand("Wfm:Preamb:XU?")       # Get x scale units
XInc = COMRCW.ExecCommand("Wfm:Preamb:XInc?")   # Get time sample interval
XOrg = COMRCW.ExecCommand("Wfm:Preamb:XOrg?")   # Get y axis origin

# Measurements
freq = COMRCW.ExecCommand("Meas:Res:1?")
print("Frequency = " + str(freq))
riseTime = COMRCW.ExecCommand("Meas:Res:2?")
print("Rise Time = " + str(riseTime))
maximum = COMRCW.ExecCommand("Meas:Res:3?")
print("Maximum = " + str(maximum))
minimum = COMRCW.ExecCommand("Meas:Res:4?")
print("Minimum = " + str(minimum))
Pp = COMRCW.ExecCommand("Meas:Res:5?")
print("Peak-to-Peak = " + str(Pp))

# Convert data to array of floats
strdata = str(strdata)
strdata = strdata.split(',')
strdata = np.asarray(strdata)
data = strdata.astype(np.float)

# Create time data array
totaltime = len(data) * float(XInc)
totaltime = float(totaltime)
datatime = np.linspace(0, totaltime, len(data))

# Plot data
plt.plot(datatime, data)
plt.title('PicoScope 9300 Series Single Acquisition Example')
plt.xlabel('Time (' + XU +')')
plt.ylabel('Voltage (' + YU +')')
plt.show()

COMRCW = 1
"""