from io import StringIO
import csv
import tkinter as tk
import time
import threading




from tkinter import *
import tkinter as tk

def donothing():
   pass



class MainMenu(tk.Menu):
    def __init__(self, fenetre):
        tk.Menu.__init__(self, fenetre)
        self.fenetre = fenetre
        self.filemenu = Menu(self, tearoff=0)
        self.filemenu.add_command(label="New", command=donothing)
        self.filemenu.add_command(label="Open", command=donothing)
        self.filemenu.add_command(label="Save", command=donothing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=donothing)
        self.add_cascade(label="File", menu=self.filemenu)
        
        self.pid_parameters = Menu(self, tearoff=0)
        self.pid_parameters.add_command(label="régler pid", command=self.pid_fenetre)
        self.add_cascade(label="PID_tunning", menu=self.pid_parameters)

        self.helpmenu = Menu(self, tearoff=0)
        self.helpmenu.add_command(label="Help Index", command=donothing)
        self.helpmenu.add_command(label="About...", command=donothing)
        self.add_cascade(label="Help", menu=self.helpmenu)
        
    def pid_fenetre(self):
        self.pid_fenetre = InputLayout(self.fenetre)
        
        
    



class InputTemperatures(tk.Frame, threading.Thread):
    
    """Lot des widgets nécessaire aux paramètre du PID."""
    
    def __init__(self, fenetre, **kwargs):
        tk.Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        threading.Thread.__init__(self)
        self.order_temperatures_user = []
        self.order_temperature_plot = 0
        self.iterator = 0
        # proportionnal coeff :
        #___________________________________________________________________
        self.layout_temperatures_selected = tk.Frame(self)
        self.temperatures_selected_caption = tk.Label(self.layout_temperatures_selected, text="liste des températures")
        self.temperatures_selected_caption.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.3)
        
        self.var_texte = tk.StringVar() 
        self.texte_utilisateur = tk.Entry(self.layout_temperatures_selected, textvariable=self.var_texte, width=40)
        self.texte_utilisateur.place(relx=0.02, rely=0.33, relwidth=0.96, relheight=0.3)
        
        self.temperatures_selected = tk.Label(self.layout_temperatures_selected, width=35)
        self.temperatures_selected.place(relx=0.02, rely=0.66, relwidth=0.96, relheight=0.3)
        
        self.layout_temperatures_selected.place(relx=0.02, rely=0.02, relwidth=0.75, relheight=0.75)
        #___________________________________________________________________
        
        self.bouton_cliquer_valider_temperatures = tk.Button(self, text="valider", command=self.valider_temperatures, height = 4, width = 5)
        self.bouton_cliquer_valider_temperatures.place(relx=0.78, rely=0.02, relwidth=0.2, relheight=0.75)
        
        

        
        
        self.temperature_order_temperature_caption = tk.Label(self, text="temperature_order_temperature")
        #self.temperature_order_temperature_caption.grid(row=2, column=0, padx=5, pady=5)
        
        self.temperature_order_temperature = tk.Label(self, text=0)
        #self.temperature_order_temperature.pack()
        
        
         
        
        
        self.var_case = tk.StringVar()
        self.case = tk.Checkbutton(self, text="ACTIVER", variable=self.var_case)
        #self.case.pack()
        
        self.param_value="0"
        
        #-------Bouttons------------------->
        self.layout_bouttons_control = tk.Frame(self)
        
        self.bouton_debut = tk.Button(self.layout_bouttons_control, text="debut", command=self.cliquer_bouton_debut)
        self.bouton_debut.place(relx=0.02, rely=0.02, relwidth=0.15, relheight=0.96)
        
        self.bouton_precedent = tk.Button(self.layout_bouttons_control, text="précédent", command=self.cliquer_bouton_precedent)
        self.bouton_precedent.place(relx=0.18, rely=0.02, relwidth=0.15, relheight=0.96)
        
        self.bouton_pause = tk.Button(self.layout_bouttons_control, text="pause", command=self.cliquer_bouton_pause)
        self.bouton_pause.place(relx=0.34, rely=0.02, relwidth=0.15, relheight=0.96)
                                
        self.bouton_play = tk.Button(self.layout_bouttons_control, text="play", command=self.cliquer_bouton_play)
        self.bouton_play.place(relx=0.51, rely=0.02, relwidth=0.15, relheight=0.96)
             
        self.bouton_suivant = tk.Button(self.layout_bouttons_control, text="suivant", command=self.cliquer_bouton_suivant)
        self.bouton_suivant.place(relx=0.67, rely=0.02, relwidth=0.15, relheight=0.96)
        
        self.bouton_fin = tk.Button(self.layout_bouttons_control, text="fin", command=self.cliquer_bouton_fin)
        self.bouton_fin.place(relx=0.83, rely=0.02, relwidth=0.15, relheight=0.96)
    
        
        self.layout_bouttons_control.place(relx=0.02, rely=0.8, relwidth=0.96, relheight=0.2)
        
       
    def run(self):    
            self.order_temperatures_user = self.get_temps()
            self.order_temperatures_user = StringIO(self.order_temperatures_user)
            self.order_temperatures_user = csv.reader(self.order_temperatures_user, delimiter=',')
            
            self.order_temperatures_user = list(self.order_temperatures_user)[0]
           
            self.order_temperatures_user = [float(i) for i in self.order_temperatures_user]
            
            
            
            self.order_temperature_plot = self.order_temperatures_user[self.iterator]
            self.temperature_order_temperature["text"] = self.order_temperature_plot

            
            time.sleep(0.5)
        

    def valider_temperatures(self):
        
        self.temperatures_selected["text"] = self.texte_utilisateur.get()
        self.What_User_Wrote = self.texte_utilisateur.get()
      
        self.param_value = self.What_User_Wrote
        self.run()
        
    def cliquer_bouton_suivant(self):
        self.iterator += 1
        self.run()
        
    def cliquer_bouton_precedent(self):
        self.iterator -= 1
        self.run()
    def cliquer_bouton_pause(self):
        pass
    
    def cliquer_bouton_play(self):
        pass
    
    def cliquer_bouton_fin(self):
        self.iterator = len(self.order_temperatures_user)
        
    def cliquer_bouton_debut(self):
        self.iterator = 0
        
        
        
        
        
        
    def get_temps(self):
        a = self.temperatures_selected
     
        return self.param_value
    




