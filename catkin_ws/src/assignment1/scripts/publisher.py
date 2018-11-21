#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def publisher():
    pub = rospy.Publisher('5', String, queue_size=10)
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(1)

    myInteger = 100
    while not rospy.is_shutdown():
        info = "Current Integer is %s" % myInteger
        rospy.loginfo(info)
        pub.publish(str(myInteger))
        rate.sleep()
        if myInteger <= 0:
            myInteger = 100
        else:
            myInteger -= 5

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass


