#!/usr/bin/python2

import time
#from smbus2 import SMBus # import library smbus2 compatible to use I2C
#bus = SMBus(1)

from smbus import SMBus # import library smbus2 compatible to use I2C
bus = SMBus(1)

I2CAdress = 0x40
TEMP = 0xE3
HUM = 0xE5
#data = []

bus.write_byte(I2CAdress, HUM)
#data = read_byte_data(I2CAdress,0xE3)
data = bus.read_i2c_block_data(I2CAdress,HUM)

#print data
# Convert the data
data[2] = data[2] | 0xFC

#temp = data[1] * 256 + data[2]
#cTemp = -46.85 + (175.72 * temp / 65535.0)

humidity = data[1] * 256 + data[2]
humidityPercent = -6 + (125 * humidity / 65535)

#humidity = 100 * (data[3] * 256 + data[4]) / 65535.0

# Output data to screen
#print "Temperature in Celsius is : %.2f C" %cTemp
print "Relative Humidity is : %.2f %%RH" %humidityPercent