class InputParameter(tk.Frame):
    
    """Lot des widgets nécessaire aux paramètre du PID."""
    
    def __init__(self, fenetre, name, **kwargs):
        tk.Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.fenetre = fenetre
        self.pack(fill=tk.BOTH)
      
        
        # proportionnal coeff :
        self.caption = tk.Label(self, text=name)
        self.caption.pack()

        

        
        self.message = tk.Label(self, text="0")
        self.message.pack()
        
        self.bouton_cliquer = tk.Button(self, text="valider", command=self.cliquer)
        self.bouton_cliquer.pack(side="right")
         
        self.var_texte = tk.DoubleVar(value=0)
        
        self.texte_utilisateur = tk.Entry(self, textvariable=self.var_texte, width=40)
        self.texte_utilisateur.pack()
        
        self.var_case = tk.IntVar()
        self.case = tk.Checkbutton(self, text="ACTIVER", variable=self.var_case)
        self.case.pack()
        
        self.param_value=0

    def cliquer(self):
        
        self.message["text"] = self.texte_utilisateur.get()
        self.What_User_Wrote = self.texte_utilisateur.get()
        self.Convert_To_Int = float(self.What_User_Wrote)
        self.param_value = self.Convert_To_Int
    def get_coeffs(self):
        a = self.message
     
        return float(self.param_value)

