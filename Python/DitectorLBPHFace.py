import cv2                  #   Importing the opencv
import numpy as np          #   Import Numarical Python


#   import the Haar cascades for face and eye ditection

face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
spec_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')


recognise = cv2.face.createLBPHFaceRecognizer()                                 #   LBPH Face recogniser object
recognise.load("Recogniser/trainingData.xml")                                   #   Load the training data from the trainer to recognise the faces

Info = open("Names.txt", "r")

def FindName(Id, conf, Info):
    ID = []
    NAME = []
    while (True):
        Line = Info.readline()
        if Line == '':
            break
        ID.append(int(Line.split(",") [0]))
        NAME.append (Line.split(",")[1])
    
    Name = "Names: " + str(NAME[ID.index(Id)]) + str(round(conf))     
    return Name
    


cap = cv2.VideoCapture(1)                                                       #   Camera object
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
            
            cv2.rectangle(gray, (x, y-30), (x + w, y-1), (0,0,0), -2)           #   Draw a Black Rectangle over the face frame
            cv2.putText(gray, str(ID), (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 1.2, (255, 255, 255))    #   Print the name of the ID
               
    
    cv2.imshow('Face Recognition System', gray)                                 #   Show the video  
    
    if cv2.waitKey(1) & 0xFF == ord('q'):                                       #   Quit if the key is Q
        break

cap.release()
cv2.destroyAllWindows()
