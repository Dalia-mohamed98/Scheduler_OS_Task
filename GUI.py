#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 16:14:40 2018

@author: Haneen
"""

from tkinter import *
from module02 import program
#import matplotlib
#import numpy as np
#matplotlib.use("TkAgg")
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
#from matplotlib.figure import Figure
#import plotting as m_plt

'''class gui(Tk):
    
    def __init__(self):
        
        return
    
    def run(self):'''
root = Tk()
root.title("OS Scheduler")

#msg = Label(root, text = "Please Enter Req. Info.")

alg_l = Label(root, text = "Algorithm")

alg_t = StringVar(root)
choices = { 'FCFS','HPF','SRTN','RRobin'}
alg_t.set('FCFS') # set the default option
 
alg_popupMenu = OptionMenu(root, alg_t, *choices)

file_l = Label(root, text = "File")
file_t = StringVar()
file_e = Entry(root, textvariable = file_t)

cst_l = Label(root, text = "CSTime")
cst_t = StringVar()
cst_e = Entry(root, textvariable = cst_t)

qntm_l = Label(root, text = "Quantum")
qntm_t = StringVar()
qntm_e = Entry(root, textvariable = qntm_t)

#msg.grid(row = 0, columnspan = 2)

alg_l.grid(row = 1, sticky = E)
alg_popupMenu.grid(row = 1, column = 1, sticky = W)


file_l.grid(row = 2, sticky = E)
file_e.grid(row = 2, column = 1, sticky = W)


cst_l.grid(row = 3, sticky = E)
cst_e.grid(row = 3, column = 1, sticky = W)


qntm_l.grid(row = 4, sticky = E)
qntm_e.grid(row = 4, column = 1, sticky = W)

button = Button(root, text = "RUN", fg = "blue", command = lambda:program(file_t.get(), alg_t.get(), cst_t.get(), qntm_t.get()))
button.grid(row = 5, columnspan = 2)


root.mainloop()
        
''' f = Figure(figsize = (5, 5), dpi = 100)
        a = f.add_subplot(111)
        
        y_pos = np.arange(len(m_plt.time))
        
        a.bar(y_pos, m_plt.processes, width=1, align='center', alpha=1, color=['red', 'green'])
        #a.xticks(y_pos, m_plt.time)
        #a.ylabel('Processes')
        #a.xlabel('Time')
        #a.title('Scheduling')
        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().grid(expand = True)
        
        return
    
a = gui()
a.mainloop()'''