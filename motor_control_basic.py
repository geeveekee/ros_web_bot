import RPi.GPIO as gpio
from time import sleep

in1 = 
in2 = 
en = 
_dir = 1

gpio.setmode(gpio.BOARD)
gpio.setup(in1, gpio.OUT)
gpio.setup(in2, gpio.OUT)
gpio.setup(en, gpio.OUT)

gpio.output(in1, gpio.LOW)
gpio.output(in2, gpio.LOW)

p=gpio.PWM(en, 1000)    #pin no., signal time

p.start(25) #duty cycle
print("""r-run : s-stop : f-forward : b-backward : l-low : 
m-medium : h-hihg : e-exit""")

def set_motor_state(sig1, sig2):
    gpio.output(in1, sig1)
    gpio.output(in2, sig2)


while True:
    x=raw_input()

    if x=='r':
        #run
        if(_dir==1):
            set_motor_state(0, 1)
            print("forward")
            x='z'
        else:
            set_motor_state(1, 0)
            print("backwad")
            x='z'

    elif x=='s':
        #stop
        set_motor_state(0, 0)
        x='z'

    elif x=='f':
        #forward
        set_motor_state(1, 0)
        x='z'
    
    elif x=='b':
        #backward
        set_motor_state(0, 1)
        _dir=0
        x='z'
        
    elif x=='l'
        #low
        p.ChangeDutyCycle(25)
        x='z'

    elif x=='m':
        #medium
        p.ChangeDutyCycle(75)
        x='z'
    
    elif x=='e':
        gpio.cleanup()
        break

    else:
        print("Please enter valid data: ")