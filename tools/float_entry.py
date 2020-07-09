#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 06:24:30 2020

@author: melinapannier
"""


import tkinter as tk
from tkinter import ttk

class NumEntry(ttk.Spinbox):
    def __init__(self, parent, **kwargs):
        self.var = tk.StringVar()
        ttk.Spinbox.__init__(self, parent, textvariable=self.var, **kwargs)
        self.old_value = ''
        self.var.trace('w', self.check)
        self.get, self.set = self.var.get, self.var.set

    def check(self, *args):
        if self.get().isdigit(): 
            # the current value is only digits; allow this
            self.old_value = self.get()
        else:
            # there's non-digit characters in the input; reject this 
            self.set(self.old_value)

# #demo:
# window = tk.Tk()
# From_entry=NumEntry(window, width=25)
# From_entry.grid(column=1,row=2,padx=5)
# window.mainloop()