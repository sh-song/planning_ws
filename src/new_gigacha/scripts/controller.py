

class Controller:
    def __init__(self):
        rospy.init_node("Planner", anonymous=False)
        print(f"Planner: Initializing Planner...")
        self.ego = EgoVehicle()
        self.ego.global_path = read_global_path('kcity', 'final')
