
import multiprocessing
from time import sleep
from image_processor import ImageProcessor
from communicator import MultiProcessor
from controller import STMControl

def init():
    rpi_control_queue = multiprocessing.Queue()
    image_queue = multiprocessing.Queue()

    controller = STMControl()
    controller.connect()
    image_processor = ImageProcessor()
    image_processor.connect()
    
    mp = MultiProcessor(rpi_control_queue, image_queue)
    mp.start()

    _rpi_control(rpi_control_queue,image_queue,controller,image_processor)


def _rpi_control(rpi_control_queue, image_queue, controller, image_processor):
        while True:
            try:
                if not rpi_control_queue.empty():
                    message = rpi_control_queue.get_nowait()
                    print("read from control queue {}".format(message))                    

                    if message not in ",":
                        pass

                    msgArray = message.split(",")
                    if len(msgArray) > 0:
                        if message in "AR,AN,": 
                            msg = msgArray[2]
                            if msg == "F":
                                controller.write(1)
                            if msg == "R":
                                controller.write(90)
                            if msg == "L":
                                controller.write(-90)
                            if msg == "PIC":
                                image = image_processor.takePic()
                                image_queue.put_nowait(image)

                        else:
                            for msg in msgArray:
                                print("msg: {}".format(msg))                                
                                if msg == "picture":              
                                    sleep(3)                      
                                    image_id = image_processor.takePic()
                                    image_queue.put_nowait(image_id)

                                else:    
                                    controller.write(msg)

            except Exception as error:
                print('Process _rpi_control failed: ' + str(error))
                break    
       

if __name__ == '__main__':
    init()
