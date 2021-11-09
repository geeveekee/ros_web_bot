#!/usr/bin/python3

import rospy
import RPi.GPIO as gpio 
from std_msgs.msg import Bool

button = 


if __name__ =='__main__':
    rospy.init_node("button_publisher")

    pub = rospy.Publisher('button_state', Bool, queue_size=20)

    gpio.setmode(gpio.BOARD)
    gpio.setup(button, gpio.IN, pull_up_down = gpio.PUD_UP)

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        button_state = not gpio.input(button)
        pub.publish(button_state)
        rospy.loginfo(button_state)
        rate.sleep()

    gpio.cleanup()