import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('landscapes_Hw1/f95.png', 0)
_, imB = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
kernel = np.ones((11,11), np.uint8)
kernel1 = np.ones((5,5), np.uint8)
kernel2 = np.ones((69,69), np.uint8)
kernelC = np.ones((30, 30), np.uint8)
imErode = cv2.erode(imB, kernel, iterations=1)
imOpen = cv2.dilate(imErode, kernel, iterations=1)

imgC = cv2.morphologyEx(imOpen, cv2.MORPH_OPEN, kernelC)
imgCC = cv2.dilate(imgC, kernel1, iterations=1)

imgD = cv2.morphologyEx(imOpen, cv2.MORPH_OPEN, kernel2)


imDilate = cv2.dilate(imOpen, kernel, iterations=1)
imgOpen2 = cv2.dilate(imErode, kernel1, iterations=1)
imgDilate2 = cv2.dilate(imgOpen2, kernel1, iterations=1)
imClose = cv2.erode(imgDilate2, kernel1, iterations=1)

imClose2 = cv2.erode(imgDilate2, kernel2, iterations=1)

plt.subplot(2,2,1)
plt.imshow(imB, cmap='gray')
plt.axis('off')
plt.title('Original')

plt.subplot(2,2,2)
plt.imshow(imOpen, cmap='gray')
plt.axis('off')


plt.subplot(2,2,3)
plt.imshow(imgCC, cmap='gray')
plt.axis('off')


# Change this from (2,2,3) to (2,2,4)
plt.subplot(2,2,4)
plt.imshow(imgD, cmap='gray')
plt.axis('off')


plt.tight_layout()
plt.show()
