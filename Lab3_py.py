# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 15:47:01 2023

@author: Bhuvan





"""


import serial
import time as t
import numpy as np
import matplotlib.pyplot as plt

#value=130

arraySize=250
serialPort=serial.Serial()
serialPort.baudrate=9600
serialPort.port="COM3"

print(serialPort)
serialPort.open()
dataRead=False
data1=[]
data2=[]
value = 0
while (dataRead==False and value < 256):
    serialPort.write(bytes([value]))
    t.sleep(0.1)
    inByte = serialPort.in_waiting
#This loop reads in data from the array until byteCount reaches the array size (arraySize)
    byteCount=0
    while ((inByte>0)&(byteCount<arraySize)):

        dataByte=serialPort.read()
        byteCount=byteCount+1
        data1=data1+[dataByte]
        #dataByte=serialPort.read()
        #data2=data2+[dataByte]
        value += 1
        print(value)
    if (byteCount==arraySize):
        dataRead=True
        
serialPort.close()
dataOut1=np.zeros(arraySize)
#dataOut2=np.zeros(arraySize)
arrayIndex=range(arraySize)
#Transform unicode encoding into integers
for i in arrayIndex:
    dataOut1[i]=ord(data1[i])
    #dataOut2[i]=ord(data2[i])

#I = (dataOut1 - dataOut2)/0.995
#Plot your analog output!
f1=plt.figure()
plt.plot(dataOut1)
#plt.plot(dataOut2)
plt.xlabel("LED Voltage(V)")
plt.ylabel("Current(mA)")

#np.savetxt('e7_p2_{}.csv'.format(str(value)), dataOut, delimiter = ",")