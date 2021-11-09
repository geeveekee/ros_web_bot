#!/usr/bin/python3
from sys import exc_info
import rospy
from std_msgs.msg import String

def talker():
    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('comm', String, queue_size=100)
    rate = rospy.Rate(1)
    count = 0

    while not rospy.is_shutdown():
        hello_str = "Hello world %d" %count
        rospy.loginfo(hello_str)     
        pub.publish(hello_str)
        count+=1
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass