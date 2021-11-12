import rospy
from new_gigacha.msg import Serial_Info, Local

class SensorHub:
    def __init__(self, ego):
        self.ego = ego
        
        rospy.Subscriber("/pose", Local, self.localCallback)
        rospy.Subscriber("/serial", Serial_Info, self.serialCallback)        

    def localCallback(self, msg):
        self.ego.pose = msg

    def serialCallback(self, msg):
        self.ego.speed = msg.speed
        self.ego.steer = msg.steer
        self.ego.brake = msg.brake