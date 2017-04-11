#   ------------ DITECTOR FOR THE LBPH FACE RECOGNISER
#   ------------ BY LAHIRU DINALANKARA AKA SPIKE


import cv2                  #   Importing the opencv
import numpy as np          #   Import Numarical Python
import NameFind

#   import the Haar cascades for face and eye ditection

face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
spec_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')


recognise = cv2.face.createLBPHFaceRecognizer()                                 #   LBPH Face recogniser object
recognise.load("Recogniser/trainingDataLBPH.xml")                                   #   Load the training data from the trainer to recognise the faces


    
# -------------------------     START THE VIDEO FEED ------------------------------------------

cap = cv2.VideoCapture(0)                                                       #   Camera object

while (True):
    ret, img = cap.read()                                                       #   Read the camera object
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                #   Convert the Camera to gray
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)                         #   Detect the faces and store the positions
    
    for (x, y, w, h) in faces:                                                  #   Frames  LOCATION X, Y  WIDTH, HEIGHT
        
        #   Eyes should be inside the face.
        roi_gray = gray[y: y+h, x: x+w]                                         #   The Face is isolated and cropped
        eyes = eye_cascade.detectMultiScale(roi_gray)
        glass = spec_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            ID, conf = recognise.predict(roi_gray)                    #   Determine the ID of the photo
            NAME = NameFind.ID2Name(ID, conf)
            NameFind.DispID(x, y, w, h, NAME, gray)    
    cv2.imshow('LBPH Face Recognition System', gray)                                 #   Show the video  
    
    if cv2.waitKey(1) & 0xFF == ord('q'):                                       #   Quit if the key is Q
        break

cap.release()
cv2.destroyAllWindows()
