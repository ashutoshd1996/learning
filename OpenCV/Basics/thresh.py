from ctypes import cdll
import cv2 as cv

img = cv.imread('Data/Photos/cats.jpg')
# cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# Simple thesholding
threshold, thresh = cv.threshold(gray,150, 255, cv.THRESH_BINARY)
# sets the pixel intensities above 150 to 255
# cv.imshow('Simple Threshold', thresh)


threshold, thresh_inv = cv.threshold(gray,150, 255, cv.THRESH_BINARY_INV)
# sets the pixel intensities below 150 to 255
# cv.imshow('Simple Threshold Inverse', thresh_inv)

# Adaptive thresholding 
adaptive = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 1) 
cv.imshow('Adaptive Threshold', adaptive)

cv.waitKey(0)