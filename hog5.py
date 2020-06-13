import cv2
import matplotlib.pyplot as plt
from skimage.feature import hog
from skimage import data, color, exposure
import numpy as np

main_image = cv2.imread("main.jpg",0)
temp=cv2.imread('template.jpg',0)
fd, image = hog(main_image, orientations=8, pixels_per_cell=(16, 16),
                    cells_per_block=(1, 1),block_norm='L2', visualize=True)
#hog_image_rescaled = exposure.rescale_intensity(image, in_range=(0,10))
'''plt.subplot(1,2,1)
plt.imshow(image,cmap = 'gray')
plt.title('Original'), 
plt.xticks([]), plt.yticks([])

plt.subplot(1,2,2)
plt.imshow(hog_image_rescaled,cmap = 'gray')
plt.title('HOG of image'), 
plt.xticks([]), plt.yticks([])

plt.show()'''
w,h=temp.shape[::-1]
res = cv2.matchTemplate(image,temp,cv2.TM_CCOEFF_NORMED) 
threshold = 0.4
loc = np.where( res >= threshold)  
print(loc)
for pt in zip(*loc[::-1]): 
    cv2.rectangle(main_image, pt, (pt[0] + w, pt[1] + h), (255,255,255), 1) 
cv2.imshow('Detected',main_image)
cv2.waitKey(0)
cv2.destroyAllWindows()