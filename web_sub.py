#!/usr/bin/python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import time
import random
from motor_extended import Motor
from math import sqrt, atan

my_list = ['f', 'b', 't']

def is_inside(a1, a2, x, z):
	#angles must b radians
	start_angle = a1
	end_angle = a2
	angle = atan(z/x)

	if(angle > a1 and angle < a2):
		return 1
	else:
		return 0
	
def what_to_do(x, z):
	if is_inside(-0.39, 0.39, x, z):
		print("turning right")
		m.turn_right_left_speed(100, 1, 0)

	elif is_inside(0.39, 1.17, x, z):
		print("Forward and right")
		m.move_forw_speed_left_right(1, 0)

	elif is_inside(1.17, 1.9, x, z):
		print("forward")
		m.move_forw_backw_speed(1, 0, 100)

	elif is_inside(1.9, 3.5, x, z):
		print("forward and left")
		m.move_forw_speed_left_right(0, 1)
		
	elif is_inside(3.5, -3.5, x, z):
		print("turning left")
		m.turn_right_left_speed(100, 0, 1)

	elif is_inside(-3.5, -1.9, x, z):
		print("backw and left")
		m.move_backw_speed_left_right(0, 1)

	elif is_inside(-1.9, -1.17, x, z):
		print("Backward")
		m.move_forw_backw_speed(0, 1, 100)

	elif is_inside(-1.17, -0.39, x, z):
		print("Backward and right")
		m.move_backw_speed_left_right(1, 0)

def print_cb(evt):
	print(f"**********: {linear_x}")
	print(f"**********: {angular_z}")
	what_to_do(linear_x, angular_z)
	#global my_list
	#funct = random.choice(my_list)
	#print(funct)
	#if funct == 'f':
	#	m.forward()
	#elif funct == 'b': 
	#	m.backward()
	#else:
	#	m.turn()


def callback(msg):
	print(f"linear: {msg.linear.x}")
	print(f"angular: {msg.angular.z}")
	global linear_x, angular_z
	linear_x = msg.linear.x 
	angular_z = msg.angular.z 


def listener():
	rospy.init_node('twist_sub', anonymous=True)
	rospy.Subscriber("/test", Twist, callback)

	rospy.Timer(rospy.Duration(3), print_cb)
	rospy.spin()

if __name__ == '__main__':
	m = Motor()
	listener()

