import cv2
import numpy as np
from matplotlib import pyplot as plt

imgBGR = cv2.imread("Image.jpg")
im_rgb = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
mask = np.zeros(im_rgb.shape[:2], dtype="uint8")

cv2.rectangle(mask, (0, 90), (290, 450), 255, -1)

plt.figure(figsize=(10,4))
plt.subplot(1,3,1)
plt.imshow(im_rgb)
plt.title('RGB')

plt.subplot(1,3,2)
plt.imshow(mask)
plt.title('mask')

masked = cv2.bitwise_and(im_rgb, im_rgb, mask=mask)
