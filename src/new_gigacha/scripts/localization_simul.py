#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Pose, PoseStamped
from new_gigacha.msg import Local
from tf.transformations import euler_from_quaternion
import pymap3d
from numpy import rad2deg


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
        self.lat_origin = 37.239231667
        self.lon_origin = 126.773156667
        self.alt_origin = 15.400
        
        # #Songdo
        # self.lat_origin = 37.3851693
        # self.lon_origin = 126.6562271
        # self.alt_origin = 15.4

        #virtual ground
        # self.lat_origin = 4.83333333333e-05
        # self.lon_origin = 124.511281667
        # self.alt_origin = 15.4

        rospy.Subscriber("/simul_gps", Pose, self.gpsCallback)
        rospy.Subscriber("/simul_imu", Pose, self.imuCallback)


    def main(self):
        self.pub.publish(self.msg)
        self.vis_msg.pose.position.x = self.msg.x
        self.vis_msg.pose.position.y = self.msg.y
        self.vis_msg.header.stamp = rospy.Time.now()
        self.vis_pub.publish(self.vis_msg)
        print("Localization is on...")


    def gpsCallback(self, data):
        self.msg.x, self.msg.y, _ = pymap3d.geodetic2enu(data.position.x, data.position.y, self.alt_origin, \
                                            self.lat_origin , self.lon_origin, self.alt_origin)

    def imuCallback(self, data):
        self.vis_msg.pose.orientation = data.orientation
        ori = [data.orientation.x, data.orientation.y, data.orientation.z, data.orientation.w] 
        roll, pitch, yaw = euler_from_quaternion(ori)
        self.msg.heading = rad2deg(yaw) % 360 #East = 0, North = 90, West = 180, South = 270 deg 
        # print(f'msg.heading : {self.msg.heading}')
            

    
if __name__ == '__main__':
    
    loc = Localization()
    rate = rospy.Rate(50)
 
    while not rospy.is_shutdown():

        loc.main()
        rate.sleep()