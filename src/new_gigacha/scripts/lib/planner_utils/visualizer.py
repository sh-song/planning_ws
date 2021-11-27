import rospy
from sensor_msgs.msg import PointCloud
from geometry_msgs.msg import Point32
from new_gigacha.msg import Local

class Visualizer:
    def __init__(self,ego):
        self.ego = ego
        self.global_path_pub = rospy.Publisher("/global_path", PointCloud, queue_size=1)
        self.vis_global_path = PointCloud()
        self.vis_global_path.header.frame_id = "world"

        self.pose_pub = rospy.Publisher("/pose_pub", PointCloud, queue_size=1)
        self.pose = PointCloud()
        self.pose.header.frame_id = "world"

        self.obsmap_pub = rospy.Publisher("/map_pub", PointCloud, queue_size=1)
        self.obsmap = PointCloud()
        self.obsmap.header.frame_id = "world"


        # self.local_path_pub = rospy.Publisher("/local_path", PointCloud, queue_size=1)
        # self.obs_pub = rospy.Publisher("/obs_pub", PointCloud, queue_size=1)
        # self.target_pub = rospy.Publisher("/target", PointCloud, queue_size=1)

        # self.vis_local_path = PointCloud()
        # self.vis_local_path.header.frame_id = "world"


        # self.obs = PointCloud()
        # self.obs.header.frame_id = "world"

        # self.target = PointCloud()
        # self.target.header.frame_id = "world"

    def run(self):
        if len(self.vis_global_path.points) == 0:
            for i in range(len(self.ego.global_path.x)):
                self.vis_global_path.points.append(Point32(self.ego.global_path.x[i], self.ego.global_path.y[i], 0))
                self.vis_global_path.header.stamp = rospy.Time.now()

        
        self.global_path_pub.publish(self.vis_global_path)

        self.pose.points = []
        self.pose.points.append(Point32(self.ego.pose.x, self.ego.pose.y, 0))
        self.pose.header.stamp = rospy.Time.now()
        self.pose_pub.publish(self.pose)


        self.obsmap.points = self.ego.obs_map.points
        self.obsmap.header.stamp = rospy.Time.now()
        self.obsmap_pub.publish(self.obsmap)
