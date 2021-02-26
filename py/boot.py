# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

# import os
# files=os.listdir()
# if len(files)>=2:
#     print('The device have %d files'%len(files))
#     for i in range(len(files)):
#         if files[i]!='boot.py':
#             print('file name:',files[i])
#             exec(open(files[i]).read(),globals())
#             
# else:
#     print("MicroPython has no files!")

#import time
from time import sleep_ms
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
# import esp
# esp.osdebug(None)
import gc
gc.collect()

ssid = 'check .env settings'
password = 'check .env settings'
mqtt_server = '192.168.0.178'
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.144'
client_id = ubinascii.hexlify(machine.unique_id())
print("id van de client " + str(client_id))

last_message = 0
message_interval = 5
counter = 0

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
print("Connecting the station")

attempt = 0

# while station.isconnected() == False or attempt < 10:
#     attempt = attempt + 1
#     pass

if station.isconnected():
    print("Connection successful")
    print(station.ifconfig())
else:
    print("Could not establish connection")
    
print("starting main.py")
exec(open("main.py").read(),globals())
