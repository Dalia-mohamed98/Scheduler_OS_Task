#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 21:54:45 2018

@author: Haneen
"""
import numpy as np

'''Read File Section'''

inputFile = open('file01.txt','r')

lines = inputFile.readlines()

processNo = int(lines[0])

miu1, sigma1 = lines[1].split()
miu1 = float(miu1)
sigma1 = float(sigma1)

miu2, sigma2 = lines[2].split()
miu2 = float(miu2)
sigma2 = float(sigma2)

lamda = float(lines[3])

#print(type(processNo), type(miu1), sigma2, miu2, sigma2, lamda)'''

outputFile = open('output01.txt', 'w')
outputFile.write(str(processNo) + '\n')

for i in range(processNo):
    
    outputFile.write(str(i+1) + ' ' + str(np.random.normal(miu1, sigma1)) + ' ' + str(np.random.normal(miu2, sigma2)) + ' ' + str(np.random.poisson(lamda)) + '\n')
    
outputFile.close()