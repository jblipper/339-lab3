# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 15:47:01 2023

@author: Bhuvan





"""


import serial
import time as t
import numpy as np
import matplotlib.pyplot as plt


arraySize=250
serialPort=serial.Serial()
serialPort.baudrate=9600
serialPort.port="COM3"

print(serialPort)

deltaV = []
V1 = []
V2 = []

for value in range(0, 255):
    print("Value is:", value)
    data1=[]
    data2=[]
    serialPort.open()
    dataRead=False
    while (dataRead==False):
        serialPort.write(bytes([value]))
        t.sleep(0.1)
        inByte = serialPort.in_waiting
        print(inByte)
    #This loop reads in data from the array until byteCount reaches the array size (arraySize)
        byteCount=0
        while ((inByte>0)&(byteCount<arraySize)):
    
            dataByte=serialPort.read()
            byteCount=byteCount+1
            data1.append(ord(dataByte))
            dataByte=serialPort.read()
            data2.append(ord(dataByte))
        print("Data 2 is:", data2)
        
        deltaV.append(np.nanmean(data1)/255*5 - np.nanmean(data2)/255*5 )
        V1.append(np.nanmean(data1)/255*5)
        V2.append(np.nanmean(data2)/255*5)
        
        if (byteCount==arraySize):
            dataRead=True
    serialPort.close()


deltaV = np.array(deltaV)
I = deltaV/0.995
print("I is", I)
print("V2 is:", V2)
#Plot your analog output!
f1=plt.figure()
#plt.plot(deltaV, I, ".")
plt.plot(V2,I,".")
V2 = np.array(V2)
V2_clean = V2[np.isfinite(V2)]
I_clean = I[np.isfinite(np.array(I))]

np.savetxt('blue1_run4.csv'
           , np.concatenate((V2_clean[:, np.newaxis], I_clean[:, np.newaxis]), axis=1), delimiter = ",")