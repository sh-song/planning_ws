from math import hypot, cos, sin, degrees, atan2, radians, pi, sqrt
import numpy as np

class Stanley_Method:
    def __init__(self, state, global_path, local_path):
        self.k = 0.5 # CTR parameter
        
        self.state = state
        self.global_path = global_path
        self.local_path = local_path
        self.yaw = []

    def normalize(self, angle):
        while angle > pi:
            angle -= 2.0 * pi

        while angle < -pi:
            angle += 2.0 * pi

        return angle
    
    def make_yaw(self):
        for i in range(len(self.global_path.x)-1):
            self.yaw.append(atan2(self.global_path.x[i+1]-self.global_path.x[i],\
                self.global_path.y[i+1]-self.global_path.y[i]))   
        # print(self.yaw)  

    def run(self):        
        if self.state.mode=="local path tracking":
            path = self.local_path
        else:
            path = self.global_path

        min_dist = 1e9
        min_index = 0
        n_points = len(self.global_path.x)

        front_x = self.state.x 
        front_y = self.state.y 

        for i in range(n_points):
            dx = front_x - self.global_path.x[i]
            dy = front_y - self.global_path.y[i]

            dist = sqrt(dx*dx+dy*dy)
            
            if dist < min_dist:
                min_dist = dist
                min_index = i

        map_x =  self.global_path.x[min_index]
        map_y =  self.global_path.y[min_index]
        map_yaw = self.yaw[min_index]
        dx = map_x - front_x
        dy = map_y - front_y

        perp_vec = [cos(self.state.heading+pi/2), sin(self.state.heading+pi/2)]
        cte = np.dot([dx, dy], perp_vec)
        
        final_yaw = map_yaw - self.state.heading
        # control law
        yaw_term = self.normalize(final_yaw)
        cte_term = atan2(self.k*cte, self.state.speed)

        # steering
        steer = yaw_term + cte_term
        return max(min((steer), 27.0), -27.0)
        # return steer