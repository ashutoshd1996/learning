import cv2 as cv
import numpy as  np

img = cv.imread('Data/Photos/Park.jpg')
# cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel 
sobel_x = cv.Sobel(gray, cv.CV_64F,1,0)
sobel_y = cv.Sobel(gray, cv.CV_64F,0,1)
combined_sobel = cv.bitwise_or(sobel_x,sobel_y)
# combined_sobel = cv.Sobel(gray, cv.CV_64F,1,1)
# cv.imshow('sobel_x', sobel_x)
# cv.imshow('sobel_y', sobel_y)
cv.imshow('combined_sobel', combined_sobel)

# Canny
canny = cv.Canny(gray, 150,150)
cv.imshow('Canny',canny)

cv.waitKey(0)