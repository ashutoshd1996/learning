import cv2 as cv


img = cv.imread('Data/Photos/lady.jpg')
# cv.imshow('Person', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray Person', gray)

haar_cascade = cv.CascadeClassifier('E:\\code\\learning\\OpenCV\\Face detection\\haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print('Number of faces found = ', len(faces_rect))

for x,y,w,h in faces_rect:
    faces = cv.rectangle(img, (x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow('Faces', faces)

cv.waitKey(0)