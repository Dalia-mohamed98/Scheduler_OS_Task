# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 09:49:36 2018

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
    
    def runProcess(self):
        if self.__process == None:
            if self.__queue.size() != 0:
                self.__process = self.__queue.dequeue()
                #print('g', self.__process.getNumber())
            else:
                #return "Queue Empty
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
    
    def addProcess(self, process):
        self.__queue.enqueue(process)
        print(1,process.getNumber())

        #hna hasort  lqueue descindingly according to priority
        self.sort()
        return
    
    def switchContext(self):
        for i in range(super().getCST()):
            plotting.addPoint(0)
            #TODO add wait
        #print(2,self.__process.getNumber())
        self.__process = None
        return

    def sort(self):
    
        processes = list()
        
        size = self.__queue.size()
        #print(size)
        
        for i in range(size):
            processes.append(self.__queue.dequeue())
            print(processes[i].getNumber())
                
        processes = processes[0].sortList(processes, 1,False)

        processes = processes[0].sortList(processes, 3,True)
        
        for i in range(len(processes)): 
            print(processes[i].getNumber())
        
        for i in range(len(processes)):
            self.__queue.enqueue(processes[i])
            
        return
         
