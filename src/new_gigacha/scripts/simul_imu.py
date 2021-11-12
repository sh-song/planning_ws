import socket
import threading
import time
import struct
import os
from new_gigacha.msg import Local

class udp_sensor_parser :
    def __init__(self,ip,port,data_type):
        self.data_type=data_type
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        recv_address = (ip,port)
        self.sock.bind(recv_address)
        self.data_size=65535 
        self.parsed_data=[]
        thread = threading.Thread(target=self.recv_udp_data)
        thread.daemon = True 
        thread.start() 

    

    def recv_udp_data(self):
        while True :
            
            raw_data, sender = self.sock.recvfrom(self.data_size)
            self.data_parsing(raw_data)



    def data_parsing(self,raw_data) :
   

        if self.data_type=='imu' :
            header=raw_data[0:9].decode()
            
            if header == '#IMUData$' :
                data_length=struct.unpack('i',raw_data[9:13])
                imu_data=struct.unpack('10d',raw_data[25:105])
                self.parsed_data=imu_data

        
    def __del__(self):
        self.sock.close()
        print('del')

class SimulIMU():
    def __init__(self, host_ip, gps_port):
        rospy.init_node('SimulIMU', anonymous=False)
        self.pub = rospy.Publisher('/simul_imu', Local, queue_size = 1)
        self.msg = Local()
        self.imu_parser=udp_sensor_parser(host_ip, imu_port,'imu')

    def main():
        if len(imu_parser.parsed_data)==10 :
            print('------------------------------------------------------')
            print(' ori_w:{0}  ori_x {1}  ori_y {2}  ori_z {3}'.format(round(imu_parser.parsed_data[0],2),round(imu_parser.parsed_data[1],2),round(imu_parser.parsed_data[2],2),round(imu_parser.parsed_data[3],2)))
            print(' ang_vel_x :{0}  ang_vel_y : {1}  ang_vel_z : {2} '.format(round(imu_parser.parsed_data[4],2),round(imu_parser.parsed_data[5],2),round(imu_parser.parsed_data[6],2)))
            print(' lin_acc_x :{0}  lin_acc_y : {1}  lin_acc_z : {2} '.format(round(imu_parser.parsed_data[7],2),round(imu_parser.parsed_data[8],2),round(imu_parser.parsed_data[9],2)))

        #TODO Publish yaw


if __name__ == '__main__':
    
    path = os.path.dirname( os.path.abspath( __file__ ) )

    with open(os.path.join(path,("params.json")),'r') as fp :
        params = json.load(fp)

    params=params["params"]
    user_ip = params["user_ip"]
    host_ip = params["host_ip"]
    imu_port = params["imu_dst_port"]

    rate = rospy.Rate(10) #10 Hz?
    imu = SimulIMU(host_ip, imu_port)
    print("dd")
 
    while not rospy.is_shutdown():
        imu.main()
        rate.sleep()