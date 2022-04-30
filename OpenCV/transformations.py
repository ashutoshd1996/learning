from gettext import translation
import cv2 as cv
from cv2 import resize
import numpy as np

img = cv.imread('Data/Photos/park.jpg') # Reading images 

cv.imshow('park', img) #Displaying images 

# translation
def translate(img, x, y):
    trans_mat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, trans_mat, dimensions)
    # -X --> Left
    # -Y --> Up
    # X --> Right
    # Y --> Down

translated = translate(img, 100, 100)
cv.imshow('translated', translated)

# rotation 
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None :
        rotPoint = (width/2, height/2)
    rotMAt = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMAt, dimensions)
rotated = rotate(img, 45)
cv.imshow('rotated', rotated)

# flipping
flip =cv.flip(img, -1)
# 0 = vertically 
# 1 = horizontally, 
# -1 = both horizontally and vertically 
cv.imshow('flip', flip)

cv.waitKey(0)
