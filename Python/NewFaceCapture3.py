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
#   GlassCascade    FaceCascade     Image   +++++++++++++++++++++
def DetectEyes(Cascade1, Cascade2, Image):
    dst = []
    Theta = 0
    
    faces = face_cascade.detectMultiScale(Image, 1.3, 5)             #   Detect the faces and store the positions

    for (x, y, w, h) in faces:                                                              #   Frames  LOCATION X, Y  WIDTH, HEIGHT
        FaceImage = Image[y-int(h/2): y+int(h*1.5), x-int(x/2): x+int(w*1.5)]                  #   The Face is isolated and cropped
        glass = Cascade1.detectMultiScale(FaceImage)                                            #   This ditects the eyes 
        for (sx, sy, sw, sh) in glass:
            cv2.rectangle(FaceImage, (sx, sy), (sx+sw, sy+sh), (255, 0, 0), 2)   
            if glass.shape[0] == 2:                                                         #   The Image should have 2 eyes
                print "Ditected 2 eyes"
                CentE1 = (glass[0][0] + (glass[0][2]/2), glass[0][1] + glass[0][3]/2)
                CentE2 = (glass[1][0] + (glass[1][2]/2), glass[1][1] + glass[1][3]/2)
                
                DY = ((glass[1][1] + glass[1][3]/2) - (glass[0][1]+glass[0][3]/2))      #   Height diffrence between the glass
                DX = ((glass[1][0] + glass[1][2]/2) - glass[0][0]+(glass[0][2]/2))      #   Width diffrance between the glass
                
                print "Eye 1  " + str(CentE1)
                print "Eye 2  " + str(CentE2)

                cv2.circle(FaceImage, CentE1, 30, (255, 0, 0), 2, 1)
                cv2.circle(FaceImage, CentE2, 30, (0, 255, 0), 2, 1)
                
                if (DX != 0.0) and (DY != 0.0):                                         #   Make sure the the change happens only if there is an angle
                    Theta = math.degrees(math.atan(round(float(DY)/float(DX),2)))                #   Find the Angle
                    print "Theta  " + str(Theta)
                    
                    M = cv2.getRotationMatrix2D((cols/2,rows/2),Theta,1)                #   Find the Rotation Matrix
                    Image = cv2.warpAffine(Image,M,(cols,rows))
                    cv2.imshow("ROTATED", Image)

            Face2 = Cascade2.detectMultiScale(Image, 1.3, 5)                      #   This ditects a face in the image
            FaceX = Face2[0][0]
            FaceY = Face2[0][1]
            FaceWidth = Face2[0][2]
            FaceHeigth = Face2[0][3]
            
            print "Face 2 Info  " + str(Face2)

            #cv2.rectangle(Image, (FaceX, FaceY), (FaceX + FaceWidth, FaceY + FaceHeigth), WHITE, 1)
            CroppedFace = Image[FaceY: FaceY + FaceHeigth, FaceX: FaceX + FaceWidth]
                
            cv2.imshow("CROPPED AND ROTATED", CroppedFace)
            return CroppedFace, x, y, h, w
            
            
        
              


Count = 0                                    

cap = cv2.VideoCapture("TestFile.wmv")   #   Camera object
#cap = cv2.VideoCapture(0)
img = cv2.imread("Me4.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                    #   Convert the Camera to gray
rows,cols = gray.shape	                                    #   Get the size of the image
dst = gray




            


    

    #   Eyes should be inside the face.
    
XX = DetectEyes(spec_cascade, face_cascade, gray)

if (XX):
    cv2.imshow("RETURNED", XX[0])
    NameFind.DrawBox(gray, XX[1], XX[2], XX[3], XX[4])


cv2.imshow('Face Recognition System Capture Faces', gray)       #   Show the video  

cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()
