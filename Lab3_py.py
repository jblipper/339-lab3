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
            print("Data byte =", dataByte)
            byteCount=byteCount+1
            data1.append(ord(dataByte))
            print("Data 1 is:", data1)
            dataByte=serialPort.read()
            data2.append(ord(dataByte))
            print("Data 2 is:", data2)
        if (byteCount==arraySize):
            dataRead=True
    #data1out=np.zeros(arraySize)
    #data2out=np.zeros(arraySize)
    #arrayIndex=range(arraySize)
    #for i in arrayIndex:
        #data1out[i]=ord(data1[i])
        #data2out[i]=ord(data2[i])
    deltaV.append(np.mean(data1)/255*5 - np.mean(data2)/255*5 )
    V1.append(np.mean(data1)/255*5)
    V2.append(np.mean(data2)/255*5)
    serialPort.close()

#Transform unicode encoding into integers
#for i in arrayIndex:
   #deltaVout[i]=ord(deltaV[i])
   #V2out[i]=ord(V2[i])

deltaV = np.array(deltaV)
I = deltaV/0.995
#Plot your analog output!
f1=plt.figure()
#plt.plot(deltaV, I, ".")
plt.plot(V2,I,".")



#np.savetxt('e7_p2_{}.csv'.format(str(value)), dataOut, delimiter = ",")