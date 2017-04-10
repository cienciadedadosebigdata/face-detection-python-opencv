#   ------------ DITECTOR FOR THE FISHER FACE RECOGNISER
#   ------------ FOR THE FACE RECOGNITION ALL THE FACES ARE REQUIRED TO BE SAME SIZE

import cv2                  #   Importing the opencv
import numpy as np          #   Import Numarical Python
import NameFind


#   import the Haar cascades for face and eye ditection

face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
spec_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')


recognise = cv2.face.createFisherFaceRecognizer(num_components = 100, threshold = 5000)  # creating FISHER FACE RECOGNISER 
recognise.load("Recogniser/trainingDataFisher.xml")                                   #   Load the training data from the trainer to recognise the faces



    

cap = cv2.VideoCapture(0)                                                       #   Camera object

ID = 0

while (True):
    ret, img = cap.read()                                                       #   Read the camera object
    print img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                #   Convert the Camera to gray
     
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)                         #   Detect the faces and store the positions
    for (x, y, w, h) in faces:                                                  #   Frames  LOCATION X, Y  WIDTH, HEIGHT
        roi_gray = cv2.resize((gray[y: y+h, x: x+w]), (110, 110))               #   The Face is isolated and cropped

        #   -----------------------------------     BY CONFIRMING THE EYES ARE INSIDE THE FACE BETTER FACE RECOGNITION IS GAINED
        

        roi_color = img[y: y+h, x: x+w] 
        eyes = eye_cascade.detectMultiScale(roi_gray)
        glass = spec_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 255, 255), 1)     #   Draw a rectangle arround the face
            ID, conf = recognise.predict(roi_gray)                              #   Determine the ID of the photo
            NAME = NameFind.ID2Name(ID ,conf)
            

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
            cv2.imshow('CAPTURED FACE', roi_gray)                   

    cv2.imshow('FisherFace Face Recognition System', gray)                                 #   Show the video  
    
    if cv2.waitKey(1) & 0xFF == ord('q'):                                       #   Quit if the key is Q
        break

cap.release()
cv2.destroyAllWindows()
