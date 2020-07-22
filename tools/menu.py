import tkinter as tk
from PIL import Image, ImageTk
from tkinter import LEFT, TOP, X, FLAT, RAISED

class MainMenu(tk.Menu):
    def __init__(self, master):
        tk.Menu.__init__(self, master)
        self.master = master
        self.filemenu = tk.Menu(self, tearoff=0)
        self.filemenu.add_command(label="New", command=self.donothing)
        self.filemenu.add_command(label="Open", command=self.donothing)
        self.filemenu.add_command(label="Save", command=self.donothing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.donothing)
        self.add_cascade(label="File", menu=self.filemenu)
        
        self.pid_parameters = tk.Menu(self, tearoff=0)
        self.pid_parameters.add_command(label="régler pid", command=self.pid_parameters)
        self.add_cascade(label="PID_tunning", menu=self.pid_parameters)

        self.helpmenu = tk.Menu(self, tearoff=0)
        self.helpmenu.add_command(label="Help Index", command=self.donothing)
        self.helpmenu.add_command(label="About...", command=self.donothing)
        self.add_cascade(label="Help", menu=self.helpmenu)
        
        self.img = Image.open("C:/Users/yannb/OneDrive/Pictures/play.PNG")
        img = ImageTk.PhotoImage(self.img)
      

        exitButton = tk.Button(self.master, image=img, relief=tk.FLAT, command=self.test) #(y->m)
        exitButton.image = img
        exitButton.grid(row=0, column=0)
         
    def test(self):
        print(111111111111)
        
    def pid_parameters(self):
        self.pid_master = InputLayout(self.master)
    
    def donothing(self):
        print("do nothing")