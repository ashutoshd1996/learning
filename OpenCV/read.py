import cv2 as cv

# img = cv.imread('Data/Photos/cat_large.jpg') # Reading images 

# cv.imshow('Cat', img) #Displaying images 

# cv.waitKey(0) #waits for infinite time until keypress

capture = cv.VideoCapture('Data/Videos/dog.mp4')

while True :
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()


