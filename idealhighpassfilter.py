# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# img = cv2.imread('landscapes_Hw1/dog.jpeg', cv2.IMREAD_COLOR)
# img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# M, N = img.shape[:2]
# D0 = 30
# u = np.arange(0, M) - M/2
# v = np.arange(0, N) - N/2
# [V, U] = np.meshgrid(v, u)
# D = np.sqrt(U**2 + V**2)
# H = np.array(D > D0)
# channels = cv2.split(img_rgb)
# filtered_channels = []
# for ch in channels:
#     F = np.fft.fft2(ch)
#     F_shifted = np.fft.fftshift(F)
#     G = H * F_shifted
#     G_ishift = np.fft.ifftshift(G)
#     ch_filtered = np.real(np.fft.ifft2(G_ishift))
#     filtered_channels.append(ch_filtered)
# filtered_img = cv2.merge(filtered_channels)
# fig = plt.figure(dpi=300)
# plt.subplot(1, 2, 1)
# plt.imshow(img_rgb)
# plt.axis('off')
# plt.title('Input Image')
# plt.subplot(1, 2, 2)
# plt.imshow(np.uint8(filtered_img))
# plt.axis('off')
# plt.title('Output Image (Ideal HPF)')
# plt.show()

# When you compute the FFT of an image, the zero frequency (DC component) is positioned at the top-left corner.
# Using np.fft.fftshift rearranges the FFT output so that the zero frequency is at the center.
# This makes it easier to apply symmetric filters.
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('landscapes_Hw1/dog.jpeg', cv2.IMREAD_GRAYSCALE)

F = np.fft.fft2(img)
F = np.fft.fftshift(F)
M, N = img.shape
D0 = 30
u = np.arange(0, M)-M/2
v = np.arange(0, N)-N/2
[V, U] = np.meshgrid(v, u)
D = np.sqrt(np.power(U, 2) + np.power(V, 2))
H = np.array(D > D0)
G = H * F
G = np.fft.ifftshift(G)
imgOut = np.real(np.fft.ifft2(G))

fig = plt.figure(dpi=300)
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.title('Input Image')

plt.subplot(1, 2, 2)
plt.imshow(imgOut, cmap='gray')
plt.axis('off')
plt.title('Output Image (Ideal HPF)')

plt.show()
