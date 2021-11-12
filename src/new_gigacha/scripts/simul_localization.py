#!/usr/bin/env python
import serial #Serial USB
import socket #UDP LAN
import rospy
from nav_msgs.msg import Odometry
import pymap3d


class Localization():
    def __init__(self):
        rospy.init_node('Localization', anonymous=False)
        self.pub = rospy.Publisher('/pose', Local, queue_size = 1)
        self.msg = Local()

        #Set
        self.lat_origin = 37.239231667
        self.lon_origin = 126.773156667
        self.alt_origin = 15.400

        self. x = 0
        self. y = 0
        self. yaw = 0

        rospy.Subscriber("/simul_gps", Local, self.gpsCallback)
        rospy.Subscriber("/simul_imu", Local, self.imuCallback)

        rospy
    def main(self):


        self.msg.x = x
        self.msg.y = y

        self.pub.publish(msg)


    def gpsCallback(self, data):
        self.msg.x, self.msg.y, _ = pymap3d.geodetic2enu(data.x, data.y, self.alt_origin, \
                                            self.lat_origin , self.lon_origin, self.alt_origin)


    def imuCallback(self, data):
        self.msg.heading = data.heading


    
if __name__ == '__main__':
    
    loc = Localization()
    rate = rospy.Rate(1000)
 
    loc.connect()
    print("dd")
 
    while not rospy.is_shutdown():

        loc.main()