#!/usr/bin/python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import time
import random
from motor_extended import Motor
from math import sqrt, atan, pi
import RPi.GPIO as io

my_list = ['f', 'b', 't']

def is_inside(x, z):
	#angles must b radians

	angle = atan(z/x)
	pie = pi

	if((x>0 and z>0) or (x>0 and z<0)):
		angle = angle
	elif(x<0 and z>0):
		angle = pi+angle
	elif(x<0 and z<0):
		angle = -(pie-angle)

	if((-pie/8)<angle and (pie/8)>=angle):
		print("right")
		m.turn_right_left_speed(80, 1, 0)
		return 1

	elif((pie/8)<angle and (3*pie/8)>=angle):
		print("right forward")
		m.move_forw_speed_left_right(1, 0)
		return 1

	elif((3*pie/8)<angle and (5*pie/8)>=angle):
		print("forward")
		m.move_forw_backw_speed(1, 0, 80)
		return 1

	elif((5*pie/8)<angle and (7*pie/8)>=angle):
		print("left forward")
		m.move_forw_speed_left_right(0, 1)
		return 1

	elif(((7*pie/8)<angle and (pie)>=angle) or ((-pie)<angle and (-7*pie/8)>=angle)):
		print("left")
		m.turn_right_left_speed(80, 0, 1)
		return 1

	elif((-7*pie/8)<angle and (-5*pie/8)>=angle):
		print("left backward")
		m.move_backw_speed_left_right(0, 1)
		return 1

	elif((-5*pie/8)<angle and (-3*pie/8)>=angle):
		print("backward")
		m.move_forw_backw_speed(0, 1, 80)
		return 1

	elif((-3*pie/8)<angle and (-pie/8)>=angle):
		print("right backward")
		m.move_backw_speed_left_right(1, 0)
		return 1

	else:
		return 0
	#if(x < 0 or z < 0):
	#	a1 = -(3.14 - a1)
	#	a2 = -(3.14 - a2)
	#	if((angle > a1) and (angle < a2)):
	#		return 1
	#	else:
	#		return 0
	#else:
	#	if((angle > a1) and (angle < a2)):
	#		return 1
	#	else:
	#		return 0



def what_to_do(x, z):

	
	if is_inside(-0.39, 0.39, x, z):
		print("turning right")
		m.turn_right_left_speed(80, 1, 0)

	elif is_inside(0.39, 1.17, x, z):
		print("Forward and right")
		m.move_forw_speed_left_right(1, 0)

	elif is_inside(1.17, 1.9, x, z):
		print("forward")
		m.move_forw_backw_speed(1, 0, 80)

	elif is_inside(1.9, 3.5, x, z):
		print("forward and left")
		m.move_forw_speed_left_right(0, 1)
		
	elif is_inside(3.5, -3.5, x, z):
		print("turning left")
		m.turn_right_left_speed(80, 0, 1)

	elif is_inside(-3.5, -1.9, x, z):
		print("backw and left")
		m.move_backw_speed_left_right(0, 1)

	elif is_inside(-1.9, -1.17, x, z):
		print("Backward")
		m.move_forw_backw_speed(0, 1, 80)

	elif is_inside(-1.17, -0.39, x, z):
		print("Backward and right")
		m.move_backw_speed_left_right(1, 0)

	elif (x == 0 and z == 0):
		print("hold")
		m.hold()
	else:
		print("nackwards")
		m.move_forw_backw_speed(0, 1, 80)

def print_cb(evt):
	try:
		print(f"**********: {linear_x}")
		print(f"**********: {angular_z}")
	except NameError:
		print("ffs")
		listener()
	
	is_inside(linear_x, angular_z)
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

	global linear_x, angular_z
	
	linear_x = msg.linear.x 
	angular_z = msg.angular.z 
	print(f"x: {linear_x}, z: {angular_z}")


def listener():
	global linear_x, angular_z
	
	rospy.init_node('twist_sub', anonymous=True)
	rospy.Subscriber("/to_rpi", Twist, callback)

	rospy.Timer(rospy.Duration(3), print_cb)
	rospy.spin()

if __name__ == '__main__':
	m = Motor()
	listener()

io.cleanup()
