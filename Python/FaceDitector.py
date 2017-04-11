# --------------------------  THIS IS USED TO DITECT FACES AND EYES USING HAAR CASCADES--------------
#                             CREATED BY LAHIRU DINALANKARA - AKA SPIKE
#----------------------------------------------------------------------------------------------------

import cv2                  #   Importing the opencv
import numpy as np          #   Import Numarical Python
import NameFind



#   import the Haar cascades for face ditection

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
spec_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')


#ID = NameFind.AddName()

Count = 0                                    

cap = cv2.VideoCapture(0)   #   Camera object

while True:
    ret, img2 = cap.read()
    img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)        #   Convert the Camera to gray
    faces = face_cascade.detectMultiScale(img, 1.1, 15) #   Detect the faces and store the positions
    
    for (x, y, w, h) in faces:                                      #   Frames  LOCATION X, Y  WIDTH, HEIGHT
        cv2.rectangle(img, (x, y), (x+w, y+h), WHITE, 1)
        cv2.putText(img, "FACE", (x, y-5), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)

        #   Eyes should be inside the face.
        #roi_gray = gray[y: y+h, x: x+w]             #   The Face is isolated and cropped
        
    eyes = eye_cascade.detectMultiScale(img)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), WHITE, 1)
        cv2.putText(img, "EYE", (ex, ey-5), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)
        
    glass = spec_cascade.detectMultiScale(img)
    for (sx, sy, sw, sh) in glass:
        cv2.rectangle(img, (sx, sy), (sx+sw, sy+sh), WHITE, 1)
        cv2.putText(img, "SPECS", (sx, sy-5), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)

    
    cv2.imshow('Face Recognition System', img)          #   Show the video  
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
