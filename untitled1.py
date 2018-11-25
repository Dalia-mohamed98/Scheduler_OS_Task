# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 14:34:35 2018

@author: Mary
"""

from scheduler import Scheduler
from circularqueue import CircularQueue
import plotting


class HPF(Scheduler):
    
    __queue = CircularQueue()
    __process = None
    
    def __init__(self, context_switch_time, quantum):
        
        super().__init__(context_switch_time, quantum)
        return
    
    def addProcess(self, process):
        
        self.__queue.enqueue(process)
        self.sort()
        
        return
    
    def switchContext(self):
        
        for i in range(super().getCST()):
            plotting.addPoint(0)
            for j in range(self.__queue.size()):
                pro = self.__queue.dequeue()
                pro.wait(1)
                self.__queue.enqueue(pro)
                
        print(self.__process.getNumber(), self.__process.getBurst(), self.__process.getRun())
        self.__process = None
        return
    
    def runProcess(self):
        
        if self.__process == None:
            if self.__queue.size() != 0:
                self.__process = self.__queue.dequeue()
                print(self.__process.getNumber(), self.__process.getBurst(), self.__process.getRun())
                
            else:
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
        
        while(self.__queue.size() != 0):
            processes.append(self.__queue.dequeue())
            
        processes = processes[0].sortList(processes, 1)
        processes = processes[0].sortList(processes, 3, True)
        self.__queue = CircularQueue()
        
        for i in range(len(processes)):
            print(processes[i].getNumber(), processes[i].getBurst(), processes[i].getRun())
        
        for i in range(len(processes)):
            self.__queue.enqueue(processes[i])
            
        return