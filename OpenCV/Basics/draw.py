import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype=np.uint8)
# cv.imread('Data/Photos/Cat')
# cv.imshow('Cat', img)

# 1. Painting the image
# cv.imshow('Blank', blank)
# blank[200:300, 300:400] = 0,255,0 
# cv.imshow('green', blank)  


# 2. Drawing a rectangle 
cv.rectangle(blank, (0,0),(250,250), (255,255,0), thickness=2)
# cv.imshow('Rectangle', blank)

# 3. Drawing a circle 
cv.circle(blank, (250,250), 40, (0,0,255), thickness=-1)
# cv.imshow('Circle', blank)

# 4. Drawing a line 
cv.line(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (255,255,255), thickness=3)
# cv.imshow('Line', blank)

# 5. Putting Text on an image 
cv.putText(blank, 'hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)
cv.waitKey(0)

