# --------------------------  THIS IS USED TO STORE THE PHOTOS TO TRAIN THE FACE RECOGNITION SYSTEMS
#                             CREATED BY LAHIRU DINALANKARA - AKA SPIKE
#----------------------------------------------------------------------------------------------------

import cv2                  #   Importing the opencv
import numpy as np          #   Import Numarical Python
import NameFind


#   import the Haar cascades for face ditection

face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
spec_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')


ID = NameFind.AddName()

Count = 0                                    

cap = cv2.VideoCapture(0)   #   Camera object

while (Count < 100):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        #   Convert the Camera to gray
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) #   Detect the faces and store the positions
    
    for (x, y, w, h) in faces:                                      #   Frames  LOCATION X, Y  WIDTH, HEIGHT
        

        #   Eyes should be inside the face.
        roi_gray = gray[y: y+h, x: x+w]             #   The Face is isolated and cropped
        roi_color = img[y: y+h, x: x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        glass = spec_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 1)        
            for (sx, sy, sw, sh) in glass:
                Count = Count +1
                print(str(Count))
                cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (255, 0, 0), 2)

                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Draw a box arround the face
                cv2.putText(img,"Face Ditected", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, .8, 255)
                cv2.imwrite("dataSet/User." + str(ID) + "." + str(Count) + ".jpg", roi_gray)
                cv2.imshow('Last Detected face', roi_gray)         #   Show the detected faces
                cv2.waitKey(100)
    
    cv2.imshow('Face Recognition System', img)          #   Show the video  
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
