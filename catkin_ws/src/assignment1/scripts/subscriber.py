#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    #rospy.loginfo('cccc %s', data.data)
    rospy.loginfo('Current Number from listener is %s', str(int(data.data) + 5))

def listener():
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber('5', String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()