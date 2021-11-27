class MissionPlanner:
    def __init__(self, ego):
        self.ego = ego


    def run(self):
        
        #Mission Decision
        if self.ego.state is "Ready":
            self.ego.mission=self.ego.global_path.mission[self.ego.index]
            self.ego.mode = "small"

        #     if not self.ego.mission == "":
        #         print(f"========Mission {self.ego.mission} Start")
        #         self.ego.state = "On Mission"


        # #Mode Decision
        # if self.ego.state is not "Ready":

        #     if self.ego.mission is "big":
        #         print('bigbigbigbvigbigibig')

        # else: #Ready
        #     self.ego.mode = "general"
        