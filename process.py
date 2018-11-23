#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 19:50:14 2018

@author: Haneen
"""

def getAvgTA(processes):
    
    sum = 0
    for i in range(len(processes)):
        sum += processes[i].getTurnaround()
    
    return (sum/len(processes))

def getAvgWTA(processes):
    
    sum = 0
    for i in range(len(processes)):
        sum += processes[i].getWeightedTA()
    
    return (sum/len(processes))

class Process:
    
    __number = 0
    __arrival = 1
    __burst = 2
    __priority = 3
    __wait = 4
    __run = 5
    __remaining = 6
    
    def __init__(self, data):
        
        self.__list = list()
        self.__list.append(data[0])
        self.__list.append(data[1])
        self.__list.append(data[2])
        self.__list.append(data[3])
        self.__list.append(0)
        self.__list.append(0)
        self.__list.append(data[2]) 
        return
        
    
    def run(self, time):
        self.__list[self.__run] += time
        self.__list[self.__remaining] = self.getRemaining()
        return
    
    def wait(self, time):
        self.__list[self.__wait] += time
        return
    
    def getNumber(self):
        return self.__list[self.__number]
    
    def getArrival(self):
        return self.__list[self.__arrival]
    
    def getBurst(self):
        return self.__list[self.__burst]
    
    def getPriority(self):
        return self.__list[self.__priority]
    
    def getWait(self):
        return self.__list[self.__wait]
    
    def getRun(self):
        return self.__list[self.__run]
    
    def getRemaining(self):
        return self.__list[self.__burst] - self.__list[self.__run]
    
    def getTurnaround(self):
        return self.__list[self.__wait] + self.__list[self.__burst]
    
    def getWeightedTA(self):
        return (self.getTurnaround() / self.__list[self.__burst])
    
    def sortList(self, processes, k):
        return sorted(processes, key = lambda processes : processes.__list[k])