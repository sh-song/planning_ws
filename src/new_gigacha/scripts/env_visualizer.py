import rospy
from sensor_msgs.msg import PointCloud
from geometry_msgs.msg import Point32
from nav_msgs.msg import Odometry
from new_gigacha.msg import Local
from lib.general_utils.sig_int_handler import Activate_Signal_Interrupt_Handler
from lib.general_utils.read_global_path import read_global_path

class environmentVisualizer:
    def __init__(self):
        rospy.init_node("Environment_Visualizer", anonymous=False)
        self.vis_global_path_pub = rospy.Publisher("/vis_global_path", PointCloud, queue_size=1)
        self.vis_global_path_msg = PointCloud()
        self.vis_global_path_msg.header.frame_id = "map"

        global_path = read_global_path('kcity', 'final')
        for i in range(len(global_path.x)):
            self.vis_global_path_msg.points.append(Point32(global_path.x[i], global_path.y[i], 0))
    
        # self.obsmap_pub = rospy.Publisher("/vis_map", PointCloud, queue_size=1)
        # self.obsmap = PointCloud()
        # self.obsmap.header.frame_id = "map"
    

        # self.local_path_pub = rospy.Publisher("/vis_local_path", PointCloud, queue_size=1)
        # self.obs_pub = rospy.Publisher("/vis_obs_pub", PointCloud, queue_size=1)
        # self.target_pub = rospy.Publisher("/vis_target", PointCloud, queue_size=1)

        # self.vis_local_path = PointCloud()
        # self.vis_local_path.header.frame_id = "map"


        # self.obs = PointCloud()
        # self.obs.header.frame_id = "map"

        # self.target = PointCloud()
        # self.target.header.frame_id = "map"

    def run(self):
        print(f"Publishing maps for visualization")
        self.vis_global_path_msg.header.stamp = rospy.Time.now()
        self.vis_global_path_pub.publish(self.vis_global_path_msg)


        # self.obsmap.points = self.ego.obs_map.points
        # self.obsmap.header.stamp = rospy.Time.now()
        # self.obsmap_pub.publish(self.obsmap)



if __name__ == "__main__":
    Activate_Signal_Interrupt_Handler()
    vv = environmentVisualizer()
    rate = rospy.Rate(10)
    while True:
        vv.run()
        rate.sleep()
