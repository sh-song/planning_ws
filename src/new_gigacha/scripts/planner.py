from lib.general_utils.sig_int_handler import Activate_Signal_Interrupt_Handler
from lib.planner_utils.global_path_planner import global_map_client
# from lib.planner_utils.mission_planner import MissionPlanner
from lib.planner_utils.path_planner import PathPlanner
# from lib.planner_utils.index_finder import IndexFinder
from lib.planner_utils.sensor_hub import SensorHub

from new_gigacha.msg import Local, Path
import rospy

class EgoVehicle:
    def __init__(self):
        self.mission = ""
        self.state =""
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
        # self.whereami = IndexFinder(self.ego)
        # self.mission_planner = MissionPlanner(self.ego)
      

    def run(self):
        # self.mission_planner.run()
        # self.path_planner.run()
        # self.whereami.run()
        print(self.ego.global_path)


# global_map = global_map_client("kcity", "final")

# print(type(global_map))

if __name__ == "__main__":
    Activate_Signal_Interrupt_Handler()
    pp = Planner()

    while True:
        print('=======')

        pp.run()