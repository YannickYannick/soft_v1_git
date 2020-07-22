import threading
import pandas
import time 

import datetime as dt
import numpy as np
from random import random

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import tkinter as tk
import ttk

from tkinter import *
from Def_four import *

import serial
import pid_widgets
import Class_four
import serial
import math
time.sleep(1)
from io import StringIO
import csv
from tkinter import *
from tkinter.ttk import *


from tkinter import *
import tkinter as tk
# creating tkinter window 
  

  


        
    
    
        
class MainWindow(tk.Tk):
    
    def __init__(self):
        
        tk.Tk.__init__(self)
        self.minsize(height=800, width=1300)
    
        self.temps_plateau = 0
        self.input_temperatures = pid_widgets.InputTemperatures(self,  background="Blue")
        #self.plage_températures.grid(row=1, column=0, columnspan=2, rowspan=2, padx=5, pady=5)
       
        self.input_temperatures.place(relx=0.02, rely=0.02, relwidth=0.55, relheight=0.2)
        
        self.indicators_layout = pid_widgets.IndicatorsLayout(self,  background="Green")
        self.indicators_layout.place(relx=0.78, rely=0.02, relwidth=0.2, relheight=0.96 )
        
        
        self.main_menu = pid_widgets.MainMenu(self)
        
        
        self.config(menu=self.main_menu)
       

        self.application = Class_four.CommunicationOven(self)
#        self.application.liveplotting.canvas.get_tk_widget().place(relx=0.02, rely=0.3, relwidth=0.55, relheight=0.6 )
        self.application.barPID.place(relx=0.6, rely=0.3, relwidth=0.02, relheight=0.6 )
        self.label = tk.Label(self, text=11)
        self.label.pack()
        
        self.protocol('WM_DELETE_WINDOW', self.doSomething)  # root is your root window
        
        self.bouton_test = tk.Button(self, text='close_all', command=self.test_fermeture).pack()
        
        
    def test_fermeture(self):
        self.application.i2cprotocol.stop()
        self.application.regulation_fonction.arret = True
        self.application.arret = True
        
    def __enter__(self):
        print("entered ..")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("MMMM")

        

    def doSomething(self):
        self.application.stop()
     #   self.application.regulation_fonction.arret = True
     #  self.application.arret = True
    # check if saving
    # if not:
        self.destroy()
        
        
    def destroyy(self):
        #self.application.i2cprotocol.stop()
        print("__________________________________________________________________________________")
       
        self.quit()
    def pid_fenetre(self):
        self.pid_fenetre = pid_widgets.InputLayout(self)
        
    

        
        


        

 


mainwindow = MainWindow()
mainwindow.mainloop()
time.sleep(5)

