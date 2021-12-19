from math import hypot, cos, sin, degrees, atan2, radians

class PurePursuit:
    def __init__(self, state, global_path, local_path):
        self.WB = 1.04 # wheel base
        self.k = 0.03 #1.5
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
            lookahead = 2
            
        target_index = int(self.state.index + lookahead*10)
        target_x, target_y = path.x[target_index], path.y[target_index]

        tmp = degrees(atan2(target_y - self.state.y, target_x - self.state.x)) % 360
        alpha = self.state.heading - tmp

        print(f"tmp_value : {tmp}")
        print(f"self.state.heading value :{self.state.heading}")

        angle = atan2(2.0 * self.WB * sin(radians(alpha)) / lookahead, 1.0)
        return max(min(degrees(angle), 27.0), -27.0)
