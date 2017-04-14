# ---------- THIS IS USED TO CAPTURE STORE THE PHOTOS TO TRAIN THE FACE RECOGNITION SYSTEMS ---------
#                             CREATED BY LAHIRU DINALANKARA - AKA SPIKE
#----------------------------------------------------------------------------------------------------

import cv2                  #   Importing the opencv
import numpy as np          #   Import Numarical Python
import NameFind
import math
WHITE = [255, 255, 255]

#   import the Haar cascades for face ditection

face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
spec_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')


#ID = NameFind.AddName()

def DetectEyes(Cascade1, Cascade2, Image):
    dst = []
    faces = face_cascade.detectMultiScale(Image, 1.3, 5)             #   Detect the faces and store the positions

    for (x, y, w, h) in faces:                                                              #   Frames  LOCATION X, Y  WIDTH, HEIGHT
        FaceImage = Image[y-int(h/2): y+int(h*1.5), x-int(x/2): x+int(w*1.5)]                  #   The Face is isolated and cropped
        glass = Cascade1.detectMultiScale(FaceImage)                                            #   This ditects the eyes 
        for (sx, sy, sw, sh) in glass:
            cv2.rectangle(FaceImage, (sx, sy), (sx+sw, sy+sh), (255, 0, 0), 2)   
            if glass.shape[0] == 2:                                                         #   The Image should have 2 eyes                
                    CentE1 = (glass[0][0] + (glass[0][2]/2), glass[0][1] + glass[0][3]/2)
                    CentE2 = (glass[1][0] + (glass[1][2]/2), glass[1][1] + glass[1][3]/2)
                    DY = ((glass[1][1] + glass[1][3]/2) - (glass[0][1]+glass[0][3]/2))      #   Height diffrence between the glass
                    DX = ((glass[1][0] + glass[1][2]/2) - glass[0][0]+(glass[0][2]/2))      #   Width diffrance between the glass
                    
                    print DX, DY
                    if (DX != 0.0) and (DY != 0.0):                                         #   Make sure the the change happens only if there is an angle
                        
                        Theta = math.degrees(math.atan(round(float(DY)/float(DX),2)))                #   Find the Angle
                        print str(Theta)

                        M = cv2.getRotationMatrix2D((cols/2,rows/2),Theta,1)                #   Find the Rotation Matrix
                        dst = cv2.warpAffine(Image,M,(cols,rows))
                        Face2 = Cascade2.detectMultiScale(dst, 1.3, 5)
                        for (xx, yy, ww, hh) in Face2:
                            cv2.rectangle(dst, (xx, yy), (xx+ww, yy+hh), WHITE, 1)
                            Cropped = dst[yy: yy+hh, xx: xx+ww]
                            cv2.imshow("CROPPEDANDROTATED", Cropped)
                            return Cropped, x, y, h, w
                        
                        cv2.imshow("ROTATED", dst)
                     


Count = 0                                    
Theta = 0
cap = cv2.VideoCapture("TestFile.wmv")   #   Camera object
cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                    #   Convert the Camera to gray
    rows,cols = gray.shape	                                    #   Get the size of the image
    dst = gray




                
    
    
        

        #   Eyes should be inside the face.
        
    XX = DetectEyes(spec_cascade, face_cascade, gray)
    if (XX):
        NameFind.DrawBox(gray, XX[1], XX[2], XX[3], XX[4])
##        
##            
##        cv2.imshow("CAPTURED PHOTO", roi_gray)
##        
##        cv2.rectangle(gray, (x, y), (x+w, y+h), WHITE, 1)
##        cv2.putText(gray, "FACE DITECTED", (x+(w/2), y-5), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)        
##                            #   Show the detected faces
##        
##        
##        cv2.rectangle(gray, (0,0), (gray.shape[1], 30), (0,0,0), -1)
##        cv2.putText(gray, (str(Theta) + " Photos Saved ..."), (200, 20), cv2.FONT_HERSHEY_DUPLEX, .6, WHITE)
##        print(str(Count))
##       
##        #cv2.imwrite("dataSet/User." + str(ID) + "." + str(Count) + ".jpg", roi_gray)
##        
##        #cv2.waitKey(300)
##        Count = Count +1

    cv2.imshow('Face Recognition System Capture Faces', gray)       #   Show the video  
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
