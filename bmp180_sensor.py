
from bmp180 import BMP180
import time
from machine import I2C, Pin # create an I2C bus object accordingly to the port you are using77

#bus = I2C(1, baudrate=100000)          
i2cbmp =  I2C(scl=Pin(22), sda=Pin(1), freq=400000)   # esp8266

bmp180 = BMP180(i2cbmp)
bmp180.oversample_sett = 2
bmp180.baseline = 101325

def bmpSensor():
    while True:
        temp = bmp180.temperature
        p = bmp180.pressure
        altitude = bmp180.altitude
        print(temp, p, altitude)
        time.sleep_ms(3500)

bmpSensor()
