import cv2
import numpy as np
import math
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
imgBGR = cv2.imread("Image.jpg")
imgRGB = imgBGR[:, :, [2, 1, 0]]

a = [1,2,3,4,5]
a = np.arange(8).reshape(2,4);
print(a[:,[3,2,1,0]])