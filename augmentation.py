# example of horizontal shift image augmentation
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator
import cv2     
import math 
import matplotlib.pyplot as plt  
import pandas as pd
from numpy import expand_dims
from keras.preprocessing import image 
import numpy as np 
from keras.utils import np_utils
from skimage.transform import resize 


data = pd.read_csv('C:/Users/csc28032018h/Desktop/AKTU Internship/Codes/test.csv')
#test = pd.read_csv('C:/Users/csc28032018h/Desktop/AKTU Internship/Codes/test.csv')

X = []
for img_name in data.Image_ID:
    img = plt.imread('C:/Users/csc28032018h/Desktop/AKTU Internship/Codes/test/' + img_name)
    X.append(img)
X = np.array(X)

'''test_image = []
test_image_name=[]
for img_name in test.Image_ID:
    img = plt.imread('C:/Users/csc28032018h/Desktop/AKTU Internship/Codes/test/' + img_name)
    test_image.append(img);
    test_image_name.append(img_name)
test_img = np.array(test_image)'''

from keras.utils import np_utils
train_y = np_utils.to_categorical(data.Class)
print(len(train_y))
#test_y = np_utils.to_categorical(test.Class)
train_datagen = ImageDataGenerator(featurewise_center=True,
    featurewise_std_normalization=True,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True)

train_generator = train_datagen.flow_from_directory(
        directory='test/',  # this is the target directory
        target_size=(224, 224),
		classes=data.Class
		)