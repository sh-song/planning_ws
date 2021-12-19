from new_gigacha.msg import Local, Path, Planning_Info
from sensor_msgs.msg import PointCloud

class EgoVehicle:
    def __init__(self):
        self.mission = "Init"
        self.mode = "driving" 
        self.status ="Ready" 
        self.pose = Local() #x, y, heading
        self.index = -1
        self.speed = -1
        self.brake = -1
        self.steer = -1
        # self.nearby_obs = []
        self.obs_map=PointCloud()
        self.global_path = Path()
        self.local_path=Path()
        self.veh_index=0