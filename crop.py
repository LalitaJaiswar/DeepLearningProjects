#Cropping an image
import numpy as np
import cv2

main_img=cv2.imread('main.jpg')
cropped=main_img[20:100,20:200].copy();
cv2.imshow('Cropped',cropped)
cv2.imwrite('new1.jpg',cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()