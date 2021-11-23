import RPi.GPIO as gpio
from time import sleep

en = 
l = 
r = 

def init():
	gpio.setmode(gpio.BOARD)
	gpio.setup(en, gpio.OUT)
	gpio.setup(l, gpio.OUT)
	gpio.setup(r, gpio.OUT)
	gpio.output(en, 1)

def forward(tf):
	gpio.output(r, 1)
	gpio.output(l, 0)
	time.sleep(tf)

def reverse(tf):
	gpio.output(l, 1)
	gpio.output(r, 0)
	time.sleep(tf)

init()
forward(1)
reverse(1)



gpio.cleanup()
