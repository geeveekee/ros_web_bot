#!/usr/bin/python3
try:
    from motor_extended import Motor
except ModuleNotFoundError:
    print("issok")

import rospy
from geometry_msgs.msg import Twist

class Subscriber:
    def __init__(self, topic_name):
        rospy.init_node("web_sub")
        self.sub = rospy.rospy.Subscriber(topic_name, Twist, motorCb)

    def motorCb(self, msg):
        print(f"linear: {msg.linear}")
        print(f"angular: {msg.angular}")

if __name__ == '__main__':
    s = Subscriber("/to_rpi")
    rospy.spin()
        


