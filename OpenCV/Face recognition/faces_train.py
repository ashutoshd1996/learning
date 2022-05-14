import os 
import cv2 as cv
from cv2 import cvtColor
import numpy as np
from sklearn.pipeline import FeatureUnion

people =  ['Ben Afflek','Elton John','Jerry Seinfield','Madonna','Mindy Kaling']

DIR = r'E:\code\learning\OpenCV\Data\Faces\train'
haar_cascade = cv.CascadeClassifier('E:\\code\\learning\\OpenCV\\Face detection\\haar_face.xml')

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            
            for x,y,w,h in faces_rect:
                faces_roi = gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()


face_recognizer = cv.face.LBPHFaceRecognizer_create()
features = np.array(features, dtype='object') 
labels = np.array(labels)

#  Training the reognizer on features list and labels
face_recognizer.train(features,labels)

face_recognizer.save(r'Face recognition\face_trained.yml')
np.save(r'Face recognition\Features.npy', features)
np.save(r'Face recognition\Labels.npy',labels)


