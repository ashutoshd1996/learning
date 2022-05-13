import cv2 as cv

img = cv.imread('Data/Photos/cats.jpg')
cv.imshow('Cats', img)

# averaging
avg = cv.blur(img,(3,3))
cv.imshow('Average', avg)

# Gaussian Blur
gblur = cv.GaussianBlur(img,(3,3), 0)
cv.imshow('Gaussian Blur', gblur)

# median - more effective in reducing noise, can remove salt and pepper noise 
# High kernel sizes not recommended
median = cv.medianBlur(img,3)
cv.imshow('Median', median)

# Bilateal Blurring - retains edges
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)