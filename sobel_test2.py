import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('sample.jpg',0)
sobelx = cv2.Sobel(img,cv2.CV_32F,1,0,ksize=3)
sobely = cv2.Sobel(img,cv2.CV_32F,0,1,ksize=3)
mag, angle = cv2.cartToPolar(sobelx, sobely, angleInDegrees=True)
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), 
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(mag,cmap = 'gray')
plt.title('Mag'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()