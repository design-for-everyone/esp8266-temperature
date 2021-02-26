# testing the temperature sensor: not used in final application
from machine import Pin
from time import sleep_ms
import dht 

led = Pin(2,Pin.OUT)
print(led)
sensor = dht.DHT11(Pin(14))
print(sensor)
is_looping = True
counter = 1;
# 
print("ready to start measuring")
# 
while is_looping:
    print("in the loop")
    counter = counter + 1
    if counter == 10:
        is_looping = False
    try:
        led.value(1)
        print("ready to measure")
        sleep_ms(1500)
        sensor.measure()
        led.value(0)

        print("measured")
        temp = sensor.temperature()
        hum = sensor.humidity()
        print("Temperature : " + str(temp) + " - Humidity: " + str(hum))
    except OSError as e:
        print('Failed to read sensor.')

print("End of the program")