class InputParameterProportionnal(tk.Frame):
    def __init__(self,  fenetre, name, **kwargs):
        tk.Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.fenetre = fenetre
        self.pack(fill=tk.BOTH)
      
        
        # proportionnal coeff :
        self.caption = tk.Label(self, text=name)
        self.caption.pack()

        
        self.message = tk.Label(self, text="0")
        self.message.pack()
        
        self.bouton_cliquer = tk.Button(self, text="valider", command=self.cliquer)
        self.bouton_cliquer.pack(side="right")
         
        self.var_texte = tk.DoubleVar(value=0)
        
        self.texte_utilisateur = tk.Entry(self, textvariable=self.var_texte, width=40)
        self.texte_utilisateur.pack()
        
        self.var_case = tk.IntVar()
        self.case = tk.Checkbutton(self, text="ACTIVER", variable=self.var_case)
        self.case.pack()
        
        self.param_value=0
        
    def cliquer(self):
        self.message["text"] = self.texte_utilisateur.get()
        self.What_User_Wrote = self.texte_utilisateur.get()
        self.Convert_To_Int = float(self.What_User_Wrote)
        self.param_value = self.Convert_To_Int
        self.fenetre.fenetre.application.regulation_fonction.coeff_proportionnel = self.param_value


class InputParameterIntergral(InputParameter):
    def __init__(self,  fenetre, name,  **kwargs):
        tk.Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.fenetre = fenetre
        self.pack(fill=tk.BOTH)
      
        
        # proportionnal coeff :
        self.caption = tk.Label(self, text=name)
        self.caption.pack()

        
        self.message = tk.Label(self, text="0")
        self.message.pack()
        
        self.bouton_cliquer = tk.Button(self, text="valider", command=self.cliquer)
        self.bouton_cliquer.pack(side="right")
         
        self.var_texte = tk.DoubleVar(value=0)
        
        self.texte_utilisateur = tk.Entry(self, textvariable=self.var_texte, width=40)
        self.texte_utilisateur.pack()
        
        self.var_case = tk.IntVar()
        self.case = tk.Checkbutton(self, text="ACTIVER", variable=self.var_case)
        self.case.pack()
        
        self.param_value=0
        
        
        
    def cliquer(self):
        self.message["text"] = self.texte_utilisateur.get()
        self.What_User_Wrote = self.texte_utilisateur.get()
        self.Convert_To_Int = float(self.What_User_Wrote)
        self.param_value = self.Convert_To_Int
        self.fenetre.fenetre.application.regulation_fonction.coeff_intergral = self.param_value

        
class InputParameterDerive(InputParameter):
    def __init__(self,  fenetre, name,  **kwargs):
        tk.Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.fenetre = fenetre
        self.pack(fill=tk.BOTH)
      
        
        # proportionnal coeff :
        self.caption = tk.Label(self, text=name)
        self.caption.pack()

        
        self.message = tk.Label(self, text="0")
        self.message.pack()
        
        self.bouton_cliquer = tk.Button(self, text="valider", command=self.cliquer)
        self.bouton_cliquer.pack(side="right")
         
        self.var_texte = tk.DoubleVar(value=0)
        
        self.texte_utilisateur = tk.Entry(self, textvariable=self.var_texte, width=40)
        self.texte_utilisateur.pack()
        
        self.var_case = tk.IntVar()
        self.case = tk.Checkbutton(self, text="ACTIVER", variable=self.var_case)
        self.case.pack()
        
        self.param_value=0
        
    def cliquer(self):
        self.message["text"] = self.texte_utilisateur.get()
        self.What_User_Wrote = self.texte_utilisateur.get()
        self.Convert_To_Int = float(self.What_User_Wrote)
        self.param_value = self.Convert_To_Int
        self.fenetre.fenetre.application.regulation_fonction.coeff_derive = self.param_value
        
        
        
