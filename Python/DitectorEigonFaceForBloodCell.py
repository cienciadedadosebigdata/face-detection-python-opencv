#   ------------ DITECTOR FOR THE EIGEN FACE RECOGNISER
#   ------------ FOR THE FACE RECOGNITION ALL THE FACES ARE REQUIRED TO BE SAME SIZE

import cv2                  #   Importing the opencv
import numpy as np          #   Import Numarical Python
import NameFind


#   import the Haar cascades for face and eye ditection




recognise = cv2.face.createEigenFaceRecognizer(num_components = 50, threshold = 10000)  # creating EIGEN FACE RECOGNISER 
recognise.load("Recogniser/trainingDataEigan.xml")                                   #   Load the training data from the trainer to recognise the faces


Image = cv2.imread('B.jpg')
img = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY) 

IM = cv2.resize(img, (110, 110))        #   resize the image so the EIGEN recogniser can be trained



ID, conf = recognise.predict(IM)                    #   Determine the ID of the photo
if (ID == 1):
    print ("Not Infected")

else:
    print("Infected")

print ("Conf: " + str(conf))

