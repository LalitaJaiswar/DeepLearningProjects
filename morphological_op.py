#Morphological operation on image(3-4 operations)
import cv2
import numpy as np
from matplotlib import pyplot as plt


orig_img=cv2.imread('C://Users//csc28032018h//Desktop//AKTU Internship//main.jpg')
gray_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2GRAY)
(thresh, BW_img) = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
kernel = np.ones((3,3),np.uint8)
erosion = cv2.erode(gray_img,kernel,iterations = 1)
cv2.imshow('Original Image',gray_img);
cv2.imshow('Erosion',erosion);
cv2.waitKey(0)
cv2.destroyAllWindows()