class InputLayout(tk.Toplevel):
    
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""
    
    def __init__(self, fenetre, **kwargs):
        tk.Toplevel.__init__(self, fenetre, width=768, height=576, **kwargs)
        
        #self.pack(fill=tk.BOTH) #self.create_window()
        self.fenetre = fenetre
  
        #self.proportionnal = InputParameter(self,"proportionnal")
        self.integral = InputParameter(self,"integral")
        self.derive = InputParameter(self,"derive")


        
        self.proportionnal = InputParameterProportionnal(self,"proportionnal")
        InputParameterIntergral(self,"integral")
        InputParameterDerive(self,"derive")
 

       
        self.bouton = tk.Button(self, text="parameter",command=self.get_coeffs)
        self.bouton.pack()       
        self.bouton_fermer = tk.Button(self, text='fermer', command=self.destroy).pack(padx=10, pady=10)
        
    
    def get_coeffs(self):
        
        
        self.proportionnal_value = self.proportionnal.get_coeffs()
        self.integral_value = self.integral.get_coeffs() 
        self.derive_value = self.derive.get_coeffs()
     
     
        return self.proportionnal_value, self.integral_value, self.derive_value
    
    def on_press(self, event):
        pass
    
    
    
    
    
    
    
    
class Fenetre(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Fenêtre principale')
        self.geometry('300x100')
        self.proportionnal = InputParameter(self,"proportionnal")
        self.popup = InputLayout()

class IndicatorsLayout(tk.Frame):
         
    def __init__(self, fenetre,  **kwargs):
        tk.Frame.__init__(self, fenetre, width=68, height=576,  **kwargs)
        #self.pack(fill=tk.BOTH)        #self.create_window()
        self.fenetre = fenetre
        tk.Label(self, text="order_temperature en cours (°C)").place(relx=0.02, rely=0.04, relwidth=0.96, relheight=0.06 )
        self.input_temperatures_indicator = tk.Label(self, text="0")
        self.input_temperatures_indicator.place(relx=0.02, rely=0.11, relwidth=0.96, relheight=0.05)
        
       
        self.temperature_caption = tk.Label(self, text="température réeelle (°C)").place(relx=0.02, rely=0.20, relwidth=0.96, relheight=0.06 )
        self.real_temperature  = tk.Label(self, text=0)
        self.real_temperature.place(relx=0.02, rely=0.27, relwidth=0.96, relheight=0.05 )
        
        self.temperature_caption = tk.Label(self, text="vitesse de chauffe(°C/min)").place(relx=0.02, rely=0.36, relwidth=0.96, relheight=0.06 )
        tk.Label(self, text=0).place(relx=0.02, rely=0.43, relwidth=0.96, relheight=0.05 )
        
        
        self.time_caption = tk.Label(self, text="temps global (s)").place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.06 )
        self.time = tk.Label(self, text="temps global (s)")
        self.time.place(relx=0.02, rely=0.59, relwidth=0.96, relheight=0.05)
        
        self.temperature_caption = tk.Label(self, text="temps palier (s)").place(relx=0.02, rely=0.68, relwidth=0.96, relheight=0.06 )
        self.time_plateau = tk.Label(self, text="temps global (s)")
        self.time_plateau.place(relx=0.02, rely=0.75, relwidth=0.96, relheight=0.05 )
        
        self.laser_caption = tk.Label(self, text="fréquence laser (hz)").place(relx=0.02, rely=0.84, relwidth=0.96, relheight=0.06 )
        self.laser = tk.Label(self, text="déconnceté")
        self.laser.place(relx=0.02, rely=0.91, relwidth=0.96, relheight=0.05 )
        
    def update(self):
            
        self.input_temperatures_indicator["text"] = self.fenetre.input_temperatures.order_temperature_plot
        self.real_temperature["text"] = self.fenetre.application.real_temperature
        self.time["text"] = self.fenetre.application.regulation_fonction.time
        self.time_plateau["text"] = self.fenetre.application.regulation_fonction.timer     
            #self.fenetre.input_temperatures.temperature_order_temperature.place(relx=0.6, rely=0.3, relwidth=0.02, relheight=0.6 )
            #
            #self.fenetre.liveplotting.time
 
