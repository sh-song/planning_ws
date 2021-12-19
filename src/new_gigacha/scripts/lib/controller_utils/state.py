
class State:
    def __init__(self):
        self.mission = "Init"
        self.mode = "Init"
        self.status ="Ready" #ready, driving
        self.index = -1
        self.x = -1.0
        self.y = -1.0
        self.heading = -1.0
        self.speed = -1.0
        self.brake = -1.0
        self.steer = -1.0
        self.gear = -1.0
        self.target_speed = 0.0
        self.auto_manual = -1.0    

        
