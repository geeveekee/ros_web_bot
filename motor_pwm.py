import RPi.GPIO as gpio
import time

en = 12
r = 37
l = 38

en2 = 32
r2 = 35
l2 = 36

def init():
	gpio.setmode(gpio.BOARD)
	gpio.setup(en, 1)
	gpio.setup(r, 1)
	gpio.setup(l, 1)
	
	gpio.setup(en2, 1)
	gpio.setup(r2, 1)
	gpio.setup(l2, 1)
	p = gpio.PWM(en, 100)
	p2 = gpio.PWM(en2, 100)

def run():
	
	p = gpio.PWM(en, 100)
	p2 = gpio.PWM(en2, 100)
	p.start(20)
	p2.start(20)
	gpio.output(en, 1)
	gpio.output(r, 1)
	gpio.output(l, 0)
	
	gpio.output(en2, 1)
	gpio.output(r2, 1)
	gpio.output(l2, 0)
	time.sleep(3)

	p.ChangeDutyCycle(100)
	p2.ChangeDutyCycle(100)
	gpio.output(en, 1)
	gpio.output(r, 1)
	gpio.output(l, 0)
	
	gpio.output(en2, 1)
	gpio.output(r2, 1)
	gpio.output(l2, 0)
	time.sleep(3)
	
	gpio.output(r, 0)
	p.stop()
	p2.stop()

init()
run()

gpio.cleanup()
