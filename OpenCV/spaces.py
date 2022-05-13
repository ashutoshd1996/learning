import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Data/Photos/Park.jpg')
cv.imshow('Park', img)

# BGR to Gray Image 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV Format 
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*A*B
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# Matplotlib takes RGB as its default format 
# plt.imshow(img) 
# plt.show()

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)
cv.waitKey(0)

# We cannot convert between formats, but only to BGR and then to a different format