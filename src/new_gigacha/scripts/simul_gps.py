#!/usr/bin/env python
import serial #Serial USB
import socket #UDP LAN
import rospy
from new_gigacha.msg import Local

import socket
import threading
import struct

class UDP_GPS_Parser :
    def __init__(self,ip,port,data_type):
        self.type=data_type
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        recv_address = (ip,port)
        self.sock.bind(recv_address)
        self.data_size=65535 
        self.parsed_data=None
        thread = threading.Thread(target=self.recv_udp_data)
        thread.daemon = True 
        thread.start() 


    def recv_udp_data(self):
        while True :
            raw_data, sender = self.sock.recvfrom(self.data_size)
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
        rospy.init_node('SimulGPS', anonymous=False)
        self.pub = rospy.Publisher('/simul_gps', Local, queue_size = 1)
        self.msg = Local()
        self.gps_parser=UDP_GPS_Parser(host_ip, gps_port,'GPRMC')

    def main(self):
        if self.gps_parser.parsed_data!=None :
            self.msg.x = gps_parser.parsed_data[0] #latitude
            self.msg.y = gps_parser.parsed_data[1] #longitude
            print(f'Lat : {self.msg.x} , Long : {self.msg.y}')
        
            self.pub.publish(msg)



if __name__ == '__main__':
    
    path = os.path.dirname( os.path.abspath( __file__ ) )

    with open(os.path.join(path,("params.json")),'r') as fp :
        params = json.load(fp)

    params=params["params"]
    user_ip = params["user_ip"]
    host_ip = params["host_ip"]
    gps_port = params["gps_dst_port"]

    rate = rospy.Rate(10) #10 Hz
    gps = SimulGPS(host_ip, gps_port)
    print("dd")
 
    while not rospy.is_shutdown():

        gps.main()
        rate.sleep()