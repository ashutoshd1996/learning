import cv2 as cv
import numpy as np

img = cv.imread('Data/Photos/cats.jpg')
cv.imshow('Cat', img) 

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray) 

blank = np.zeros(img.shape, dtype=np.uint8)

blur = cv.blur(img, (5,5), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 125, 175)
cv.imshow('canny', canny)

ret, thresh  = cv.threshold(gray, 125, 255,  cv.THRESH_BINARY)

# cv.imshow('Thresh', thresh)
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('blank', blank)
cv.waitKey(0) 