#!/usr/bin/python2

import time
import serial
import crcmod

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )
counter=0

frame = bytearray([0x02,0x04,0x01,0xE9,0x76,0x03])
print frame[0]
ser.write(frame)

frameout = bytearray()

x=ser.read(1)
while len(x) != 0:
    frameout.append(x[0])
    x=ser.read(1)

for index in range(len(frameout)):
    print hex(frameout[index])
