#   ------------ DITECTOR FOR THE LBPH FACE RECOGNISER
#   ------------ BY LAHIRU DINALANKARA AKA SPIKE


import cv2                  #   Importing the opencv
import numpy as np          #   Import Numarical Python
import NameFind

#   import the Haar cascades for face and eye ditection

face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
spec_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')


LBPH = cv2.face.createLBPHFaceRecognizer()                                 #   LBPH Face recogniser object
EIGEN = cv2.face.createEigenFaceRecognizer(200, 10000)
FISHER = cv2.face.createFisherFaceRecognizer(200, 1000)

LBPH.load("Recogniser/trainingDataLBPH.xml")                                   #   Load the training data from the trainer to recognise the faces
EIGEN.load("Recogniser/trainingDataEigan.xml")
FISHER.load("Recogniser/trainingDataFisher.xml")



    
# -------------------------     START THE VIDEO FEED ------------------------------------------

img = cv2.imread('Me4.jpg')


#--------------
#ret, img = cap.read()                                                       #   Read the camera object
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                #   Convert the Camera to gray
faces = face_cascade.detectMultiScale(gray, 1.3, 4)                         #   Detect the faces and store the positions
print(faces)

for (x, y, w, h) in faces:                                                  #   Frames  LOCATION X, Y  WIDTH, HEIGHT
    
    #   Eyes should be inside the face.
    Face = cv2.resize((gray[y: y+h, x: x+w]), (110, 110))                                         #   The Face is isolated and cropped

    
    ID, conf = LBPH.predict(Face)                    #   Determine the ID of the photo
    NAME = NameFind.ID2Name(ID, conf)
    NameFind.DispID(x, y, w, h, NAME, gray)

    ID, conf = EIGEN.predict(Face)
    NAME = NameFind.ID2Name(ID, conf)
    NameFind.DispID2(x, y, w, h, NAME, gray)

    ID, conf = FISHER.predict(Face)
    NAME = NameFind.ID2Name(ID, conf)
    NameFind.DispID3(x, y, w, h, NAME, gray)

    
cv2.imshow('LBPH Face Recognition System', gray)                                 #   Show the video  
cv2.waitKey(0)



cv2.destroyAllWindows()
