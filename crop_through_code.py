import cv2
import numpy as np
import pandas as pd

data = pd.read_csv('C:/Users/csc28032018h/Desktop/Project/Dataset/Training_Class0_Crop.csv')
c=0
for img_name in data.ImageId:
	img = cv2.imread('C:/Users/csc28032018h/Desktop/Project/Dataset/class0/' + img_name)
	#print(img
	if(img.shape[1]==1080):
		#print(img.shape)
		img=img[745:1920,0:1080]
		cv2.imwrite('C:/Users/csc28032018h/Desktop/Project/Dataset/Class0_/'+img_name,img)
		c+=1
print(c)	  
	  
