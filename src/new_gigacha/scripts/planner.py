from lib.general_utils.sig_int_handler import Activate_Signal_Interrupt_Handler
from lib.planner_utils.mission_planner import MissionPlanner
from lib.planner_utils.path_planner import PathPlanner
from lib.planner_utils.index_finder import IndexFinder
from lib.planner_utils.sensor_hub import SensorHub
from lib.general_utils.read_global_path import read_global_path
from lib.general_utils.ego import EgoVehicle

from new_gigacha.msg import Local, Path, Planning_Info
from math import hypot
import rospy



class Planner:
    def __init__(self):
        rospy.init_node("Planner", anonymous=False)
        print(f"Planner: Initializing Planner...")
        self.ego = EgoVehicle()
        #self.ego.global_path = read_global_path('songdo', 'parking')
        self.ego.global_path = read_global_path('songdo', 'parking_simul')

        self.sensor_hub = SensorHub(self.ego)
        self.path_planner = PathPlanner(self.ego)
        self.whereami = IndexFinder(self.ego)
        self.mission_planner = MissionPlanner(self.ego)
        self.planning_pub = rospy.Publisher("/planner", Planning_Info, queue_size=1)
        self.planning_msg = Planning_Info()

    def publish_planning_info(self):
        self.planning_msg.index = self.ego.index
        self.planning_msg.mode = self.ego.mode
        self.planning_msg.local = self.ego.pose
        self.planning_pub.publish(self.planning_msg)

    def run(self):
        # print(self.ego.obs_map)
        self.whereami.run()
        self.mission_planner.run()
        self.path_planner.run()


        self.publish_planning_info()

        print(f'Ego index: {self.ego.index}')

        distance = hypot(self.ego.global_path.x[0]-self.ego.pose.x, self.ego.global_path.y[0]-self.ego.pose.y)
        print(f"Distance: {distance}")


if __name__ == "__main__":
    Activate_Signal_Interrupt_Handler()
    pp = Planner()
    rate = rospy.Rate(20)
    while True:
        pp.run()
        rate.sleep()
