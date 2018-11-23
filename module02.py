#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 22:04:12 2018

@author: Haneen
"""

#from roundrobin import RoundRobin
import roundrobin
import plotting
import process as p
import shortestRTN

inputFile = open('output01.txt','r')

lines = inputFile.readlines()
processes = list()
data = [i for i in range(4)]

total = int(lines[0])

for i in range(1, len(lines)):
    
    data[0], data[1], data[2], data[3] = lines[i].split()
    data[0] = int(data[0])
    data[1] = round(float(data[1]), 4)
    data[2] = round(float(data[2]), 4)
    data[3] = round(float(data[3]), 4)
    
    processes.append(p.Process(data))
    
processes = processes[0].sortList(processes, 1)

#sch = roundrobin.RoundRobin(1, 6)
sch = shortestRTN.srtn(1, 6)
#plotting.defineY(total)
#processes = roundrobin.Process.sortList(processes, roundrobin.Process.getArrival())
    
for i in range(len(processes)):
    
    print(processes[i].getArrival())
    
#print(processes[0].getNumber())

time = 0
done = 0
iteratable = 0

while done < total:
    
    while iteratable != total and (processes[iteratable].getArrival() <= time):
        sch.addProcess(processes[iteratable])
        iteratable += 1
    
    done += sch.runProcess()
    time += 1
    print(done, time)
    
plotting.plot()
print(p.getAvgTA(processes), p.getAvgWTA(processes))