import socket
import time
from imutils.video import VideoStream
import imagezmq
  
sender = imagezmq.ImageSender(connect_to='tcp://192.168.43.143:12345') #
  
rpi_name = socket.gethostname() # send RPi hostname with each image
picam = VideoStream(usePiCamera=True,resolution=(1088,592)).start()
time.sleep(0.5)  # allow camera sensor to warm up
while True:
        image = picam.read()
        sender.send_image(rpi_name, image)
