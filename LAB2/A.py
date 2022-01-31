import cv2
import numpy as np


def additioncv(frames1,frames2,weight):
    cframe1 = frames1.copy()
    cframe2 = frames2.copy()
    cframe1[:,:,0] = cv2.add(weight[0]*cframe1[:,:,0],weight[1]*cframe2[:,:,0])
    cframe1[:,:,1] = cv2.add(weight[0]*cframe1[:,:,1],weight[1]*cframe2[:,:,1])
    cframe1[:,:,2] = cv2.add(weight[0]*cframe1[:,:,2],weight[1]*cframe2[:,:,2])

    return cframe1
            
def write_video(file_path, frames1 , frames2 , fps ,weight):
    """
    Writes frames to an mp4 video file
    :param file_path: Path to output video, must end with .mp4
    :param frames: List of PIL.Image objects
    :param fps: Desired frame rate
    """
    height, width, layers = frames1.shape
    size = (width,height)
    time = fps * 10
    writer = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 60, size)
    for i in range(0,time,1):
        #writer.write(cv2.addWeighted(frames1,(1-(i/(time//2))),frames2,(i/(time//2)),0))
        writer.write(additioncv(frames1,frames2,weight[i]))
    writer.release()

imgBGR = cv2.imread("Image.jpg")
im_rgb = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
im_hsv = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2HSV)

a = 1.0
b = 0.0
array = []
for i in range(0,300,1):
    array.append([a,b])
    a = a - 0.0033333
    b = b + 0.0033333
array.append([0,1])

a = 0.0
b = 1.0
for i in range(0,300,1):
    array.append([a,b])
    a = a + 0.00333333
    b = b - 0.00333333
array.append([1,0])


#print(array)
write_video("lel.avi",imgBGR,im_rgb,60,array)



        