#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 21:24:43 2018

@author: Haneen
"""
import queue
from scheduler import Scheduler
from plotting import pltng

class SRTN(Scheduler):
    
    
    
    def __init__(self, context_switch_time, quantum):
        
        super().__init__(context_switch_time, quantum)
        self.__queue = queue.Queue()
        self.__process = None
        self.plotting = pltng()
        
        return
    
    def addProcess(self, process):
        
        self.__queue.put(process)
        
        temp = self.__process
        
        if self.__process != None:
            
            self.__queue.put(self.__process)
            self.__process = None
            
        self.sort()
        
        self.__process = self.__queue.get()
        guard = self.__process
        
        if temp != self.__process:
            self.switchContext()
            self.__process = guard
        
        return
    
    def switchContext(self):
        
        #Add context Switch Handeling
        for i in range(super().getCST()):
            self.plotting.addPoint(0)
            for j in range(self.__queue.qsize()):
                pro = self.__queue.get()
                pro.wait(1)
                self.__queue.put(pro)
                
        self.__process = None
        return
    
    def runProcess(self):
        
        if self.__process == None:
            
            if self.__queue.qsize() != 0:
                self.__process = self.__queue.get()
                
            else:
                #return "Queue Empty"
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
    
    def sort(self):
        
        processes = list()
        
        size = self.__queue.qsize()
        print(size)
        
        for i in range(size):
            processes.append(self.__queue.get())
            print(processes[i].getNumber())
            
        processes = processes[0].sortList(processes, 6)
        
        for i in range(len(processes)):
            print(processes[i].getNumber())
        
        for i in range(len(processes)):
            self.__queue.put(processes[i])
            
        return
    
    def plot(self):
        
        self.plotting.plot()
        return