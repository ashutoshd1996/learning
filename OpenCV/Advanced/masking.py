import cv2 as cv
import numpy as np

img = cv.imread('Data/Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow('Blank', blank)

rectangle = cv.rectangle(blank.copy(),(30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

weird = cv.bitwise_and(circle, rectangle)
# cv.imshow('mask', weird)

masked = cv.bitwise_and(img, img, mask = weird)
cv.imshow('Weird shaped masked image', masked)

cv.waitKey(0)