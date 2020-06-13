from PIL import Image
import numpy as np
import os
from glob import glob
import pandas as pd
import cv2
from matplotlib import pyplot as plt
from PIL import Image

data = pd.read_csv('C:/Users/csc28032018h/Desktop/AKTU Internship/Codes/flipped.csv')
directoryPath  = "C:/Users/csc28032018h/Desktop/No pedstrain/flipped/*." 
fileExtensions = [ "jpg", "jpeg", "png" ]
files    = []
for extension in fileExtensions:
    files.extend( glob( directoryPath+extension))
i=0	
for myFile in files:
    image= Image.open(myFile)
    #print(myFile)
    if image is not None:
        rotated_image = image.transpose(Image.FLIP_LEFT_RIGHT)
        rotated_image.save(myFile)
    else:
        print(myFile)