from math import hypot, cos, sin, degrees, atan2, radians, asin, pi
import numpy as np
from numpy.lib.utils import lookfor
from lib.controller_utils.pure_pursuit import PurePursuit
from lib.controller_utils.stanley import Stanley_Method

class Combined_Method:
    def __init__(self, state, global_path, local_path):
        self.k_min = 0.2
        self.k_max = 0.8
        
        self.state = state
        self.global_path = global_path
        self.local_path = local_path

        self.combined_pp= PurePursuit(self.state, self.global_path, self.local_path) 
        self.combined_st= Stanley_Method(self.state, self.global_path, self.local_path)


    def run(self):
        self.combined_st.make_yaw()
        self.steer_pp, self.target_index = self.combined_pp.run()
        self.steer_st = self.combined_st.run()

        if self.state.mode == "local path tracking":
            path = self.local_path
        else:
            path = self.global_path

        target_x, target_y = path.x[self.target_index], path.y[self.target_index]

        beta = atan2(path.x[self.target_index + 1] - target_x, path.y[self.target_index + 1] - target_y)\
                -atan2(target_x - path.x[self.target_index - 1],target_y - path.y[self.target_index - 1])

        d = hypot((target_x - path.x[self.target_index - 1]),\
            (target_y - path.y[self.target_index - 1]))

        self.R_min = (d)/(2*sin((20*pi)/180))     ## maximum steer angle in xx
        self.beta_max = 2*(asin(((d)/2)/self.R_min))

        if beta >= self.beta_max:
            k_pp = self.k_max
        else:
            k_pp = self.k_min + (beta/self.beta_max)*(self.k_max - self.k_min)

        k_st = 1 - k_pp
        if self.state.mode == "backward":
            k_pp = 0
        # print(f"d : {d}")
        # print(f"R_min : {self.R_min}")
        print(f"k_pp : {k_pp}")
        print(f"k_st : {k_st}")
        print(f"steer_pp : {self.steer_pp}")
        print(f"steer_st : {self.steer_st}")
       
        steer = k_pp*self.steer_pp + k_st*self.steer_st
        print(f"steer : {steer}")
        return steer

