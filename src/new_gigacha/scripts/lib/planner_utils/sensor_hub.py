import rospy
import message_filters
from new_gigacha.msg import Serial_Info, Local, Obstacles
from lib.planner_utils.mapping import Mapping
from nav_msgs.msg import Odometry


class SensorHub:
    def __init__(self, ego):
        self.ego = ego
        
        rospy.Subscriber("/pose", Local, self.simul_localCallback) #Simul
        # rospy.Subscriber("/pose", Odometry, self.real_localCallback)
        rospy.Subscriber("/serial", Serial_Info, self.serialCallback)



        # obs_sub = message_filters.Subscriber("/obstacles", Obstacles)
        # local_sub = message_filters.Subscriber("/pose", Local)
        # ts = message_filters.ApproximateTimeSynchronizer([obs_sub, local_sub], 10, 0.1, allow_headerless=True)
        # ts.registerCallback(self.obsCallback)

        # self.obs_map_maker = Mapping()

           
    
    def simul_localCallback(self, msg):
        self.ego.pose = msg
    def real_localCallback(self, msg):
        self.ego.pose.x = msg.pose.pose.position.x
        self.ego.pose.y = msg.pose.pose.position.y
        self.ego.pose.heading = msg.twist.twist.angular.z
        

    def serialCallback(self, msg):
        self.ego.speed = msg.speed
        self.ego.steer = msg.steer
        self.ego.brake = msg.brake

    def obsCallback(self, obs, local):
        self.obs_map_maker.mapping(self.ego, obs.circles, local)
        self.ego.obs_map=self.obs_map_maker.showObstacleMap()