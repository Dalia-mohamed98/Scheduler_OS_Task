#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 18:13:54 2018

@author: Haneen
"""

#main class

class Scheduler:
    
    def __init__(self, context_switch_time, quantum):
        
        self.__cST = context_switch_time
        self.__qntm = quantum
        return
    
    def getCST(self):
        return self.__cST
    
    def getQntm(self):
        return self.__qntm
             
    def addProcess(self, process):
        return
    
    def removeProcess(self, process):
        return
        
    def runProcess(self):
        return
    
    def switchContext(self):
        return