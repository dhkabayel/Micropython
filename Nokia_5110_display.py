
import pcd8544
import framebuf
import utime
import machine
import _thread

from machine import Pin, SPI
from time import *


spi = SPI(1, baudrate=328125, bits=8, polarity=0, phase=1, sck=Pin(18), mosi=Pin(13))
spi.init()
cs = Pin(5, Pin.OUT)
dc = Pin(15, Pin.OUT)
rst = Pin(4, Pin.OUT)
# backlight on
bl = Pin(12, Pin.OUT, value=1) # off by default

lcd = pcd8544.PCD8544(spi, cs, dc, rst)
lcd.contrast(0x3c, pcd8544.BIAS_1_40, pcd8544.TEMP_COEFF_0)
lcd.reset()
lcd.init()
lcd.clear()


buffer = bytearray((lcd.height // 8) * lcd.width)
framebuf = framebuf.FrameBuffer1(buffer, lcd.width, lcd.height)

rtc = machine.RTC()
rtc.ntp_sync ('a.ntp.br')
rtc.init (rtc.now())

def watch():
    data = strftime('%d/%m/%y')
    relogio = strftime('%H:%M:%S')
    lcd.position(0, 0)
while True:
    framebuf.text(data, 10, 12, 1)
    framebuf.text(relogio,10,24,1)
    lcd.data(buffer)
    agora = strftime('%H:%M:%S')

if relogio != agora:
    relogio = agora
    framebuf.fill(0) # clear framebuffer
    utime.sleep(1)
    lcd.data(buffer)

_thread.start_new_thread ("clock",watch, ())
