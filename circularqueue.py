#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 19:00:57 2018

@author: Haneen
"""

class CircularQueue:
    
    def __init__(self):
        
        self.queue = list()
        self.head = 0
        self.tail = 0
        self.max_size = 1000
        return
    
    
    def size(self):
         
        if self.tail >= self.head:
             return (self.tail - self.head)
        
        return (self.max_size - (self.head - self.tail))
    
    
    def enqueue(self, data):
        
        if self.size() == self.max_size - 1:
            return ("Queue Full!")
        
        self.queue.append(data)
        self.tail = (self.tail + 1) % self.max_size
        return True
    
    
    def dequeue(self):
        
        if self.size() == 0:
            return ("Queue Empty!") 
        
        data = self.queue[self.head]
        self.head = (self.head + 1) % self.max_size
        return data