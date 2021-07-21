
import datetime
from PIL import Image
import time, pickle, requests, threading
import os 
from picamera import PiCamera
from picamera.array import PiRGBArray

class ImageProcessor:

    def connect(self):
        self.count = 0
        self.camera = PiCamera()
        self.camera.exposure_mode = "auto"
        self.camera.resolution = (640, 480)
        self.output = PiRGBArray(self.camera)

        # start camera preview to let camera warm up
        #self.camera.start_preview()
        #threading.Thread(target=time.sleep, args=(2,)).start()
        print("connect image rec server")

    def takePic(self):
        #start_time = datetime.now()
        try:
            print("take pic func")            
            self.camera.capture(self.output, 'bgr')
            frame = self.output.array
            print("frame:{}".format(len(frame)))
            self.output.truncate(0)
            self.count += 1

            data = pickle.dumps(frame)
            print("posting server!")
            # send to Laptop via HTTP POST
            r = requests.post("http://192.168.6.24:8123", data=data) #static IP
            #print('Time taken to take picture: ' + str(datetime.now() - start_time) + 'seconds')
            print("response text:{}".format(r.text))
            if r.status_code == 200:
                image_data = r.text
                image_arr = image_data.split(":")
                return image_arr[0]                   

            return 0

        except Exception as error:
                print('take pic failed: ' + str(error))

        finally:
                self.camera.close()

        

    def takePicLocal(self):
        print("takePicLocal")
        os.system("raspistill -o Desktop/image.jpg -w 640 -h 480")
        print("save image")
        jpgfile = Image.open("Desktop/image.jpg")
        print("open  image")
        data = pickle.dumps(jpgfile)
        print("dump image")

        r = requests.post("http://192.168.6.24:8123", data=data) #static IP
            #print('Time taken to take picture: ' + str(datetime.now() - start_time) + 'seconds')
        print("response text:{}".format(r.text))
        if r.status_code == 200:
            image_data = r.text
            image_arr = image_data.split(":")
            return image_arr[0]
                    