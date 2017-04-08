

import os       #   importing the OS for path
import cv2      #   importing the OpenCV library
import numpy as np  
from PIL import Image

recog = cv2.face.createLBPHFaceRecognizer()     # creating face recogniser

path = 'dataSet'                                # path to the photos

def getImageWithID (path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    FaceList = []
    IDs = []

    for imagePath in imagePaths:
        faceImage = Image.open(imagePath).convert('L')  #   Open image and convert to gray
        faceNP = np.array(faceImage, 'uint8')           # convert the image to Numpy array
        ID = int(os.path.split(imagePath)[-1].split('.')[1])    #   Retreave the ID of the array
        FaceList.append(faceNP)                         #   Append the Numpy Array to the list
        IDs.append(ID)                                  #   Append the ID to the IDs list

        cv2.imshow("Trainig Set", faceNP)               #   Show the images in the list
        cv2.waitKey(20)
    return np.array(IDs), FaceList                      # The IDs are converted in to a Numpy array


IDs, FaceList = getImageWithID(path)

recog .train(FaceList, IDs)             # The recongniser is trained using the images
recog.save('Recogniser/trainingData.xml')
cv2.destroyAllWindows();
