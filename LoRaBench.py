#!/usr/bin/python2

import crcmod
import binascii


def LoRaBenchEncodeFrame(input_byte_array):

    # http://crcmod.sourceforge.net/crcmod.html#crcmod.Crc
    # for the polynomial, the value is for the LoRaBench documentation
    # and equaly, why use 0x18408 and not 0x8408 (see http://stackoverflow.com/questions/24851027/how-to-calculate-ansi-crc16-polynomial-0x8005-in-python3)
    crc16 = crcmod.mkCrcFun(0x11021,rev=True,initCrc=0, xorOut=0x0000)

    #print ("initial array:" + str(input_byte_array))

    #insert len in first position
    input_byte_array.insert(0, len(input_byte_array)+3 )
    #print ("len and array:" + str(input_byte_array))

    # creating the string format expected by crc16
    inputstr = binascii.hexlify(bytearray(input_byte_array))
    #print inputstr

    # Computing CRC16
    crc = crc16(inputstr.decode("hex"))
    #print crc
    #print hex(crc)

    input_byte_array.append(crc & 0xFF)
    input_byte_array.append(crc >> 8)
    #print input_byte_array

    #STX
    input_byte_array.insert(0, 2 )
    #ETX
    input_byte_array.append(3)

    return input_byte_array
