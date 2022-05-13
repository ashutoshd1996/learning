import cv2 as cv
from cv2 import CascadeClassifier

img = cv.imread('Data/Photos/lady.jpg')
# cv.imshow('Person', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
cv.waitKey(0)

