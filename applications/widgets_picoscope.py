# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 15:27:32 2020

@author: yannb
"""

import tkinter as tk
class ParametreTk(tk.Frame):
    def __init__(self,  fenetre, com_object, name, parametre_consigne, parametre_unite="", **kwargs):
        tk.Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.fenetre = fenetre
        self.pack(fill=tk.BOTH)
        self.com_object = com_object
        self.parametre_consigne = parametre_consigne
        self.parametre_unite = parametre_unite
        self.consigne_picoscope = " 0"
      
        
        # proportionnal coeff :
        
        self.caption = tk.Label(self, text=name)
        self.caption.pack()

        
        self.message = tk.Label(self, text="0")
        self.message.pack()
        
        self.bouton_cliquer = tk.Button(self, text="valider", command=self.cliquer)
        self.bouton_cliquer.pack(side="right")
         
        self.var_texte = tk.DoubleVar(value=0)
        
        self.texte_utilisateur =  tk.Spinbox(self, from_ = 0, to = 5000000, increment=0.1, textvariable=self.var_texte)
        self.texte_utilisateur.pack()
        
        self.curseur = tk.Scale(self, orient = "horizontal", from_=0, to=5000000, variable = self.var_texte, showvalue=0)
        self.curseur.pack()
        
        #option
        self.var_case = tk.IntVar()
        self.case = tk.Checkbutton(self, text="ACTIVER", variable=self.var_case)
        
        
        
        self.param_value=0
        self.connect( self.texte_utilisateur, '<Return>', self.cliquer)
        
       
        
    def cliquer(self, event=None):
        self.message["text"] = self.texte_utilisateur.get()
        self.What_User_Wrote = self.texte_utilisateur.get()
        self.Convert_To_Int = float(self.What_User_Wrote)
        self.param_value = self.Convert_To_Int
        #self.fenetre.application.regulation_fonction.coeff_proportionnel = self.param_value
        self.consigne_picoscope = self.parametre_consigne + " " + str(self.param_value) + self.parametre_unite
        self.fenetre.update()
    
        
    def connect(self, widget, signal, event) :
        widget.bind(signal, event)
class WidgetsOscilloscope(tk.Frame):
    def __init__(self,  fenetre, name, **kwargs):
        tk.Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.fenetre = fenetre
        # pour le futur, je devrais utiliser une app pour gérer tout ça
        self.application =fenetre
        self.pack(fill=tk.BOTH)
    
        self.reglage_amplitude = ParametreTk(self, self.application, "U/div", "CH1:SCALE", "mV/div")
        self.reglage_amplitude_offset = ParametreTk(self, self.application, "U/div offset", "TB:ScaleA?")
        self.reglage_amplitude.place(relx=0.02, rely=0.02, relwidth=0.48, relheight=0.3)
        self.reglage_amplitude_offset.place(relx=0.52, rely=0.02, relwidth=0.48, relheight=0.3)
        
        self.reglage_temps_unite = ParametreTk(self, self.application, "s/div", "TB:ScaleA?", "n")
        self.reglage_temps_unite_offset  = ParametreTk(self, self.application, "s/div_offset", "TB:ScaleA?")
        self.reglage_temps_unite.place(relx=0.02, rely=0.25, relwidth=0.48, relheight=0.3)
        self.reglage_temps_unite_offset.place(relx=0.52, rely=0.25, relwidth=0.48, relheight=0.3)
    def update(self):
        self.fenetre.update()

