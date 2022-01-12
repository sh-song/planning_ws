from math import hypot
from time import time
class MissionPlanner:
    def __init__(self, ego):
        self.ego = ego
        self.pre_time = -1
        self.check = 0
        self.aft_time = -1

    def run(self):
        
        #Mission Decision
        # if self.ego.status is "Ready":
            # self.ego.mission=self.ego.global_path.mission[self.ego.index]
            # self.ego.mode = "small"


        if self.ego.mission == "Init":
            self.ego.mission = "parking"

        print(f"status: {self.ego.status}\n, mode:{self.ego.mode}")
        if self.ego.mission == "parking":
            dist1 = hypot(self.ego.pose.x - self.ego.global_path.x[990], \
                        self.ego.pose.y - self.ego.global_path.y[990]  )
            # dist1 = hypot(self.ego.pose.x - self.ego.global_path.x[0], \
            #     self.ego.pose.y - self.ego.global_path.y[0]  )
            print(f"dist1: {dist1}")
            
            
            if dist1 < 1 and self.ego.mode == "driving" and self.pre_time < 0 and self.check == 0 :
                self.ego.status = "parking ready"
                self.ego.mode = "stop"
                self.pre_time = time()

            if dist1 < 1.5 and self.ego.mode == "stop" and time() - self.pre_time > 3:
                self.ego.mode = "parking_driving"
                self.pre_time = -1
                self.check = 1
                
        
            dist2 = hypot(self.ego.pose.x - self.ego.global_path.x[1113], \
                        self.ego.pose.y - self.ego.global_path.y[1113]  )
            print(f"dist2: {dist2}")

            
            if dist2 < 1 and self.ego.mode == "parking_driving" and self.aft_time < 0:
                self.ego.status = "parking complete"
                self.ego.mode = "emergency_stop"
                self.aft_time = time()
                


            if self.ego.status == "parking complete" and time() - self.aft_time > 3:
                self.ego.status = "parking backward"
                self.ego.mode = "backward"
                self.aft_time = -1

            
            if dist1 < 1.5 and self.ego.status == "parking backward" and self.aft_time < 0 :
                self.ego.status = "parking end"
                self.ego.mode = "emergency_stop"
                self.aft_time = time()


            if self.ego.status == "parking end" and time() - self.aft_time > 3:
                self.ego.status = "general"
                self.ego.mode = "driving"

                self.ego.mission = "gogo"

            
            

            
        

        # #Mode Decision
        # if self.ego.state is not "Ready":

        #     if self.ego.mission is "big":
        #         print('bigbigbigbvigbigibig')

        # else: #Ready
        #     self.ego.mode = "general"
        