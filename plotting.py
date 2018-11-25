#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 11:04:17 2018

@author: Haneen
"""

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

class pltng: 
    
    def __init__(self):
        self.__time = []
        self.__processes = []
   
    def addPoint(self, process):
        
        if len(self.__time)== 0:
            self.__time.append(0)
            
            
        else:
            self.__time.append(self.__time[-1]+1)
            
        self.__processes.append(process)
        return

    def plot(self):
        
        print(len(self.__time), len(self.__processes))
        plt.gcf().clear()
        print(len(self.__time), len(self.__processes))
        #self.__processes.append(0)
        y_pos = np.arange(len(self.__time))
        
        plt.bar(y_pos, self.__processes, width=1, align='center', alpha=1, color=['red', 'green'])
        plt.xticks(y_pos, self.__time)
        plt.ylabel('Processes')
        plt.xlabel('Time')
        plt.title('Scheduling')
    
        plt.show()
        return