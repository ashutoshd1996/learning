import cv2 as cv
from cv2 import INTER_CUBIC

img = cv.imread('Data/Photos/park.jpg')
cv.imshow('Park', img)

# converting image to graycale 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Cat_grey', gray)

# blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

# Edge Detector 
canny  = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow('Dilated Edges', dilated)

# Eroding  the image
eroded = cv.erode(dilated, (7,7), iterations=3)
# cv.imshow('eroded', eroded)

# Resizing
resize = cv.resize(img, (500, 500),interpolation=cv.INTER_AREA)
# cv.imshow('resized', resize)

# Cropping 
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)
cv.waitKey(0)