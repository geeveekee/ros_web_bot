import RPi.GPIO as gpio 
import time 

class Motor():
    def __init__(self):
        print("Initializing")
        self.en1 = 12
        self.en2 = 32

        self.l1 = 37
        self.r1 = 38

        self.l2 = 35
        self.r2 = 36

        gpio.setmode(gpio.BOARD)
        gpio.setup(self.en1, gpio.OUT)
        gpio.setup(self.l1, gpio.OUT)
        gpio.setup(self.r1, gpio.OUT)

        gpio.setup(self.en2, gpio.OUT)
        gpio.setup(self.l2, gpio.OUT)
        gpio.setup(self.r2, gpio.OUT)

        self.p1 = gpio.PWM(self.en1, 100)
        self.p2 = gpio.PWM(self.en2, 100)

    def free_run(self):
        print("free run")
        #runs it for 3 seconds slow and then 3 seconds fast
        self.p1.start(20)
        self.p2.start(20)

        gpio.output(self.en1, 1)
        gpio.output(self.r1, 1)
        gpio.output(self.l1, 0)

        gpio.output(self.en2, 1)
        gpio.output(self.r2, 1)
        gpio.output(self.l2, 0)

        time.sleep(3)

        self.p1.ChangeDutyCycle(100)
        self.p2.ChangeDutyCycle(100)
        gpio.output(self.en1, 1)
        gpio.output(self.r1, 1)
        gpio.output(self.l1, 0)

        gpio.output(self.en2, 1)
        gpio.output(self.r2, 1)
        gpio.output(self.l2, 0)

        time.sleep(3)

        self.p1.stop()
        self.p2.stop()
        self.hold()

    def hold(self):
        print("hold")
        gpio.output(self.en1, 0)
        gpio.output(self.en2, 0)

        gpio.output(self.l1, 0)
        gpio.output(self.r1, 0)
        gpio.output(self.l2, 0)
        gpio.output(self.r2, 0)
        gpio.output(self.en2, 0)
        time.sleep(2)


    def turn_right_left_speed(self, speed, right, left):
        print(f"turnning right_left with speed: {speed}, {right}, {left}")
        #turn right slowly or fast
        if right:
            self.p1.start(speed)
            gpio.output(self.en1, 1)
        else:
            self.p2.start(speed)
            gpio.output(self.en2, 1)

        
        gpio.output(self.r1, right)
        gpio.output(self.l1, 0)

        
        gpio.output(self.r2, left)
        gpio.output(self.l2, 0)

        time.sleep(2)
        self.hold()
      


    def move_forw_backw_speed(self, forw, backw, speed):
        print(f"moving forw_back with speed: {forw}, {backw}, {speed}")
        self.p1.start(speed)
        self.p2.start(speed)

        gpio.output(self.en1, 1)
        gpio.output(self.r1, forw)
        gpio.output(self.l1, backw)

        gpio.output(self.en2, 1)
        gpio.output(self.l2, backw)
        gpio.output(self.r2, forw)

        time.sleep(2)
        self.hold()

    def move_forw_speed_left_right(self, right, left): 
        print(f"moving forw and turning with speed: {right}, {left}")
        gpio.output(self.en1, 1)
        gpio.output(self.en2, 1)

        if right:
            self.p1.start(50)
            self.p2.start(30)

        elif left:
            self.p1.start(30)
            self.p2.start(50)

        gpio.output(self.r1, right)
        gpio.output(self.l1, left)

        gpio.output(self.r2, right)
        gpio.output(self.l2, left)

        time.sleep(2)
        self.hold()
    
    def move_backw_speed_left_right(self, right, left): 
        print(f"moving backw and turnning with speed: {right}, {left}")
        gpio.output(self.en1, 1)
        gpio.output(self.en2, 1)

        if right:
            self.p1.start(50)
            self.p2.start(30)

        elif left:
            self.p1.start(30)
            self.p2.start(50)

        gpio.output(self.r1, left)
        gpio.output(self.l1, right)

        gpio.output(self.r2, left)
        gpio.output(self.l2, right)

        time.sleep(2)
        self.hold()



gpio.cleanup()
