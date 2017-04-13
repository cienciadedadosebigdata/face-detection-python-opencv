# ---------- THIS IS USED TO CAPTURE STORE THE PHOTOS TO TRAIN THE FACE RECOGNITION SYSTEMS ---------
#                             CREATED BY LAHIRU DINALANKARA - AKA SPIKE
#----------------------------------------------------------------------------------------------------

import cv2                  #   Importing the opencv
import numpy as np          #   Import Numarical Python
import NameFind
WHITE = [255, 255, 255]

#   import the Haar cascades for face ditection

face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


#ID = NameFind.AddName()

Count = 0                                    

cap = cv2.VideoCapture(0)   #   Camera object

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                    #   Convert the Camera to gray
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)             #   Detect the faces and store the positions
    
    for (x, y, w, h) in faces:                                      #   Frames  LOCATION X, Y  WIDTH, HEIGHT
        

        #   Eyes should be inside the face.
        roi_gray = gray[y: y+h, x: x+w]                             #   The Face is isolated and cropped
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(gray, (x, y), (x+w, y+h), WHITE, 1)
            cv2.putText(gray, "FACE DITECTED", (x+(w/2), y-5), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)        
            
            cv2.rectangle(gray, (0,0), (gray.shape[1], 30), (0,0,0), -1)
            cv2.putText(gray, (str(Count) + " Photos Saved ..."), (200, 20), cv2.FONT_HERSHEY_DUPLEX, .6, WHITE)
            print(str(Count))
           
            #cv2.imwrite("dataSet/User." + str(ID) + "." + str(Count) + ".jpg", roi_gray)
            cv2.imshow("CAPTURED PHOTO", roi_gray)                  #   Show the detected faces
            #cv2.waitKey(300)
            Count = Count +1

    cv2.imshow('Face Recognition System Capture Faces', gray)       #   Show the video  
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
