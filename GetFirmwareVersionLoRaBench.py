#!/usr/bin/python2

import time
import serial
import crcmod
import LoRaBench
import numpy as np

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )
counter=0

#frame = bytearray([0x02,0x04,0x01,0xE9,0x76,0x03])
frametx = LoRaBench.LoRaBenchEncodeFrame([0x01])
print ("Sending frame: " + str(frametx))
ser.write(frametx)

framerx = bytearray()

x=ser.read(1)
while len(x) != 0:
    framerx.append(x[0])
    x=ser.read(1)

# can display the result to the same line
np.set_printoptions(formatter={'int':hex })
print np.array(framerx)
#print ("Received frame: " + str(framerx))

#for index in range(len(framerx)):
#    print hex(framerx[index])
