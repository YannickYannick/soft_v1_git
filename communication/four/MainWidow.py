import tkinter as tk
from Application_four import MainApplication
import pid_widgets
import Class_four
import matplotlib.animation as animation
import time

class MainWindow(tk.Tk):
    
    def __init__(self):
        
        tk.Tk.__init__(self)
        self.régulation = Class_four.FonctionPID()
        self.application = MainApplication(self)
        

 


mainwindow = MainWindow()
mainwindow.mainloop()
time.sleep(5)

"""
i = 0
while True:

    mainwindow.update()
    mainwindow.reegulationn.ani = animation.FuncAnimation(self.reegulationn, self.reegulationn.update, fargs=(i,), interval=100)

    time.sleep(0.2)
"""
