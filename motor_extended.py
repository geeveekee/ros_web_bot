import RPi.GPIO as io 
import time 

class Motor:
    def __init__(self):
        print("Initializing")
        self.en1 = 12
        self.en2 = 32

        self.l1 = 37
        self.r1 = 38

        self.r1 = 35
        self.r2 = 36

        io.setmode(io.BOARD)
        io.setup(self.en1, io.OUT)
        io.setup(self.l1, io.OUT)
        io.setup(self.r1, io.OUT)

        io.setup(self.en2, io.OUT)
        io.setup(self.l2, io.OUT)
        io.setup(self.r2, io.OUT)

        self.p1 = io.PWM(self.en1, 100)
        self.p2 = io.PWM(self.en2, 100)

    def free_run(self):
        print("free run")
        #runs it for 3 seconds slow and then 3 seconds fast
        self.p1.start(20)
        self.p2.start(20)

        self.gpio.output(self.en1, 1)
        self.gpio.output(self.r1, 1)
        self.gpio.output(self.l1, 0)

        self.gpio.output(self.en2, 1)
        self.gpio.output(self.r2, 1)
        self.gpio.output(self.l2, 0)

        time.sleep(3)

        self.p1.ChangeDutyCycle(100)
        self.p2.ChangeDutyCycle(100)
        self.gpio.output(self.en1, 1)
        self.gpio.output(self.r1, 1)
        self.gpio.output(self.l1, 0)

        self.gpio.output(self.en2, 1)
        self.gpio.output(self.r2, 1)
        self.gpio.output(self.l2, 0)

        time.sleep(3)

        self.p1.stop()
        self.p2.stop()

    def turn_right_left_speed(self, speed, right, left):
        print(f"turnning with speed: {speed}, {right}, {left}")
        #turn right slowly or fast
        if right:
            self.p1.start(speed)
            self.gpio.output(self.en1, 1)
        else:
            self.p2.start(speed)
            self.gpio.output(self.en2, 1)

        
        self.gpio.output(self.r1, right)
        self.gpio.output(self.l1, 0)

        
        self.gpio.output(self.r2, left)
        self.gpio.output(self.l2, 0)

        time.sleep(2)


    def move_forw_backw_speed(self, forw, backw, speed):
        print(f"turnning with speed: {forw}, {backw}, {speed}")
        self.p1.start(speed)
        self.p2.start(speed)

        self.gpio.output(self.en1, 1)
        self.gpio.output(self.r1, forw)
        self.gpio.output(self.l1, backw)

        self.gpio.output(self.en2, 1)
        self.gpio.output(self.l2, backw)
        self.gpio.output(self.r2, forw)

        time.sleep(2)right

    def move_forw_speed_left_right(self, right, left): 
        print(f"turnning with speed: {right}, {left}")
        self.gpio.output(self.en1, 1)
        self.gpio.output(self.en2, 1)

        if right:
            self.p1.start(50)
            self.p2.start(30)

        elif left:
            self.p1.start(30)
            self.p2.start(50)

        self.gpio.output(self.r1, right)
        self.gpio.output(self.l1, left)

        self.gpio.output(self.r2, right)
        self.gpio.output(self.l2, left)

        time.sleep(2)
    
    def move_backw_speed_left_right(self, right, left): 
        print(f"turnning with speed: {right}, {left}")
        self.gpio.output(self.en1, 1)
        self.gpio.output(self.en2, 1)

        if right:
            self.p1.start(50)
            self.p2.start(30)

        elif left:
            self.p1.start(30)
            self.p2.start(50)

        self.gpio.output(self.r1, left)
        self.gpio.output(self.l1, right)

        self.gpio.output(self.r2, left)
        self.gpio.output(self.l2, right)

        time.sleep(2)


    
