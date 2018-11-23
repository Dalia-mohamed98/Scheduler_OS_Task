#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 21:24:43 2018

@author: Haneen
"""

from scheduler import Scheduler
from circularqueue import CircularQueue
import plotting
import process as p

class srtn(Scheduler):
    
    __queue = CircularQueue()
    __process = None
    
    def __init__(self, context_switch_time, quantum):
        
        super().__init__(context_switch_time, quantum)
        
        return
    
    def addProcess(self, process):
        
        self.__queue.enqueue(process)
        
        temp = self.__process
        
        if self.__process != None:
            
            self.__queue.enqueue(self.__process)
            self.__process = None
            
        self.sort()
        
        self.__process = self.__queue.dequeue()
        guard = self.__process
        
        if temp != self.__process:
            self.switchContext()
            self.__process = guard
        
        return
    
    def switchContext(self):
        
        #Add context Switch Handeling
        for i in range(super().getCST()):
            plotting.addPoint(0)
            for i in range(self.__queue.size()):
                pro = self.__queue.dequeue()
                pro.wait(1)
                self.__queue.enqueue(pro)
                
        self.__process = None
        return
    
    def runProcess(self):
        
        if self.__process == None:
            
            if self.__queue.size() != 0:
                self.__process = self.__queue.dequeue()
                
            else:
                #return "Queue Empty"
                plotting.addPoint(0)
                return 0
            
        self.__process.run(1)
        plotting.addPoint(self.__process.getNumber())
        
        for i in range(self.__queue.size()):
            pro = self.__queue.dequeue()
            pro.wait(1)
            self.__queue.enqueue(pro)
        
        if self.__process.getRemaining() <= 0:
            self.switchContext()
            return 1
        
        return 0
    
    def sort(self):
        
        processes = list()
        
        size = self.__queue.size()
        print(size)
        
        for i in range(size):
            processes.append(self.__queue.dequeue())
            print(processes[i].getNumber())
            
        processes = processes[0].sortList(processes, 6)
        
        for i in range(len(processes)):
            print(processes[i].getNumber())
        
        for i in range(len(processes)):
            self.__queue.enqueue(processes[i])
            
        return