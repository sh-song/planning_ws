from new_gigacha.srv import *
import rospy

class PathPlanner:
    def __init__(self, ego, where, name):
        self.ego = ego
        self.ego.global_path \
            = self.read_global_path_from_map(where, name)

    def read_global_path_from_map(self, where, name):
        rospy.wait_for_service('global_map')
        try:
            global_map = rospy.ServiceProxy('global_map', GlobalMap)
            return global_map(where, name).path

        except rospy.ServiceException as e:
                print(f"Service call failed: {e}")


    def run(self):
        if self.ego.state == "LPP":
            #LPP
            pass
        else:
            pass
            #GPP