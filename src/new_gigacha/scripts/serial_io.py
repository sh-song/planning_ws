
from utils.sig_int_handler import Activate_Signal_Interrupt_Handler
import serial
from new_gigacha.msg import Serial_Info
import threading
import struct

import rospy


class Serial_IO:
    def __init__(self):
        # Serial Connect
        self.ser = serial.Serial("/dev/ttyUSB0", 115200)

        # ROS Publish
        rospy.init_node("Serial_IO", anonymous=False)
        self.serial_pub = rospy.Publisher("/serial", Serial_Info, queue_size=1)


        # Messages/Data
        self.serial_msg = Serial_Info()  # Message to publish
        self.serial_data = []
        self.alive = 0


        # Serial Read Thread
        th_serialRead = threading.Thread(target=self.serialRead)
        th_serialRead.daemon = True
        th_serialRead.start()

        # Main Loop
        rate = rospy.Rate(20)
        while not rospy.is_shutdown():
            # print("----------loop!")

            # self.serialWrite()
            rate.sleep()


    def serialRead(self):
        while True:
            packet = self.ser.read_until(b'\x0d\x0a')
            if len(packet) == 18:
                header = packet[0:3].decode()

                if header == "STX":
                    #auto_manual, e-stop, gear
                    (self.serial_msg.auto_manual,
                    self.serial_msg.emergency_stop,
                    self.serial_msg.gear) \
                    = struct.unpack("BBB", packet[3:6])
                    
                    #speed, steer
                    tmp1, tmp2 = struct.unpack("2h", packet[6:10])
                    self.serial_msg.speed = tmp1 / 10  # km/h
                    self.serial_msg.steer = -tmp2 / 71  # degree

                    #brake
                    self.serial_msg.brake = struct.unpack("B", packet[10:11])[0]

                    #encoder -- not working
                    # self.serial_msg.encoder = struct.unpack("f", packet[11:15])
                    self.serial_msg.encoder = -1

                    #alive (heartbeat)
                    self.alive = struct.unpack("B", packet[15:16])[0]

                    self.serial_pub.publish(self.serial_msg)


if __name__ == "__main__":
    Activate_Signal_Interrupt_Handler()

    erp = Serial_IO()