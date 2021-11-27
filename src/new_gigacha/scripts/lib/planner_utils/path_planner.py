import rospy

class PathPlanner:
    def __init__(self, ego):
        self.ego = ego
        

    def run(self):
        if self.ego.mode == "small" and self.ego.obs_map.points:
            self.ego.local_path = lpp(self.ego.pose,self.ego.global_path,self.ego.index,self.ego.obs_map)
            pass
        else:
            pass
            #GPP