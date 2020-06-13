import numpy as np
import os
from glob import glob
import cv2

directoryPath  = "C:/Users/csc28032018h/Desktop/No pedstrain/*." 
fileExtensions = [ "jpg", "jpeg", "png" ]
files    = []
for extension in fileExtensions:
    files.extend( glob( directoryPath + extension ))
i=1
for myFile in files:
	image=cv2.imread(myFile)
	print('for file:'+myFile)
	if image is not None:
		h,w=image.shape[:2]
		if(w>1280 or h>800):
			w=int(w*(.5))
			h=int(h*(.5))
			image=cv2.resize(image,(w,h))
			print('resise'+str(i)+myFile)	
		r=cv2.selectROI(image,fromCenter=False,showCrosshair=False)
		#checking if 'c' has pressed
		if(r[0]!=0 and r[1]!=0 and r[2]!=0 and r[3]!=0):
			imCrop=image[int(r[1]):int(r[1]+r[3]),int(r[0]):int(r[0]+r[2])]
			cv2.imwrite('C:/Users/csc28032018h/Desktop/No pedstrain/cropped/'+str(i)+'.jpg',imCrop)
			i=i+1
		if(i==100):
			break
	cv2.destroyAllWindows()	
	#for breaking the loop
	x=input()
	if(x=='C'):
		break
