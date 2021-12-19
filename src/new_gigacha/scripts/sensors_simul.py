#!/usr/bin/env python3
from lib.general_utils.sig_int_handler import Activate_Signal_Interrupt_Handler
import serial #Serial USB
import socket #UDP LAN
import rospy
import os
import json
import socket
import struct
from geometry_msgs.msg import Pose
import threading

class UDP_GPS_Parser :
    def __init__(self,ip,port,data_type):
        self.type=data_type
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        recv_address = (ip,port)
        self.sock.bind(recv_address)
        self.data_size=65535 
        self.parsed_data=None


    def recv_udp_data(self):
        raw_data, sender = self.sock.recvfrom(self.data_size)
        print('2==========')

        self.data_parsing(raw_data)

    def data_parsing(self,raw_data) :
        raw_str=raw_data.decode()
        split_str=raw_str.split(",")
        header=split_str[0]
        
        if header[1:]== self.type :
            if self.type == 'GPRMC':
                latitude=int(float(split_str[3])/100)+(float(split_str[3])%100)/60
                longitude=int(float(split_str[5])/100)+(float(split_str[5])%100)/60
                self.parsed_data=[latitude,longitude]

            if self.type == 'GPGGA':
                latitude=int(float(split_str[2])/100)+(float(split_str[2])%100)/60
                longitude=int(float(split_str[4])/100)+(float(split_str[4])%100)/60
                self.parsed_data=[latitude,longitude]
       
    def get_data(self) :
        return self.parsed_data

    def __del__(self):
        self.sock.close()
        print('del')


class SimulGPS():
    def __init__(self, host_ip, gps_port):
        self.pub = rospy.Publisher('/simul_gps', Pose, queue_size = 1000)
        self.msg = Pose()
        self.msg.position.z = -1 # not used

        self.gps_parser=UDP_GPS_Parser(host_ip, gps_port,'GPRMC')

    def main(self):
        
        self.gps_parser.recv_udp_data()

        if self.gps_parser.parsed_data!=None :

            self.msg.position.x = self.gps_parser.parsed_data[0] #latitude
            self.msg.position.y = self.gps_parser.parsed_data[1] #longitude
            
            self.pub.publish(self.msg)

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
        self.pub = rospy.Publisher('/simul_imu', Pose, queue_size = 1)
        self.msg = Pose()
        self.imu_parser=udp_sensor_parser(host_ip, imu_port,'imu')

    def main(self):
        if len(self.imu_parser.parsed_data)==10 :

            # print(' ang_vel_x :{0}  ang_vel_y : {1}  ang_vel_z : {2} '.format(round(self.imu_parser.parsed_data[4],2),round(self.imu_parser.parsed_data[5],2),round(self.imu_parser.parsed_data[6],2)))
            # print(' lin_acc_x :{0}  lin_acc_y : {1}  lin_acc_z : {2} '.format(round(self.imu_parser.parsed_data[7],2),round(self.imu_parser.parsed_data[8],2),round(self.imu_parser.parsed_data[9],2)))

            self.msg.orientation.w = self.imu_parser.parsed_data[0]
            self.msg.orientation.x = self.imu_parser.parsed_data[1]
            self.msg.orientation.y = self.imu_parser.parsed_data[2]
            self.msg.orientation.z = self.imu_parser.parsed_data[3]
            print(self.msg)
            self.pub.publish(self.msg)

if __name__ == '__main__':
    Activate_Signal_Interrupt_Handler()

    path = os.path.dirname( os.path.abspath( __file__ ) )
    with open(os.path.join(path,("params.json")),'r') as fp :
        params = json.load(fp)

    params=params["params"]
    user_ip = params["user_ip"]
    host_ip = params["host_ip"]
    gps_port = params["gps_dst_port"]
    imu_port = params["imu_dst_port"]

    rospy.init_node('Simul_GPS_IMU', anonymous=False)
    gps = SimulGPS(host_ip, gps_port)
    imu = SimulIMU(host_ip, imu_port)

    cnt = 0
    while not rospy.is_shutdown():
        cnt +=1 
        print(f"Simul sensors are on...{cnt}")
        print('1==========')
        gps.main()

        imu.main()
