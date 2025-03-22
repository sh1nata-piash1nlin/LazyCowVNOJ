import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('landscapes_Hw1/dog.jpeg',cv2.IMREAD_GRAYSCALE)
F = np.fft.fft2(img)
F = np.fft.fftshift(F)
M,N = img.shape
D0 = 30

u = np.arange(0,M)-M/2
v = np.arange(0,N)-N/2
[V,U] = np.meshgrid(v,u)
D = np.sqrt(np.power(U,2)+np.power(V,2))
H = np.array(D<=D0)
G = H*F
G = np.fft.ifftshift(G)
imgOut = np.real(np.fft.ifft2(G))
fig = plt.figure(dpi=300)
plt.subplot(1,2,1)

plt.imshow(img, cmap='gray')
plt.axis('off')
plt.title('Input image')

plt.subplot(1,2,2)

plt.imshow(imgOut, cmap='gray')

plt.axis('off')

plt.title('Output image')
plt.show()