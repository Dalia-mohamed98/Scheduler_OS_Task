#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 22:04:12 2018

@author: Haneen
"""

#from roundrobin import RoundRobin
import process as p
from FCFS import FCFS
from HPF import HPF
from shortestRTN import SRTN
from roundrobin import RR
#from plotting import plotting
#matplotlib.use("TkAgg")
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
#from matplotlib.figure import Figure



def program(file, alg, cst, qntm):
    
    #print(len(plotting.time), len(plotting.processes))
    print(file, alg, cst, qntm)
    inputFile = open(file, 'r')
    #pltr = plotting()
    #grph = plotting.Graph()
    #sch = roundrobin.RoundRobin(int(cst), int(qntm), grph)
    if alg == 'FCFS':
        sch = FCFS(int(cst), int(qntm))
        
    elif alg == 'HPF':
        sch = HPF(int(cst), int(qntm))
        
    elif alg == 'SRTN':
        sch = SRTN(int(cst), int(qntm))
        
    else:
        sch = RR(int(cst), int(qntm))
    
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
    
    #sch = roundrobin.RoundRobin(int(cst), int(qntm), grph)
    
    #plotting.defineY(total)
    #processes = roundrobin.Process.sortList(processes, roundrobin.Process.getArrival())
        
    for i in range(len(processes)):
        print(processes[i].getNumber())
    
    time = 0
    done = 0
    iteratable = 0
    
    while done < total:
        
        while iteratable != total and (processes[iteratable].getArrival() <= time):
            sch.addProcess(processes[iteratable])
            iteratable += 1
        
        done += sch.runProcess()
        time += 0.5
        #print(done, time)
        
    sch.plot()
    writeReport(processes)
    #temp = processes[0]
    #print(processes[0] == temp)
    
    return

def writeReport(processes):
    outputFile = open('report.txt', 'w')
    outputFile.write('Processes Matrix (WT, TA, WTA) \n \n')
    processes = processes[0].sortList(processes, 0)
    for i in range(len(processes)):
        
        outputFile.write('  '+str(processes[i].getNumber()) + ' ' + str(processes[i].getWait()) + ' ' + str(processes[i].getTurnaround())+' ' +str(processes[i].getWeightedTA()) +'\n'+'\n')
    
    outputFile.write('AvgTA= '+str(p.getAvgTA(processes))+'\nAvgWTA=  '+str( p.getAvgWTA(processes)))
    return
    
    