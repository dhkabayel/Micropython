
import time
from machine import Pin
import machine

adc = machine.ADC(machine.Pin(34))
list = []


while True:
    veri = adc.read()
    adc.atten(adc.ATTN_11DB)
    time.sleep(.5)
    #print(veri)
    ekle = list.append(veri)
    time.sleep(.5)
    print(list)
    if len(list) == 5:
        topla = int(sum(list)) / len(list)
        print(topla)
        list[:] = []
