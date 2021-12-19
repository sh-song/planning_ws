import rospy
from new_gigacha.srv import *
from new_gigacha.msg import Path
import csv
from numpy import rad2deg

def make_global_map(req):
    print(f"Making Global Path from {req.where}/{req.name}.csv")
    global_path = Path()
    try:
        with open("map/" + req.where + "/" + req.name + ".csv", mode="r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                global_path.x.append(float(line[0]))
                global_path.y.append(float(line[1]))
                deg_yaw=(rad2deg(float(line[2]))+360) % 360
                global_path.heading.append(deg_yaw)
                global_path.k.append(float(line[3]))
                global_path.env.append(line[5])
                global_path.mission.append(line[6])
        return GlobalMapResponse(global_path)
    except:
        print('Error: Execute $rosrun in directory \'new_gigacha/scripts\'')

def global_map_server():
    rospy.init_node('global_map_server')
    s = rospy.Service('global_map', GlobalMap, make_global_map)
    print("Ready to Make Global Map.")
    rospy.spin()

if __name__ == "__main__":
    global_map_server()