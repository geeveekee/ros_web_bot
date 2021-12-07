#!/usr/bin/python3
import rospy
from std_msgs.msg import Bool, String

def talker(event):

    led_pub = rospy.Publisher('led_state', Bool, queue_size=100)
    motor_pub = rospy.Publisher('motor_ctl', String, queue_size=100)

    led_data = Bool(1)
    motor_data = "forward"

    print(f"LED: {led_data}")
    print(f"MOTOR: {motor_data}")
    
    led_pub.publish(led_data)
    motor_pub.publish(motor_data)

if __name__ == '__main__':
    try:
        rospy.init_node('led_talker', anonymous=True)
        T = rospy.Duration(1)
        timer = rospy.Timer(T, talker)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
