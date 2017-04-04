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
#!/usr/bin/python2

from smbus import SMBus

# I2C address of SHT21 ( datasheet_Sensirion_Humidity_Sensors_SHT21_Datasheet_V4.pdf __page 7 __ paragraph 5.3  )
I2CAdress = 0x40

# command codes ( datasheet_Sensirion_Humidity_Sensors_SHT21_Datasheet_V4.pdf __page 8 __ Table 6 )
TEM = 0xE3
HUM = 0xE5

bus = SMBus(1)

# reading raw humidity registers
raw_humidity = bus.read_word_data(I2CAdress, HUM)
data_humidity = [
                    (raw_humidity & 0xFF),
                    ( (raw_humidity >> 8) & 0xFF ),
                    ( (raw_humidity >> 16) & 0xFF ),
                    ( (raw_humidity>>24) & 0xFF )
                ]
#print data_humidity

# reading raw temperature registers
raw_temperature = bus.read_word_data(I2CAdress, TEM)
data_temperature = [
                    (raw_temperature & 0xFF),
                    ( (raw_temperature >> 8) & 0xFF ),
                    ( (raw_temperature >> 16) & 0xFF ),
                    ( (raw_temperature>>24) & 0xFF )
                    ]

#print data_temperature

# compute actual temperature
#  recover temperature word from raw temperature registers ( datasheet_Sensirion_Humidity_Sensors_SHT21_Datasheet_V4.pdf __page 10 __ paragraph 6 )
temp = data_temperature[0] * 256 + ( data_temperature[1] & 0xFC )
#  apply conversion formula ( atasheet_Sensirion_Humidity_Sensors_SHT21_Datasheet_V4.pdf __page 10 __ paragraph 6.1)
cTemp = -46.85 + (175.72 * temp / 65535.0)

#compute actual humidity
#  recover humidity word from raw temperature registers ( datasheet_Sensirion_Humidity_Sensors_SHT21_Datasheet_V4.pdf __page 10 __ paragraph 6 )
humidity = data_humidity[0] * 256 + ( data_humidity[1] & 0xFC )
#  apply humidity formula (datasheet_Sensirion_Humidity_Sensors_SHT21_Datasheet_V4.pdf __page 10 __ paragraph 6.2 )
humidityPercent = -6 + (125 * humidity / 65535)

# Output data to screen
print "Temperature in Celsius is : %.2f C" %cTemp
print "Relative Humidity is : %.2f %%RH" %humidityPercent
