#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Pose, PoseStamped
from new_gigacha.msg import Local
from sensor_msgs.msg import NavSatFix, Imu
from tf.transformations import euler_from_quaternion
import pymap3d
from numpy import rad2deg
from ublox_msgs.msg import NavPVT

#roslaunch ublox_gps ublox_zed-f9p.launch
class Localization():
    def __init__(self):
        rospy.init_node('Localization', anonymous=False)
        self.pub = rospy.Publisher('/pose', Local, queue_size = 1)
        self.msg = Local()

        #Visualization
        self.vis_pub = rospy.Publisher('/vis_pose', PoseStamped, queue_size=1)
        self.vis_msg = PoseStamped()
        self.vis_msg.header.frame_id = "map"
        
        #KCity
        # self.lat_origin = 37.239231667
        # self.lon_origin = 126.773156667
        # self.alt_origin = 15.400
        
        #Songdo
        self.lat_origin = 37.3851693 
        self.lon_origin = 126.6562271
        self.alt_origin = 15.4

        self.yaw_gps = 0
        self.hAcc = 0
        self.headingAcc = 0
        self.offset = 0
        self.yaw_imu = 0
        self.final_yaw = 0
        self.gear = None
        self.HeadingFrontBackFlg = 1


        rospy.Subscriber("/simul_gps", Pose, self.gpsCallback)
        rospy.Subscriber("/simul_imu", Pose, self.imuCallback)
        
        rospy.Subscriber('/gps_data/navpvt',NavPVT, self.gps_Heading)
        rospy.Subscriber("/gps_data/fix", NavSatFix, self.gpsCallback)
        rospy.Subscriber("/imu", Imu, self.imuCallback)



    def main(self):
        self.decide_heading()        
        self.pub.publish(self.msg)
        self.vis_msg.pose.position.x = self.msg.x
        self.vis_msg.pose.position.y = self.msg.y
        self.vis_msg.header.stamp = rospy.Time.now()
        self.vis_pub.publish(self.vis_msg)
        print("Localization is on...")


    def gpsCallback(self, data):
        self.msg.x, self.msg.y, _ = pymap3d.geodetic2enu(data.latitude, data.longitude, self.alt_origin, \
                                            self.lat_origin , self.lon_origin, self.alt_origin)

    def imuCallback(self, data):
        self.vis_msg.pose.orientation = data.orientation
        self.yaw_imu = -data.orientation.x
        self.msg.heading = self.yaw_final

        # self.msg.heading = rad2deg(self.yaw) % 360 #East = 0, North = 90, West = 180, South = 270 deg
        
    def gps_Heading(self, data):
        self.yaw_gps = (450-(data.heading * 10**(-5)))%360
        self.hAcc = data.hAcc
        self.headingAcc =data.headAcc

    def yaw_check(self):
        if self.gear == None:
            self.gear = 0
            
        if self.HeadingFrontBackFlg == 1 and self.headingAcc < 700000 and self.gear == 0 :
            self.yaw_flag = 1               
        else:
            self.yaw_flag = 0

    def decide_heading(self):
        self.yaw_check()                    
        if self.yaw_flag == 1: 
            self.offset = self.yaw_gps - self.yaw_imu 
            self.yaw_final = self.yaw_imu + self.offset
            self.yaw_final = self.yaw_final % 360

        elif self.yaw_flag == 0:
            self.yaw_final = self.yaw_imu % 360

        # self.yaw_final = self.yaw_imu % 360
        
         
            
if __name__ == '__main__':
    
    loc = Localization()
    rate = rospy.Rate(50)
 
    while not rospy.is_shutdown():

        loc.main()
        rate.sleep()