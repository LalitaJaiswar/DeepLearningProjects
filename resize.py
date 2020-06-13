from PIL import Image
import cv2
from skimage.transform import resize


img = cv2.imread('crop4.jpg') # image extension *.png,*.jpg
'''new_width  = 224
new_height = 224
img = img.resize((new_width, new_height), Image.ANTIALIAS)
img.save('new1.png') # format may what u want ,*.png,*jpg,*.gif
img=cv2.imread('new1.png')
print(img.shape)'''
img = resize(img, (224,224),
                       anti_aliasing=True)
print(img.shape)					   
cv2.imshow('new1.png',img)
cv2.waitKey(0)