import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread("D:\\AKTU Internship\\input\\main.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
kernel=np.array([[0,1,0],[1,-4,1],[0,1,0]])
edge=cv2.filter2D(gray,-1,kernel)
cv2.imshow('EDGES',edge)
cv2.waitKey(0)