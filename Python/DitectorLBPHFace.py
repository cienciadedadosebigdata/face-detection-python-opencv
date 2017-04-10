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
cap.set(6, 10)                                                                  #   Set the frame rate to 20

ID = 0

while (True):
    ret, img = cap.read()                                                       #   Read the camera object
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                #   Convert the Camera to gray
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)                         #   Detect the faces and store the positions
    
    for (x, y, w, h) in faces:                                                  #   Frames  LOCATION X, Y  WIDTH, HEIGHT
        
        #   Eyes should be inside the face.
        roi_gray = gray[y: y+h, x: x+w]                                         #   The Face is isolated and cropped
        roi_color = img[y: y+h, x: x+w] 
        eyes = eye_cascade.detectMultiScale(roi_gray)
        glass = spec_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 255, 255), 1)     #   Draw a rectangle arround the face
            ID, conf = recognise.predict(roi_gray)                    #   Determine the ID of the photo
            NAME = NameFind.ID2Name(ID, conf)
         #  ------------------------------------    THE POSITION OF THE ID BOX           
            Name_y_pos = y - 10
            Name_X_pos = x + w/2 - (len(NAME)*7/2)

            if Name_X_pos < 0:
                Name_X_pos = 0
            elif (Name_X_pos +10 + (len(NAME) * 7) > gray.shape[1]):
                  Name_X_pos= Name_X_pos - (Name_X_pos +10 + (len(NAME) * 7) - (gray.shape[1]))
            if Name_y_pos < 0:
                Name_y_pos = Name_y_pos = y + h + 10
                  
         #  ------------------------------------    THE DRAWING OF THE BOX AND ID   
            cv2.rectangle(gray, (Name_X_pos-10, Name_y_pos-25), (Name_X_pos +10 + (len(NAME) * 7), Name_y_pos-1), (0,0,0), -2)           #   Draw a Black Rectangle over the face frame
            cv2.rectangle(gray, (Name_X_pos-10, Name_y_pos-25), (Name_X_pos +10 + (len(NAME) * 7), Name_y_pos-1), (255, 255, 255), 1) 
            cv2.putText(gray, NAME, (Name_X_pos, Name_y_pos - 10), cv2.FONT_HERSHEY_DUPLEX, .4, (255, 255, 255))    #   Print the name of the ID
               
    
    cv2.imshow('LBPH Face Recognition System', gray)                                 #   Show the video  
    
    if cv2.waitKey(1) & 0xFF == ord('q'):                                       #   Quit if the key is Q
        break

cap.release()
cv2.destroyAllWindows()
