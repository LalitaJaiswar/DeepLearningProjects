import cv2
import math
count = 0
videoFile = "C:/Users/csc28032018h/Desktop/Courses/deep_learning_he/Dataset/Test Tom and Jerry.mp4"
cap = cv2.VideoCapture(videoFile)   # capturing the video from the given path
frameRate = cap.get(5) #frame rate
x=1
while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % math.floor(frameRate) == 0):
        filename ="test%d.jpg" % count;count+=1
        cv2.imwrite('C:/Users/csc28032018h/Desktop/Courses/deep_learning_he/Dataset/Test_Img/'+filename, frame)
cap.release()
print ("Done!")