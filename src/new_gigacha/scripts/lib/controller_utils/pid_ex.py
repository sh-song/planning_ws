class PID:
    def __init__(self, P, I, D):

        self.P = P
        self.I = I
        self.D = D
        self.pre_error = 0.0
        self.error_sum = 0.0
        self.dt = 1.0 / 10.0

    def run(self, current, target):
        error = target - current
        diff_error = error - self.pre_error
        self.pre_error = error
        self.error_sum += error
        return self.P*error + self.D*diff_error/self.dt # self.I*self.error_sum*self.dt


