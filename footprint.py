import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('landscapes_Hw1/footprint.png', cv2.IMREAD_GRAYSCALE)
img_bin = img.copy()
kernel = np.ones((2, 2), dtype=np.uint8)

img_eroded = cv2.erode(img_bin, kernel, iterations=1)

img_opened = cv2.dilate(img_eroded, kernel, iterations=1)

img_dilated_open = cv2.dilate(img_opened, kernel, iterations=1)

img_closed = cv2.erode(img_dilated_open, kernel, iterations=1)

plt.figure(figsize=(10, 6), dpi=100)

plt.subplot(2, 3, 1)
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(img_eroded, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(img_opened, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(img_dilated_open, cmap='gray')
plt.axis('off')

# (f) Closing of the result
plt.subplot(2, 3, 6)
plt.imshow(img_closed, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
