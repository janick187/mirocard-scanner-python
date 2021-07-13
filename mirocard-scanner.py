#!/usr/bin/python
from __future__ import print_function

from time import gmtime, strftime, sleep
from bluepy.btle import Scanner, DefaultDelegate, BTLEException
import struct
from base64 import b64decode,b64encode
import sys
import os.path


DEBUG = 0

class ScanDelegate(DefaultDelegate):

    def handleDiscovery(self, dev, isNewDev, isNewData):
        global DEBUG
        if(str(dev.addr).startswith("60:77:71")):
            print(strftime("%Y-%m-%d %H:%M:%S", gmtime()), dev.addr, dev.getScanData()[0][2])
            rawbytes = str(dev.getScanData()[0][2])

            msb3 = rawbytes[10:14]
            lsb3 = rawbytes[12:16]

            if DEBUG:
                print("MSB: {} \t LSB: {}".format(msb3,lsb3))

            humidity_raw = ((struct.unpack('>h', bytes.fromhex(msb3[2:]+msb3[0:2]))[0]&0x03FF)) 

            temperature_raw = (struct.unpack('>h', bytes.fromhex(lsb3[2:]+lsb3[0:2]))[0]&0xFFFC)>>2

            if DEBUG:
                print("Raw H: {} \t Raw T: {}".format(humidity_raw, temperature_raw))

            temperature = (-40.0 + temperature_raw / 100.0)
            humidity =  (humidity_raw / 10.0)
            
            f = open("values.txt", "w+")
            f.write("Temperature: {}".format(temperature))
            f.write("\nHumidity: {}".format(humidity))
            f.close()
            
            print("H: {:.3f}% \t T: {:.3f} C".format(humidity, temperature))

            sys.stdout.flush()

scanner = Scanner().withDelegate(ScanDelegate())

# listen for ADV_IND packages for 10s, then exit
scanner.scan(0, passive=True)