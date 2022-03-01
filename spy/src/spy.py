#!/usr/bin/env python
import cv2
import rospy
from coordi_msgs.msg import coordi
from nav_msgs.msg import Odometry
from std_msgs.msg import Int8

x=1000
y=1000
aruco=100

def callback1(data):
    global x,y
    x=data.pose.pose.position.x
    y=data.pose.pose.position.y

def callback2(data):
    global aruco
    aruco=data.data

if __name__ == '__main__':
    pub = rospy.Publisher('/terrorist_location',coordi ,queue_size=10)
    rospy.Subscriber('/odom', Odometry, callback1)
    rospy.Subscriber('/aruco', Int8, callback2)
    rospy.init_node('spy', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        location=coordi()
        if x<-4.5 and x>-5.5 and y<-8.1 and y>-9.1 and aruco==0:
            location.image=cv2.imread('/home/srinir/catkin_ws/src/Labyrinth-22/spy/src/images/image1.png').reshape(-1)
            location.orientation=[0,0,0.7,0.7]
            pub.publish(location)
        if x<8.6 and x>7.6 and y<-5.4 and y>-6.4 and aruco==10:
            location.image=cv2.imread('/home/srinir/catkin_ws/src/Labyrinth-22/spy/src/images/image2.png').reshape(-1)
            location.orientation=[0,0,0.7,0.7]
            pub.publish(location)
        rate.sleep()
