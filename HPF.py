# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 23:24:41 2018

@author: Mary
"""

import queue
from scheduler import Scheduler
from plotting import pltng

class HPF(Scheduler):
    
    def __init__(self, context_switch_time, quantum):
        
        super().__init__(context_switch_time, quantum)
        
        self.__queue = queue.Queue()
        self.__process = None
        self.plotting = pltng()
        
        return
    
    def runProcess(self):
        if self.__process == None:
            if self.__queue.qsize() != 0:
                self.__process = self.__queue.get()
                #print('g', self.__process.getNumber())
            else:
                #return "Queue Empty
                self.plotting.addPoint(0)
                return 0
            
        self.__process.run(1)
        self.plotting.addPoint(self.__process.getNumber())
        
        for i in range(self.__queue.qsize()):
            pro = self.__queue.get()
            pro.wait(1)
            self.__queue.put(pro)
            
        if self.__process.getRemaining() <= 0:
            self.switchContext()
            return 1  
        
        return 0
    
    def addProcess(self, process):
        self.__queue.put(process)
        print(1,process.getNumber())

        #hna hasort  lqueue descindingly according to priority
        self.sort()
        return
    
    def switchContext(self):
        for i in range(super().getCST()):
            self.plotting.addPoint(0)
                        
            for j in range(self.__queue.qsize()):
                pro = self.__queue.get()
                pro.wait(1)
                self.__queue.put(pro)
        self.__process = None
        return

    def sort(self):
    
        processes = list()
        
        size = self.__queue.qsize()
        
        for i in range(size):
            processes.append(self.__queue.get())
            print(processes[i].getNumber())
                
        processes = processes[0].sortList(processes, 1,False)

        processes = processes[0].sortList(processes, 3,True)
        
        for i in range(len(processes)): 
            print(processes[i].getNumber())
        
        for i in range(len(processes)):
            self.__queue.put(processes[i])
            
        return
        
    def plot(self):
        
        self.plotting.plot()
        return