#Displaying different types pf images+histogram of image
import cv2
from matplotlib import pyplot as plt

orig_img=cv2.imread('test.png')
cv2.imshow('R Image',orig_img[:,:,0])
cv2.imshow('G Image',orig_img[:,:,1])
cv2.imshow('B Image',orig_img[:,:,2])
plt.hist(orig_img.ravel(),256,[0,255]);
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
