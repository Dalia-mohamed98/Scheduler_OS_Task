#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 18:17:05 2018

@author: Haneen
"""
import queue
from scheduler import Scheduler
from plotting import pltng

class RR(Scheduler):
    
    
    def __init__(self, context_switch_time, quantum):
        
        super().__init__(context_switch_time, quantum)
        
        self.__queue = queue.Queue()
        self.__process = None
        self.plotting = pltng()
        
        self.__run_qntm = quantum
        return
    
    def runProcess(self):
        
        #finished quantum, switch context, enqueue process, restart quantum and return
        if self.__run_qntm == 0:
            
            if self.__queue.qsize() != 0:
                self.__queue.put(self.__process)
                self.switchContext()
            else:
                self.restartQntm()
            
            return 0
        
        #new quantum, new process
        if self.__process == None:

            if self.__queue.qsize() != 0:
                self.__process = self.__queue.get()
                
            else:
                #return "Queue Empty"
                self.plotting.addPoint(0)
                return 0
        
        #decrement quantum, run process
        self.__run_qntm = self.__run_qntm - 1
        self.__process.run(1)
        self.plotting.addPoint(self.__process.getNumber())
        print(self.__process.getNumber(), self.__process.getRemaining(), ' ', self.__process.getBurst())
        
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
        self.restartQntm()
        return
    
    def restartQntm(self):
        self.__run_qntm = super().getQntm()
        return
    
    def plot(self):
        
        self.plotting.plot()
        return