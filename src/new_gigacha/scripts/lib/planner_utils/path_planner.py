from new_gigacha.srv import *
import rospy

class PathPlanner:
    def __init__(self, ego):
        self.ego = ego


    def run(self):
        if self.ego.state == "LPP":
            #LPP
            pass
        else:
            pass
            #GPP