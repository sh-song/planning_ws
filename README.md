# 2021_gigacha_planning

## 설치법

1. 적당한 디렉토리에서 $git clone https://github.com/sh-song/planning_ws.git
2. $cd ~/다운로드경로/planning_ws
3. $catkin_make
4. gedit ~/.bashrc
5. gedit에서 맨 마지막 줄에 source ~/다운로드경로/planning_ws/devel/setup.sh 추가
6. 터미널 전부 껐다 켜기
7. /planning_ws/src/new_gigacha/scripts 디렉토리 안에 있는 파이썬 파일들 사용하면 됩니다.


## 사용법 -- 시뮬레이션
0. $cd /설치경로/planning_ws/src/new_gigacha/scripts
1. $python3 sensors_simul.py
2. $python3 localization_simul.py
3. $python3 serial_io.py
4. $python3 planner.py
5. $python3 serial_io.py
6. $rviz -d rviz_config.rviz

## 뭘 할 수 있나요?
1. 라이다, 카메라 안쓰는 모든 것 가능.
2. Global path 따라서 안정적으로 자율주행 가능.
3. 실시간 path + 차량 위치 시각화 by rviz
