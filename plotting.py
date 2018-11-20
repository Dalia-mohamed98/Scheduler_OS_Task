#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 11:04:17 2018

@author: Haneen
"""

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

time = [0]
processes = []

'''def defineY(processes_num):
    for i in range(processes_num):'''
        

def addPoint(process):
    
    time.append(time[-1]+1)
    processes.append(process)
    
def plot():
    
    processes.append(0)
    y_pos = np.arange(len(time))
    
    plt.bar(y_pos, processes, width=1, align='center', alpha=1)
    plt.xticks(y_pos, time)
    plt.ylabel('Processes')
    plt.xlabel('Time')
    plt.title('Scheduling')
     
    plt.show()