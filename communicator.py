import multiprocessing
import pickle
import time
import requests
from picamera import PiCamera
from picamera.array import PiRGBArray
from datetime import datetime
from controller import STMControl
from bluetooth_processor import BluetoothProcessor
from image_processor import ImageProcessor
from multiprocessing import Process, Value, Queue, Manager

class MultiProcessor:
    def __init__(self, rpi_control_queue: multiprocessing.Queue, image_queue: multiprocessing.Queue):
        print('Initializing Multi-processor')
        
        self.controller = STMControl()
        self.bluetooth_processor = BluetoothProcessor()      
        
        self.rpi_control_queue = rpi_control_queue
        self.image_queue = image_queue

        self.read_bluetooth_process = Process(target=self._read_bluetooth)
        # self.rpi_control_process = Process(target=self._rpi_control)
        self.image_process = Process(target=self._send_image)        

    def start(self):     
        try:
            self.controller.connect()
            self.bluetooth_processor.connect()
            
            self.read_bluetooth_process.start()
            #self.rpi_control_process.start()
            self.image_process.start()
           

        except Exception as error:
            raise error

    def _read_bluetooth(self):
        while True:
            try:
                raw_message = self.bluetooth_processor.read()
                print("raw message{}".format(raw_message))                      
                if raw_message is None:
                    continue

                message_list = raw_message.splitlines()
                for message in message_list:            
                    if len(message) <= 0:
                        continue  

                    print("put into control queue {}".format(message))                                                                            
                    self.rpi_control_queue.put_nowait(message)
                   
                    
            except Exception as error:
                print('Process read_bluetooth failed: ' + str(error))
                break   

    def _rpi_control(self):
        while True:
            try:
                if not self.rpi_control_queue.empty():
                    message = self.rpi_control_queue.get_nowait()
                    print("read from control queue {}".format(message))                                        
                                      
                    if message == "terminate":
                        self.controller.stop()
                    msgArray = message.split(",")
                    if len(msgArray) > 0:
                        if message in "AR,AN,": 
                            msg = msgArray[2]
                            if msg == "F":
                                self.controller.write(1)
                            if msg == "R":
                                self.controller.write(90)
                            if msg == "L":
                                self.controller.write(-90)
                            if msg == "PIC":
                                image = self.image_processor.takePic()
                                self.image_queue.put_nowait(image)

                        else:
                            for msg in msgArray:
                                print("msg: ".format(msg))                                
                                if msg == "picture":
                                    image_id = self.image_processor.takePic()
                                    self.image_queue.put_nowait(image_id)

                                elif msg != "":    
                                    self.controller.write(msg)

            except Exception as error:
                print('Process _rpi_control failed: ' + str(error))
                break    

    def _send_image(self):
        count = 1
        while True:
            try:
                if not self.image_queue.empty():
                    imageId = self.image_queue.get_nowait()                         
                    msg = "TT:{}:{}".format(count,imageId)
                    print(msg)
                    self.bluetooth_processor.send(msg)      
                    count = count + 1         
                    
            except Exception as error:
                print('Process send_image failed: ' + str(error))
                break   
        