import gc
import webrepl
webrepl.start()
gc.collect()
import machine
import time

A = machine.Pin(4, machine.Pin.OUT)
B = machine.Pin(0, machine.Pin.OUT)
C = machine.Pin(2, machine.Pin.OUT)
D = machine.Pin(12, machine.Pin.OUT)
E = machine.Pin(13, machine.Pin.OUT)
F = machine.Pin(5, machine.Pin.OUT)
G = machine.Pin(14, machine.Pin.OUT)

S1 = machine.Pin(15, machine.Pin.OUT)
S2 = machine.Pin(3, machine.Pin.OUT)
S3 = machine.Pin(1, machine.Pin.OUT)

A.value(1)
B.value(1)
C.value(1)
D.value(1)
E.value(1)
F.value(1)
G.value(1)

S1.value(0)
S2.value(0)
S3.value(0)

def bir():
	A.value(1)
	B.value(0)
	C.value(0)
	D.value(1)
	E.value(1)
	F.value(1)
	G.value(1)

def iki():
	A.value(0)
	B.value(0)
	C.value(1)
	D.value(0)
	E.value(0)
	F.value(1)
	G.value(0)

def uc():
	A.value(0)
	B.value(0)
	C.value(0)
	D.value(0)
	E.value(1)
	F.value(1)
	G.value(0)

def dort():
	A.value(1)
	B.value(0)
	C.value(0)
	D.value(0)
	E.value(1)
	F.value(0)
	G.value(1)

def bes():
	A.value(0)
	B.value(1)
	C.value(0)
	D.value(0)
	E.value(1)
	F.value(0)
	G.value(0)

def alti():
	A.value(0)
	B.value(1)
	C.value(0)
	D.value(0)
	E.value(0)
	F.value(1)
	G.value(0)

def yedi():
	A.value(0)
	B.value(0)
	C.value(0)
	D.value(1)
	E.value(1)
	F.value(1)
	G.value(1)

def sekiz():
	A.value(0)
	B.value(0)
	C.value(0)
	D.value(0)
	E.value(0)
	F.value(0)
	G.value(0)

def dokuz():
	A.value(0)
	B.value(0)
	C.value(0)
	D.value(0)
	E.value(1)
	F.value(0)
	G.value(0)

def sifir():
	A.value(0)
	B.value(0)
	C.value(0)
	D.value(0)
	E.value(0)
	F.value(0)
	G.value(1)
	
while True:
	sifir()
	S1.value(1)
	S2.value(0)
	S3.value(0)
	time.sleep_ms(5)
	sekiz()
	S1.value(0)
	S2.value(1)
	S3.value(0)
	time.sleep_ms(5)
	bir()
	S1.value(0)
	S2.value(0)
	S3.value(1)
	time.sleep_ms(5)