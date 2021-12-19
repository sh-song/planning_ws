class PID:
    def __init__(self, P, I, D, state):
        self.state = state
        self.pre_auto_manual = -1
        self.P = P
        self.I = I
        self.D = D
        self.pre_error = 0.0
        self.error_sum = 0.0
        self.dt = 1.0 / 10.0
        self.target_ex = 0
        self.delta_target = 0

    def run(self, current, target):
        if self.state.auto_manual > self.pre_auto_manual : 
            self.error_sum = 0.0
            
            print("----------------------------------------")
        
        self.pre_auto_manual = self.state.auto_manual
        print(self.error_sum)


        error = target - current
        diff_error = min(60, error - self.pre_error) 
        self.pre_error = error
        self.error_sum += error
        self.delta_target = abs(target - self.target_ex)

        return max(target - 1 , self.P*error + self.D*diff_error/self.dt + self.I*self.error_sum*self.dt)

        # if (target >= current or self.delta_target > 3 ) and target > 2  :
        #     self.target_ex = target

        #     return self.P*error + self.D*diff_error/self.dt + self.I*self.error_sum*self.dt
        # else :
        #     self.target_ex = target
        #     return target


