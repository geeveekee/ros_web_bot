#!/usr/bin/python3
import rospy
from std_msgs.msg import Bool, String
import RPi.GPIO as gpio


def led(data):
    print(data.data)
    gpio.output(led, data.data)

def motor(data1):
    print(data1.data)

def listener():
    led_sub = rospy.Subscriber('led_state', Bool, led)
    motor_sub = rospy.Subscriber('motor_ctl', String, motor)

if __name__ == '__main__':
    rospy.init_node('listener', anonymous=True)
    led=13
    gpio.setmode(gpio.BOARD)
    gpio.setup(led, gpio.OUT)

    listener()
    rospy.spin()
    gpio.cleanup()
