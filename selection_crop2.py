import cv2
import numpy as np
im=[]
r=[]
imcrp=[]
for i in range(2):
	im[i].append(cv2.imread("main.jpg"))
	'''r[i].append(cv2.selectROI(im[i],fromCenter=False,showCrosshair=False))
	print(r[i])
	imCrop[i].append(im[int(r[i][1]):int(r[i][1]+r[i][3]), int(r[i][0]):int(r[i][0]+r[i][2])])
	cv2.imshow("Image", imCrop[i])
	cv2.imwrite('output/crop.jpg',imCrop[i])
	cv2.waitKey(0)'''
cv2.destroyAllWindows()
