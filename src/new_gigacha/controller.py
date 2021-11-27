    
class Controller:
    def __init__(self):
        rospy.init_node("Controller", anonymous=False)

        rospy.Subscriber("/planner", Planning_Info, self.planningCallback)



    
    def planningCallback(self, msg):
        self.planning_info = msg
        self.local_point = msg.point
        self.local.x = msg.local.x
        self.local.y = msg.local.y
        self.local.heading = msg.local.heading
        # print(self.planning_info)
        if msg.mode == "general" and not self.control_ready:
            self.global_path.x = msg.path.x
            self.global_path.y = msg.path.y
            self.global_path.k = msg.path.k
            self.global_path.heading = msg.path.heading
            self.global_path.env = msg.path.env
            self.global_path.mission = msg.path.mission

            if self.global_path.x:
                self.control_ready = True
    def select_target(self, lookahead):  # 여기서 사용하는 self.path 관련정보를 바꾸면 됨. 여기서바꿔야하나?
        # min_dis = 99999
        # min_idx = 0
        # if self.first_check: # cur_idx 잡는데, 배달미션이나 cross 되는부분은
        #     for i in range(len(self.path.x)):
        #         dis = hypot(self.path.x[i]-self.cur.x,self.path.y[i]-self.cur.y)
        #         if min_dis > dis and abs(self.cur.heading-self.path.heading[i]) <30: # 여기에 등호가 붙으면, 뒷부분 index 잡고, 안붙으면 앞쪽 index
        #             min_dis = dis
        #             min_idx = i

        #     self.first_check = False
        # else:
        #     for i in range(max(self.cur_idx-50,0),self.cur_idx+50):
        #         dis = hypot(self.path.x[i]-self.cur.x,self.path.y[i]-self.cur.y)
        #         if min_dis > dis:
        #             min_dis = dis
        #             min_idx = i

        # self.cur_idx = min_idx # 차량과 가장 가까운 index.
        self.target_index = int(self.cur_idx + lookahead * 10)
        self.speed_idx = self.cur_idx + 60  # speed_idx는 무조건 이거로 가자.(speed_ld랑 상관없이)

    # def pure_pursuit(self,point):
    def pure_pursuit(self):

        # self.lookahead = 3
        if 10 < self.serial_info.speed < 20:
            self.lookahead = 0.2 * (self.serial_info.speed - 10) + 4  # 4로 바꾸기도 해.
        else:
            self.lookahead = 4
            # if self.path.k [self.speed_idx] >= 15 : # 속도 느린 직선구간.
            #     self.lookahead = 7
            # else:
            #     self.lookahead = 3 # 속도 느린 곡선구간 (좌회전, 우회전)

        self.select_target(self.lookahead)  # @@@@

        tmp_th = degrees(atan2((self.path.y[self.target_index] - self.cur.y), (self.path.x[self.target_index] - self.cur.x)))

        tmp_th = tmp_th % 360

        alpha = self.cur.heading - tmp_th
        if abs(alpha) > 180:
            if alpha < 0:
                alpha += 360
            else:
                alpha -= 360

        alpha = max(alpha, -90)
        alpha = min(alpha, 90)

        delta = degrees(atan2(2 * self.WB * sin(radians(alpha)) / self.lookahead, 1))

        if abs(delta) > 180:
            if delta < 0:
                delta += 360
            else:
                delta -= 360

        if abs(delta) >= 27.7:
            if delta > 0:
                return 27.7
            else:
                return -27.7
        else:

            return delta