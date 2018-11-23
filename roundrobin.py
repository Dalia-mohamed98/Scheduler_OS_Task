#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 18:17:05 2018

@author: Haneen
"""

from scheduler import Scheduler
from circularqueue import CircularQueue
import plotting

class RoundRobin(Scheduler):
    
    __queue = CircularQueue()
    __process = None
    
    def __init__(self, context_switch_time, quantum):
        
        super().__init__(context_switch_time, quantum)
        
        self.__run_qntm = quantum
        return
    
    def runProcess(self):
        
        #finished quantum, switch context, enqueue process, restart quantum and return
        if self.__run_qntm == 0:
            
            if self.__queue.size() != 0:
                self.__queue.enqueue(self.__process)
                self.switchContext()
            else:
                self.restartQntm()
            
            return 0
        
        #new quantum, new process
        if self.__process == None:

            if self.__queue.size() != 0:
                self.__process = self.__queue.dequeue()
                
            else:
                #return "Queue Empty"
                plotting.addPoint(0)
                return 0
        
        #decrement quantum, run process
        self.__run_qntm = self.__run_qntm - 1
        self.__process.run(1)
        plotting.addPoint(self.__process.getNumber())
        print(self.__process.getNumber(), self.__process.getRemaining(), ' ', self.__process.getBurst())
        
        for i in range(self.__queue.size()):
            pro = self.__queue.dequeue()
            pro.wait(1)
            self.__queue.enqueue(pro)
            
        if self.__process.getRemaining() <= 0:
            self.switchContext()
            return 1
        
        return 0
    
    def addProcess(self, process):
        self.__queue.enqueue(process)
        return
    
    def switchContext(self):
        
        #Add context Switch Handeling
        for i in range(super().getCST()):
            plotting.addPoint(0)
            
        self.__process = None
        self.restartQntm()
        return
    
    def restartQntm(self):
        self.__run_qntm = super().getQntm()
        return