from this import d
import cv2 as cv
import numpy as np
import glob

# Finding chessboard corners 

chessBoardSize = (5,8)

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)


# Defining the world coordinates for 3D points
objp = np.zeros((1, chessBoardSize[0] * chessBoardSize[1], 3), np.float32)
objp[0,:,:2] = np.mgrid[0:chessBoardSize[0], 0:chessBoardSize[1]].T.reshape(-1, 2)
prev_img_shape = None

# Creating vector to store vectors of 3D points for each checkerboard image
objpoints = []

# Creating vector to store vectors of 2D points for each checkerboard image
imgpoints = []

images = glob.glob('Data/*.jpg')

for image in images:
    img = cv.imread(image)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Finding chessboard corners
    ret, corners = cv.findChessboardCorners(gray, chessBoardSize, None)

    # print(ret)
    # If found, add object points, image Points (After refining them)
    if ret:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray, corners, (11,11), (-1, -1), criteria)
        imgpoints.append(corners)

        # Draw and display corners 
        cv.drawChessboardCorners(img, chessBoardSize, corners2, ret)
        # cv.imshow(image,img)
        # cv.waitKey(1000)

# cv.destroyAllWindows()

# Camera Calibration 

ret, CameraMatrix, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints,gray.shape[::-1],None, None)

print("Camera Calibrated: ", ret)
print("\nCamera matrix : ", CameraMatrix)
print("\ndist : ", dist)
print("\nrvecs : ", rvecs)
print("\ntvecs : ", tvecs)

# Undistortion
img = cv.imread('Data/00021.jpg')
h,  w = img.shape[:2]
newCameraMatrix, roi = cv.getOptimalNewCameraMatrix(CameraMatrix, dist, (w,h) ,1,(w,h))

dst = cv.undistort(img, CameraMatrix, dist, None, newCameraMatrix)
# crop the image
x,y,w,h = roi
dst = dst[y:y+h, x:x+w]
cv.imwrite('calibresult1.jpg', dst)

# Undistorting with remapping
mapx, mapy = cv.initUndistortRectifyMap(CameraMatrix, dist, None, newCameraMatrix, (w,h), 5)
dst = cv.remap(img, mapx, mapy, cv.INTER_LINEAR)
# crop the image
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
cv.imwrite('calibresult2.jpg', dst)

# Re-projection Error
mean_error = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv.projectPoints(objpoints[i], rvecs[i], tvecs[i], CameraMatrix, dist)
    error = cv.norm(imgpoints[i], imgpoints2, cv.NORM_L2)/len(imgpoints2)
    mean_error += error
print( "total error: {}".format(mean_error/len(objpoints)) )