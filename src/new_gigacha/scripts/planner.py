from lib.general_utils.sig_int_handler import Activate_Signal_Interrupt_Handler
from lib.planner_utils.mission_planner import MissionPlanner
from lib.planner_utils.path_planner import PathPlanner
from lib.planner_utils.index_finder import IndexFinder
from lib.planner_utils.sensor_hub import SensorHub

from new_gigacha.msg import Local, Path, Planning_Info
import rospy

class EgoVehicle:
    def __init__(self):
        self.mission = "Init"
        self.mode = "Init"
        self.state ="Ready" 
        self.pose = Local() #x, y, heading
        self.index = -1
        self.speed = -1
        self.brake = -1
        self.steer = -1
        self.nearby_obs = []
        self.global_path = Path()
    


class Planner:
    def __init__(self):
        rospy.init_node("Planner", anonymous=False)
        self.ego = EgoVehicle()
        self.sensor_hub = SensorHub(self.ego)
        self.path_planner = PathPlanner(self.ego, 'kcity', 'final')
        self.whereami = IndexFinder(self.ego)
        self.mission_planner = MissionPlanner(self.ego)
      
        self.planning_pub = rospy.Publisher("/planner", Planning_Info, queue_size=1)
        self.planning_msg = Planning_Info()

    def run(self):
        self.whereami.run()
        self.mission_planner.run()
        self.path_planner.run()
        ####
        self.planning_msg.mode = self.ego.mode
        self.planning_msg.local = self.ego.pose
        self.planning_pub.publish(self.planning_msg)
        print(self.ego.index)




if __name__ == "__main__":
    Activate_Signal_Interrupt_Handler()
    pp = Planner()
    r = rospy.Rate(1000)
    while True:
        print('===========')
        pp.run()
 
