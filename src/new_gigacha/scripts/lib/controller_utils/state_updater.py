from new_gigacha.msg import Planning_Info, Serial_Info

import rospy

class stateUpdater:
    def __init__(self, state):
        self.state = state

        rospy.Subscriber("/planner", Planning_Info, self.plannerCallback)
        rospy.Subscriber("/serial", Serial_Info, self.serialCallback)


    def plannerCallback(self, msg):
        self.state.index = msg.index
        self.state.x = msg.local.x
        self.state.y = msg.local.y
        self.state.heading = msg.local.heading
        self.state.mode = msg.mode
        
    def serialCallback(self, msg):
        self.state.auto_manual = msg.auto_manual    
        self.state.steer = msg.steer
        self.state.speed = msg.speed
        self.state.brake = msg.brake
        self.state.gear = msg.gear
        
        