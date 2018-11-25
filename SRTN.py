# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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

###################################################################
outputFile = open('output1.txt', 'w')
outputFile.write(str(processNo) + '\n')

for i in range(processNo):
    
    outputFile.write(str(i+1) + ' ' + str(abs(round(np.random.normal(miu1, sigma1),2))) + ' ' + str(abs(round(np.random.normal(miu2, sigma2),2))) + ' ' + str(np.random.poisson(lamda)) + '\n')
    
outputFile.close()
###################################################################
#inputFile = open('output1.txt','r')
#lines = inputFile.read()

#processNo = int(lines[0])
with open('output1.txt','r') as inputFile:
    processNo= [int(x) for x in next(inputFile).split()] # read first line
 
    array = []
    for line in inputFile: # read rest of lines
        array.append([float(x) for x in line.split()])
    
    
# print(processNo)
#print(array)

arr=[]
for x in array: 
    arr.append([x[1],x[2],int(x[0])])
    #arr.append([x[2]])


#####################################################################
def count(arr,arriv):
    count=0
    for x in arr:
        for y in x:
            if(y==arriv):
                count+=1
    return count
#####################################################################
def check(remainT,runn,Id):  #check whick is min to run
    if(remainT != []):
        remainT.sort()
        r=0
        while(r< len(remainT)):
            if(remainT[r][0]>0):
                if(remainT[r][0]<runn):
                    runn=remainT[r][0]
                    Id=remainT[r][1]
                break
            else: r+=1
            
            
            
def Gap(start,runn,remainT,r,val): #fill gap
    start =round(start+val,2)
    remainT[r][0] = round(remainT[r][0]-val,2)
    runn = round(runn-val,2)
    
    
def remainT(arr,runn,id):
    arr.append([runn,id])
    
    
def executed(arr,arriv,runn,id):
    arr.append([arriv,runn,id])
#####################################################################
def SRTN2(arr,RemainT):
    
    execute=[]
    arriv=arr[0][0]
    start=arriv
    runn=arr[0][1]
    j=1
    i=0
    r=0
    while( i < len(arr) and j<len(arr) ):
        #print(i,j)
        if(start==arriv):#check if arrival time arrived
            
        #check if there is more than 1 arrives get min running time
        ###########################################################
#             if(count(arr,arriv)>1):
#                 Min=runn
#                 Id=arr[i][2]
#                 C=count(arr,arriv)
#                 for l in range(1,C): #cause sorted arr check from the first till count
#                     if(Min>arr[i+l][1]):
#                         remainT(RemainT,Min,Id)
#                         Min=arr[i+l][1]
#                         Id=arr[i+l][2]
#                     else:
#                         remainT(RemainT,arr[i+l][1],arr[i+l][2])

#                 runn=Min
#                 #remainT.remove([Min,Id])
#                 j+=C-1 #new arrival after equal arriv time
        ###########################################################
            Id=arr[i][2]
            #check(RemainT,runn,Id) #check whick is min to run
            
            execT=round(arr[j][0] - start,2)
            remain = round(runn - execT,2)
            if(remain>0): #No gap between arrivals but overlaps
                executed(execute,start,execT,Id) #execute the current one till next arrival
                if(remain>arr[j][1]): #check which will run next
                    if(Id==arr[i][2]):
                        remainT(RemainT,remain,round(Id,2)) #store current remain time
                    else:
                        RemainT[r][0]= round(RemainT[r][0]-execT,2)
                    runn = arr[j][1]
                    i=j
                else:
                    remainT(RemainT,arr[j][1],arr[j][2]) 
                    runn=remain
                start=round(start+execT,2)
                
            else: #there is a gap or without overlap
                executed(execute,start,runn,arr[i][2]) #total exec of current one and still gap
                start=round(start+runn,2)
                #runn=0
                if(remain<0):
                    check(RemainT,runn,Id) #put the min in remainT in runn
                else:
                    runn= arr[j][1]
                i=j
            
        
            
        else:
            if(start<arriv): #gap
                RemainT.sort() #get min remaining time
                remain*=-1 #execute till the new arrival arrived
                runn=remain
                
                while(runn>0 and r<len(RemainT)):
                    if(RemainT[r][0] - runn >0):
                        executed(execute,start,runn,RemainT[r][1]) # exec from remainT till the new arrival arrived
                        Gap(start,runn,RemainT,r,runn) #fill gap
                    else: 
                        executed(execute,start,RemainT[r][0],RemainT[r][1]) #total exec from remainT
                        Gap(start,runn,RemainT,r,RemainT[r][0]) #fill gap
                        r+=1
                runn = arr[j][1]
                #arriv = arr[j][0]
                #i=j
          
        arriv= arr[j][0]
        j+=1
        #else:
            #if(start>arriv):
            
    #if still be a val in runn finish it
    RemainT.sort()
    if(runn>0):
        executed(execute,start,runn,arr[i][2]) #total exec
        start= round(start+runn,2)
    #then go through remianT
    while(r<len(RemainT)):
        if(RemainT[r][0]>0):
            executed(execute,start,RemainT[r][0],RemainT[r][1])
            start=round(start+RemainT[r][0],2)
        r+=1
        
    return execute                   
##############################################################################
arr.sort()
print(arr)
RemainT=[]
final=SRTN2(arr,RemainT)
print(final,RemainT)


