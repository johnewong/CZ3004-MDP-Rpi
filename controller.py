import serial
from time import sleep


class STMControl:

    def __init__(self):
        port = '/dev/ttyS0'
        baud_rate = 115200
        self.serial_port = port
        self.baud_rate = baud_rate
        self.control = None

    def connect(self):
        try:
            self.control = serial.Serial(self.serial_port, self.baud_rate, timeout=0.1)
            print("initialize STMController successful")

        except Exception:
            print("initialize STMController failed")

    def write(self, message):
        sleep(1)
        cmd = int(message)
        if cmd == 90:
            self.clockwise_90()
        elif cmd == -90:  
            self.anticlockwise_90()
        elif cmd > 0:
            self.forward(cmd)
        else :
            self.backward(cmd)       
        
        sleep(1)

    def circle(self):
        self.clockwise_90()
        self.reset() 
        self.forward_1()
        self.anticlockwise_90()
        self.forward_2()
        self.anticlockwise_90()
        self.forward_3()
        self.anticlockwise_90()
        self.reset()
        self.forward_3()
        self.anticlockwise_90()
    
    def circle1(self):
        self.clockwise_90()
        sleep(0.5)
        self.forward_1()
        sleep(0.5)
        self.anticlockwise_90()
        sleep(0.5)
        self.forward_1()
        sleep(1)
        self.forward_1()
        self.anticlockwise_90()
        sleep(0.5)
        self.forward_1()
        sleep(1)
        self.forward_1()
        sleep(0.5)
        self.anticlockwise_90()
        sleep(0.5)        
        self.forward_1()
        sleep(1)
        self.forward_1()
        sleep(0.5)

    def circle2(self):
        print("it is a bull eyes!")
        self.clockwise_90()
        sleep(0.5)
        self.forward_2()
        sleep(0.5)
        self.anticlockwise_90()
        sleep(0.5)
        self.anticlockwise_90()
        sleep(0.5)
    
    def circle3(self):
        self.clockwise_90()
        sleep(0.5)
        self.forward_2()
        sleep(0.5)
        self.anticlockwise_90()
        sleep(0.5)
        self.anticlockwise_90()
        sleep(0.5)
        print("it is a bull eyes!")
        self.clockwise_90()
        sleep(0.5)
        self.forward_2()
        sleep(0.5)
        self.anticlockwise_90()
        sleep(0.5)
        self.anticlockwise_90()
        sleep(0.5)

    def circle4(self):
        self.clockwise_90()
        sleep(0.5)
        self.forward_2()
        sleep(0.5)
        self.anticlockwise_90()
        sleep(0.5)
        self.anticlockwise_90()
        sleep(0.5)
        print("it is a bull eyes!")
        self.clockwise_90()
        sleep(0.5)
        self.forward_2()
        sleep(0.5)
        self.anticlockwise_90()
        sleep(0.5)
        self.anticlockwise_90()
        sleep(0.5)
        print("it is a bull eyes!")
        self.clockwise_90()
        sleep(0.5)
        self.forward_2()
        sleep(0.5)
        self.anticlockwise_90()
        sleep(0.5)
        self.anticlockwise_90()
        sleep(0.5)

    def test(self):
        self.forward_1()
        sleep(0.1)
        self.clockwise_90()
        sleep(0.1)
        self.forward_5()
        sleep(0.1)
        self.anticlockwise_90()
        sleep(0.1)
        self.forward_4()    

        print("test")

    def anticlockwise_90(self):
        self.anticlockwise_90_1()
        self.anticlockwise_90_2()
        self.anticlockwise_90_1()
        self.anticlockwise_90_2()
        self.anticlockwise_90_1()
        self.anticlockwise_90_2()
        self.anticlockwise_90_1()
        self.anticlockwise_90_2()

    def clockwise_90(self):
        self.clockwise_90_1()
        self.clockwise_90_2()
        self.clockwise_90_1()
        self.clockwise_90_2()
        self.clockwise_90_1()
        self.clockwise_90_2()
        self.clockwise_90_1()
        self.clockwise_90_2()

    def anticlockwise_90_1(self):
        msg1 = bytearray([0x5a, 0x0c, 0x01, 0x01, 0x00, 0x64,
                        0x00, 0x00, 0x03, 0xe8, 0x00, 0xff])       
        count = 0
        while (count < 2):
            self.control.write(msg1)
            sleep(0.5)
            count = count+1
        sleep(0.5)    
        print("anticlockwise 90 1")

    def anticlockwise_90_2(self):        
        msg2 = bytearray([0x5a, 0x0c, 0x01, 0x01, 0xff, 0x88,
                        0x00, 0x00, 0x03, 0xe8, 0x00, 0xff])
            
        count2 = 0
        while (count2 < 2):
            self.control.write(msg2)
            sleep(0.4)
            count2 = count2+1

        print("anticlockwise 90 2")


    def clockwise_90_1(self):
        msg1 = bytearray([0x5a, 0x0c, 0x01, 0x01, 0x00, 0x64,
                        0x00, 0x00, 0xfc, 0x18, 0x00, 0xff])       
        count = 0
        while (count < 2):
            self.control.write(msg1)
            sleep(0.5)
            count = count+1
        sleep(0.5)    
        print("clockwise 90 1")

    def clockwise_90_2(self):        
        msg2 = bytearray([0x5a, 0x0c, 0x01, 0x01, 0xff, 0x88,
                        0x00, 0x00, 0xfc, 0x18, 0x00, 0xff])
            
        count2 = 0
        while (count2 < 2):
            self.control.write(msg2)
            sleep(0.4)
            count2 = count2+1

        print("clockwise 90 2")    

    def forward(self, distance):
        if distance == 1:
            self.forward_1()
        if distance == 2:
            self.forward_2()
        if distance == 3:
            self.forward_3()
        if distance == 4:
            self.forward_4()
        if distance == 5:
            self.forward_5()
        if distance == 6:
            self.forward_6()
        if distance == 7:
            self.forward_7()
        if distance == 8:
            self.forward_8()
        if distance == 9:
            self.forward_9()
        if distance == 10:
            self.forward_10()
        if distance == 11:
            self.forward_10()
            self.forward_1()
        if distance == 12:
            self.forward_10()
            self.forward_2()
        if distance == 13:
            self.forward_10()
            self.forward_3()
        if distance == 14:
            self.forward_10()
            self.forward_4()
        if distance == 15:
            self.forward_10()
            self.forward_5()
        if distance == 16:
            self.forward_10()
            self.forward_6()
        if distance == 17:
            self.forward_10()
            self.forward_7()
        if distance == 18:
            self.forward_10()
            self.forward_8()
        if distance == 19:
            self.forward_10()
            self.forward_9()
        if distance == 20:
            self.forward_10()
            self.forward_10()

    def backward(self, distance):
        if distance == -1:
            self.backward_1()
        if distance == -2:
            self.backward_2()
        if distance == -3:
            self.backward_3()

        if distance < -3:
            for i in range(distance):
                self.backward_1()
                sleep(0.5)

    def left(self, degree):
        if degree == 1:
            self.left_90()
            self.reset()
        if degree == 2:
            self.left_180()
            self.reset()
        if degree == 3:
            self.left_270()
            self.reset()
        if degree == 4:
            self.left_360()
            self.reset()
        if degree == 0:
            self.anticlockwise_90()

    def right(self, degree):
        if degree == 1:
            self.right_90()
            self.reset()
        if degree == 2:
            self.right_180()
            self.reset()
        if degree == 3:
            self.right_270()
            self.reset()
        if degree == 4:
            self.right_360()
            self.reset()
        if degree == 5:
            self.right_30()
            self.reset()
        if degree == 0:
            self.clockwise_90()
        if degree == -1:
            self.test()
        if degree == -2:
            self.circle()
            
        
            

    def around(self, distance):
        # self.forward(distance)
        # self.reset()
        self.right_30()
        self.forward_3()
        # self.reset()
        self.left_300()
        self.reset()
        self.right_30()

    def forward_1(self):
        msg = bytearray([0x5a, 0x0c, 0x01, 0x01, 0x00, 0x92,
                        0x00, 0x00, 0x00, 0x00, 0x00, 0xff])
        count = 0
        while (count < 2):
            self.control.write(msg)
            sleep(1)
            count = count+1
        print("forward 10cm")

    def backward_1(self):
        msg = bytearray([0x5a, 0x0c, 0x01, 0x01, 0xff, 0x6e,
                        0x00, 0x00, 0x00, 0x00, 0x00, 0xff])
        count = 0
        while (count < 2):
            self.control.write(msg)
            sleep(1)
            count = count+1
        print("backward 10cm")

    def forward_2(self):
        msg = bytearray([0x5a, 0x0c, 0x01, 0x01, 0x00, 0xfa,
                        0x00, 0x00, 0x00, 0x00, 0x00, 0xff])
        count = 0
        while (count < 2):
            self.control.write(msg)
            sleep(1)
            count = count+1
        print("forward 20cm")

    def backward_2(self):
        msg = bytearray([0x5a, 0x0c, 0x01, 0x01, 0xff, 0x06,
                        0x00, 0x00, 0x00, 0x00, 0x00, 0xff])
        count = 0
        while (count < 2):
            self.control.write(msg)
            sleep(1)
            count = count+1
        print("backward 20cm")

    def forward_3(self):
        msg = bytearray([0x5a, 0x0c, 0x01, 0x01, 0x01, 0x90,
                        0x00, 0x00, 0x00, 0x00, 0x00, 0xff])
        count = 0
        while (count < 2):
            self.control.write(msg)
            sleep(1)
            count = count+1
        print("forward 30cm")

    def forward_4(self):
        msg = bytearray([0x5a, 0x0c, 0x01, 0x01, 0x01, 0x70,
                        0x00, 0x00, 0x00, 0x00, 0x00, 0xff])
        count = 0
        while (count < 6):
            self.control.write(msg)
            sleep(0.5)
            count = count+1
        print("forward 40cm")

    def forward_5(self):
        msg = bytearray([0x5a, 0x0c, 0x01, 0x01, 0x01, 0xA0,
                        0x00, 0x00, 0x00, 0x00, 0x00, 0xff])
        count = 0
        while (count < 6):
            self.control.write(msg)
            sleep(0.5)
            count = count+1
        print("forward 50cm")

    def forward_6(self):
        msg = bytearray([0x5a, 0x0c, 0x01, 0x01, 0x01, 0x90,
                        0x00, 0x00, 0x00, 0x00, 0x00, 0xff])
        count = 0
        while (count < 7):
            self.control.write(msg)
            sleep(0.5)
            count = count+1
        print("forward 60cm")

    def forward_7(self):
        msg = bytearray([0x5a, 0x0c, 0x01, 0x01, 0x01, 0xa0,
                        0x00, 0x00, 0x00, 0x00, 0x00, 0xff])
        count = 0
        while (count < 7):
            self.control.write(msg)
            sleep(0.5)
            count = count+1
        print("forward 70cm")

    def forward_8(self):
        msg = bytearray([0x5a, 0x0c, 0x01, 0x01, 0x01, 0x90,
                        0x00, 0x00, 0x00, 0x00, 0x00, 0xff])
        count = 0
        while (count < 8):
            self.control.write(msg)
            sleep(0.5)
            count = count+1
        print("forward 80cm")

    def forward_9(self):
        msg = bytearray([0x5a, 0x0c, 0x01, 0x01, 0x01, 0xb0,
                        0x00, 0x00, 0x00, 0x00, 0x00, 0xff])
        count = 0
        while (count < 8):
            self.control.write(msg)
            sleep(0.5)
            count = count+1
        print("forward 90cm")

    def forward_10(self):
        msg = bytearray([0x5a, 0x0c, 0x01, 0x01, 0x01, 0x90,
                        0x00, 0x00, 0x00, 0x00, 0x00, 0xff])
        count = 0
        while (count < 9):
            self.control.write(msg)
            sleep(0.5)
            count = count+1
        print("forward 100cm")

    def backward_3(self):
        msg = bytearray([0x5a, 0x0c, 0x01, 0x01, 0xfe, 0x70,
                        0x00, 0x00, 0x00, 0x00, 0x00, 0xff])
        count = 0
        while (count < 2):
            self.control.write(msg)
            sleep(1)
            count = count+1
        print("backward 30cm")

    def right_30(self):
        msg = bytearray([0x5a, 0x0c, 0x01, 0x01, 0x01, 0x90,
                        0x00, 0x00, 0xfc, 0x18, 0x00, 0xff])
        count = 0
        while (count < 2):
            self.control.write(msg)
            sleep(1)
            count = count+1

        print("right 30")

    def right_90(self):
        msg = bytearray([0x5a, 0x0c, 0x01, 0x01, 0x01, 0x90,
                        0x00, 0x00, 0xfc, 0x18, 0x00, 0xff])

        count = 0
        while (count < 4):
            self.control.write(msg)
            sleep(1)
            count = count+1
        print("right 90")

    def right_180(self):
        msg = bytearray([0x5a, 0x0c, 0x01, 0x01, 0x01, 0x90,
                        0x00, 0x00, 0xfc, 0x18, 0x00, 0xff])

        count = 0
        while (count < 6):
            self.control.write(msg)
            sleep(1)
            count = count+1
        print("right 180")

    def right_270(self):
        msg = bytearray([0x5a, 0x0c, 0x01, 0x01, 0x01, 0x90,
                        0x00, 0x00, 0xfc, 0x18, 0x00, 0xff])

        count = 0
        while (count < 10):
            self.control.write(msg)
            sleep(1)
            count = count+1
        print("right 270")

    def right_360(self):
        msg = bytearray([0x5a, 0x0c, 0x01, 0x01, 0x01, 0x90,
                        0x00, 0x00, 0xfc, 0x18, 0x00, 0xff])

        count = 0
        while (count < 13):
            self.control.write(msg)
            sleep(1)
            count = count+1
        print("right 360")

    def left_90(self):
        msg = bytearray([0x5a, 0x0c, 0x01, 0x01, 0x01, 0x90,
                        0x00, 0x00, 0x03, 0xE8, 0x00, 0xff])
        count = 0
        while (count < 4):
            self.control.write(msg)
            sleep(1)
            count = count+1
        print("left 90")

    def left_180(self):
        msg = bytearray([0x5a, 0x0c, 0x01, 0x01, 0x01, 0x90,
                        0x00, 0x00, 0x03, 0xE8, 0x00, 0xff])
        count = 0
        while (count < 6):
            self.control.write(msg)
            sleep(1)
            count = count+1
        print("left 180")

    def left_270(self):
        msg = bytearray([0x5a, 0x0c, 0x01, 0x01, 0x01, 0x90,
                        0x00, 0x00, 0x03, 0xE8, 0x00, 0xff])
        count = 0
        while (count < 10):
            self.control.write(msg)
            sleep(1)
            count = count+1
        print("left 270")

    def left_300(self):
        msg = bytearray([0x5a, 0x0c, 0x01, 0x01, 0x01, 0x90,
                        0x00, 0x00, 0x03, 0x54, 0x00, 0xff])
        count = 0
        while (count < 11):
            self.control.write(msg)
            sleep(1)
            count = count+1
        print("left 300")

    def left_360(self):
        msg = bytearray([0x5a, 0x0c, 0x01, 0x01, 0x01, 0x90,
                        0x00, 0x00, 0x03, 0xE8, 0x00, 0xff])
        count = 0
        while (count < 13):
            self.control.write(msg)
            sleep(1)
            count = count+1
        print("left 360")

    def reset(self):
        msg = bytearray([0x5a, 0x0c, 0x01, 0x01, 0x00, 0x00,
                        0x00, 0x00, 0x00, 0x00, 0x00, 0xff])
        count = 0
        while (count < 2):
            self.control.write(msg)
            sleep(1)
            count = count+1

        print("reset")
