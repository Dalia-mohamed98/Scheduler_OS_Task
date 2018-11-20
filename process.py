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
    
    def __init__(self, data = None):
        
        self.__wait = 0
        self.__run = 0
        
        if data is None:
            self.__number = 0
            self.__arrival = 0
            self.__burst = 0
            self.__priority = 0
            return
        
        self.__number = data[0]
        self.__arrival = data[1]
        self.__burst = data[2]
        self.__priority = data[3]
        return
    
    def run(self, time):
        
        if time != 0:
            self.__run = self.__run + time
            return
        
        self.run = self.burst
        return
    
    def wait(self, time):
        self.__wait = self.__wait + time
        return
    
    def getNumber(self):
        return self.__number
    
    def getArrival(self):
        return self.__arrival
    
    def getBurst(self):
        return self.__burst
    
    def getPriority(self):
        return self.__priority
    
    def getWait(self):
        return self.__wait
    
    def getRun(self):
        return self.__run
    
    def getRemaining(self):
        return self.__burst - self.__run
    
    def getTurnaround(self):
        return self.__wait + self.__run
    
    def getWeightedTA(self):
        return (self.getTurnaround() / self.__run)
    
    def sortList(self, processes):
        return sorted(processes, key = lambda processes : processes.__arrival)