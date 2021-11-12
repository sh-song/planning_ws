from new_gigacha.msg import Path
import sys
import rospy
from new_gigacha.srv import *

def global_map_client(where, name):
   rospy.wait_for_service('global_map')
   try:
        global_map = rospy.ServiceProxy('global_map', GlobalMap)
        response = global_map(where, name)
        return response.path
   except rospy.ServiceException as e:
        print(f"Service call failed: {e}")
   

# result = global_map_client('kcity', 'final')
# print(type(result.x))