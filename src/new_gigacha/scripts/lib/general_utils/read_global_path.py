import rospy
from new_gigacha.msg import Path
import csv
from numpy import rad2deg

def read_global_path(where, name):
        print(f"Making Global Path from {where}/{name}.csv")
        global_path = Path()
        with open("map/" + where + "/" + name + ".csv", mode="r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                global_path.x.append(float(line[0]))
                global_path.y.append(float(line[1]))
                deg_yaw=(rad2deg(float(line[2]))+360) % 360
                global_path.heading.append(deg_yaw)
                global_path.k.append(float(line[3]))
                # global_path.env.append(line[5])
                # global_path.mission.append(line[6])
        return global_path