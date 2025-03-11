import os
import cv2 as cv
import numpy as np

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna','Mindy Kaling' ]
DIR = R'C:\Users\USER\Desktop\uni internship\openCV faces\Resources-Faces_train'
haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = [] #image arrays of faces
labels = [] #people with which the image belongs to

def create_train():
    for persons in people:
        path = os.path.join(DIR, persons)
        label = people.index(persons)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

            for (x, y, w, h) in face_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label) #idex of p

create_train()
print('Training Done ---------------')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

#Train the model on features and labels list
face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)

