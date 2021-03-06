import numpy as np
from lib.general_utils.exp_mov_avg import ExpMovAvgFilter
from master_node.msg import Local
from geometry_msgs.msg import Point32
from sensor_msgs.msg import PointCloud

from math import radians, cos, sin, hypot, pi

class Obstacle:
    dist=0
    index=0
    point=Point32()
    rad=None
    EMA=ExpMovAvgFilter(Point32())
    update=False
    cnt=0
    def __init__(self, idx, dist, ema):
        self.index=idx
        self.dist=dist
        self.EMA=ema
        self.update=True

class Mapping:
    obs_map = {} # 실제 장애물 좌표가 저장되는 dictionary
    obstacle_cnt = 0 # 현재 장애물의 개수

    def mapping(self, ego, circles, local):
        theta = radians(local.heading)
        # print(local.heading)
        for circle in circles:
            # 현재 mapping 중인 장애물 : circle
            # 장애물 절대좌표 변환
            pos = Point32()
            pos.x = circle.center.x * cos(theta) + circle.center.y * -sin(theta) + local.x
            pos.y = circle.center.x * sin(theta) + circle.center.y * cos(theta) + local.y
            id = -1

            for i, obstacle in self.obs_map.items():
                if obstacle.EMA.tracking(pos):
                    id = i
                    break

            # 만약 딕셔너리에 없으면, 새로운 이동 평균 필터 클래스 선언후 삽입
            # circle의 절대좌표 (x, y)로 초기화
            if id == -1:

                min_dist = -1
                min_index = 0
                # base_index = avoidance가 시작된 시점의 차량의 위치와 가장 가까운 global path index
                # base_index 부터 장애물과 가장 가까운 index를 탐색한다.
                # min_dist < dist인 경우, 가장 가까운 index를 지나쳤다고 판단하여 break
                end_index = min(ego.index + 150, len(ego.global_path.x) - 1)
                if end_index == len(ego.global_path.x) - 1:
                    end_index = ego.index + 150 - (len(ego.global_path.x) - 1)

                if end_index < ego.index:
                    start_index = 0
                else:
                    start_index = ego.index
                for i in range(start_index, end_index):

                    dist = hypot(ego.global_path.x[i] - pos.x, ego.global_path.y[i] - pos.y)
                    if min_dist == -1 or min_dist > dist:
                        min_dist = dist
                        min_index = i
                self.obs_map[min_index] = Obstacle(min_index, min_dist, ExpMovAvgFilter(pos))
                self.obstacle_cnt += 1

            # 있으면, 해당 key값 이동평균 필터에 circle의 절대좌표 (x, y) 삽입
            else:
                self.obs_map[id].EMA.emaFilter(pos)
                obstacle = self.obs_map[id]
                emapos = obstacle.EMA.retAvg()

                min_dist = -1
                min_index = 0
                start_index = max(0, obstacle.index - 10)
                end_index = min(obstacle.index + 10, len(ego.global_path.x) - 1)

                for i in range(start_index, end_index):
                    dist = hypot(ego.global_path.x[i] - emapos.x, ego.global_path.y[i] - emapos.y)
                    if min_dist == -1 or min_dist > dist:
                        min_dist = dist
                        min_index = i

                self.obs_map[id].index = min_index
                self.obs_map[id].dist = min_dist
                self.obs_map[id].update = True

            # 5 프레임에 동안 안나오면, 삭제
            # 단, 회피주행중일 경우 제외
        if ego.mode == "small":
            return

        for id in list(self.obs_map.keys()):
            if self.obs_map[id].update:
                self.obs_map[id].update = False
                self.obs_map[id].cnt = 0
            elif self.obs_map[id].cnt > 5:
                del self.obs_map[id]
            else:
                self.obs_map[id].cnt += 1

    def make_target_map(self, ego):
            target_map = {}

            for i, obstacle in self.obs_map.items():
                dist = obstacle.dist
                index = obstacle.index
                emapos = obstacle.EMA.retAvg()

                std_point = Point32(ego.global_path.x[index], ego.global_path.y[index], 0)
                if dist > 1.75:
                    continue

                # 경로와 가까울때는 최대 2정도의 거리만큼 떨어져서 주행
                # 경로와 멀때는 거의 0에 가까운 거리만큼 떨어져서 주행

                rad = np.arctan2(emapos.y - std_point.y, emapos.x - std_point.x)
                crossP = ego.global_path.x[index] * emapos.y - ego.global_path.y[index] * emapos.x
                # 왼쪽에 있는데, 경로 가까이 있으면
                if crossP > 0 and dist < 0.5:
                    r = dist + 1.25
                else:
                    rad += pi
                    r = max(0, -dist + 1.25)

                if obstacle.rad != None:
                    if abs(rad - obstacle.rad) > pi / 2:
                        rad = obstacle.rad
                else:
                    obstacle.rad = rad
                point = Point32()
                point.x = std_point.x + (r * cos(rad))
                point.y = std_point.y + (r * sin(rad))
                target_map[index] = point
            return target_map
                

    # 현재 map에 저장되어있는 모든 point를 PointCloud형식으로 바꿔서 리턴하는 함수
    # 이걸 바로 rviz로 쏘고있음
    def showObstacleMap(self):
        obstacle_map = PointCloud()
        for i, obstacle in self.obs_map.items():
            obstacle_map.points.append(obstacle.EMA.retAvg())

        return obstacle_map
