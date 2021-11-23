import RPi.GPIO as gpio
import time

en = 
r = 
l = 

def init():
	gpio.setmode(gpio.BOARD)
	gpio.setup(en, 1)
	gpio.setup(r, 1)
	gpio.setup(l, 1)
	p = gpio.PWM(16, 100)

def run():
	p.start(20)
	gpio.output(en, 1)
	gpio.output(r, 1)
	gpio.output(l, 0)
	time.sleep(3)

	p.ChangeDutyCycle(100)
	gpio.output(en, 1)
	gpio.output(r, 1)
	gpio.output(l, 0)
	time.sleep(3)
	
	gpio.output(r, 0)
	p.stop()

init()
run()

gpio.cleanup()
