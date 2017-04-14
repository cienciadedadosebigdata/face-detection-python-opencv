# ---------- THIS IS USED TO CAPTURE STORE THE PHOTOS TO TRAIN THE FACE RECOGNITION SYSTEMS ---------
#                             CREATED BY LAHIRU DINALANKARA - AKA SPIKE
#----------------------------------------------------------------------------------------------------

import cv2                  #   Importing the opencv
import numpy as np          #   Import Numarical Python
import NameFind
WHITE = [255, 255, 255]

#   import the Haar cascades for face ditection

img = cv2.imread('Me.jpg',0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),20,1)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('Face Recognition System Capture Faces', dst)       #   Show the video  
    
cv2.waitKey(0)

cv2.destroyAllWindows()
