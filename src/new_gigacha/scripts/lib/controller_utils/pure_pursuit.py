from math import hypot, cos, sin, degrees, atan2, radians, pi

class PurePursuit:
    def __init__(self, state, global_path, local_path):
        self.WB = 1.04 # wheel base
        self.k = 0.3 #1.5
        self.lookahead_default = 4.0 #look-ahead default

        self.state = state
        self.global_path = global_path
        self.local_path = local_path
        

    def run(self):
       
        if self.state.mode == "local path tracking":
            path = self.local_path
        else:
            path = self.global_path

        if self.state.mode == "driving":
            lookahead = min(self.k * self.state.speed + self.lookahead_default, 6) # look-ahead
        else :
            lookahead = 0.5
            
        target_index = int(self.state.index + lookahead*10)
        target_x, target_y = path.x[target_index], path.y[target_index]
        print(f"target_index : {target_index}")
        tmp = degrees(atan2(target_y - self.state.y, target_x - self.state.x)) % 360

        if self.state.mode == "backward" :
            self.state.heading = (self.state.heading + 180) % 360        
    
        alpha = self.state.heading - tmp
        angle = atan2(2.0 * self.WB * sin(radians(alpha)) / lookahead, 1.0)

        print(f"target_index : {target_index}")
        print(f"tmp : {tmp}")
        print(f"heading : {self.state.heading}")

        if self.state.mode == "backward" :
            angle = -angle

        return max(min(degrees(angle), 27.0), -27.0), target_index
        # return max(min(degrees(angle), 27.0), -27.0)
        # return angle

    
    def deaccel(self):
        
        if self.state.mode == "local path tracking":
            path = self.local_path
        else:
            path = self.global_path

        if self.state.mode == "driving":
            lookahead = min(self.k * self.state.speed + self.lookahead_default, 6) # look-ahead
        else :
            lookahead = 0.8

        target_index_v = int(self.state.index + lookahead*25)
        target_x_v, target_y_v = path.x[target_index_v], path.y[target_index_v]
        curve_check = abs (self.state.heading - degrees(atan2(target_y_v - self.state.y, target_x_v - self.state.x)) % 360  )
        return curve_check