# ---------- THIS IS USED TO CAPTURE STORE THE PHOTOS TO TRAIN THE FACE RECOGNITION SYSTEMS ---------
#                             CREATED BY LAHIRU DINALANKARA - AKA SPIKE
# ----------------------------------------------------------------------------------------------------

import cv2                  #   Importing the opencv
import numpy as np          #   Import Numarical Python
import NameFind
WHITE = [255, 255, 255]

#   import the Haar cascades for face ditection

face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
spec_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')


#ID = NameFind.AddName()

            
        
              


#Count = 0

cap = cv2.VideoCapture("TestFile.wmv")   #   Camera object
#cap = cv2.VideoCapture(0)
#img = cv2.imread("Me4.jpg")
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                    #   Convert the Camera to gray




            


    

    #   Eyes should be inside the face.
    
    XX = NameFind.DetectEyes(spec_cascade, face_cascade, gray)

    if (XX):
        cv2.imshow("RETURNED", XX[0])
        NameFind.DrawBox(gray, XX[1], XX[2], XX[3], XX[4])


    cv2.imshow('Face Recognition System Capture Faces', gray)       #   Show the video

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
