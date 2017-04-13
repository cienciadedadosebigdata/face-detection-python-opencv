import cv2                  #   Importing the opencv
import numpy as np          #   Import Numarical Python
import NameFind
WHITE = [255, 255, 255]

#   import the Haar cascades for face ditection

face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

Recog = cv2.face.createEigenFaceRecognizer(100)

                                   



img = cv2.imread('Me.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                    #   Convert the Camera to gray
faces = face_cascade.detectMultiScale(gray, 1.3, 5)             #   Detect the faces and store the positions

for (x, y, w, h) in faces:                                      #   Frames  LOCATION X, Y  WIDTH, HEIGHT
    

    #   Eyes should be inside the face.
    roi_gray = gray[y: y+h, x: x+w]
    cv2.imshow("FACE", roi_gray)
    face[0] = roi_gray
    face[1] = roi_gray
    ID[0] = 1
    ID[1] = 1
    
Recog.train(face, ID)


cv2.waitKey(0)
cv2.destroyAllWindows()
