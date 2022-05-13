import cv2 as cv

img = cv.imread('Data/Photos/cat_large.jpg') # Reading images 



def rescaleFrame(Frame, scale=0.75):
    # works for Images, Videos and live Videos 
    width = int(Frame.shape[1] * scale) 

    height = int(Frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(Frame, dimensions, interpolation = cv.INTER_AREA) 

# def changeRes(width, height):
#     # works for only Live Videos only 
#     capture.set(3,width)
#     capture.set(4, height)



resizedImg = rescaleFrame (img, 0.2)
cv.imshow('Cat', img) #Displaying images 
cv.waitKey(0) #waits for infinite time until keypress
cv.imshow('Cat', resizedImg) #Displaying images 
cv.waitKey(0) #waits for infinite time until keypress

# capture = cv.VideoCapture('../Data/Videos/dog.mp4')

# while True :
#     isTrue, frame = capture.read()
#     frame_resized = rescaleFrame(frame, 0.2)
#     cv.imshow('Video', frame)
#     cv.imshow('Video', frame_resized)   

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()