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

def set_motor_control(choice):
    switch = {
        's': set_motor_control(0, 0),   #stop
        'f': set_motor_control(1, 0),   #forward
        'b': set_motor_control(0, 1),   #backward
        'l': p.ChangeDutyCycle(25),     #low
        'm': p.ChangeDutyCycle(75),     #medium
    }
    switch.get(choice, lamda: "Invalid")





while True:
    x=raw_input()

    if x=='r':
        #run
        if(_dir==1):
            set_motor_state(0, 1)
            #gpio.output(in1, gpio.LOW)
            #gpio.output(in2, gpio.HIGH)
            print("forward")
            x='z'
        else:
            set_motor_state(1, 0)
            #gpio.output(in1, gpio.HIGH)
            #gpio.output(in2, gpio.LOW)
            print("backwad")
            x='z'

    elif:
        

    #elif x=='s':
    #    #stop
    #    gpio.output(in1, gpio.LOW)
    #    gpio.output(in2, gpio.LOW)
    #    x='z'

    #elif x=='f':
    #    #forward
    #    gpio.output(in1, gpio.HIGH)
    #    gpio.output(in2, gpio.LOW)
    #    x='z'
    
    #elif x=='b':
    #    #backward
    #    gpio.output(in1, gpio.LOW)
    #    gpio.output(in2, gpio.HIGH)
    #    _dir=0
    #    x='z'

    #elif x=='l'
    #    #low
    #    p.ChangeDutyCycle(25)
    #    x='z'

    #elif x=='m':
    #    #medium
    #    p.ChangeDutyCycle(75)
    #    x='z'
    
    elif x=='e':
        gpio.cleanup()
        break

    else:
        print("Please enter valid data: ")