#   ------------ TRAINER FOR THE EIGEN FACE RECOGNISER
#   ------------ FOR THE FACE RECOGNITION ALL THE FACES ARE REQUIRED TO BE SAME SIZE

import os               #   importing the OS for path
import cv2              #   importing the OpenCV library
import numpy as np      #   importing Numpy library
from PIL import Image   #   importing Image library

EigenFace = cv2.face.createEigenFaceRecognizer()     # creating EIGEN FACE RECOGNISER
FisherFace = cv2.face.createFisherFaceRecognizer()  # Create FISHER FACE RECOGNISER
LBPHFace = cv2.face.createLBPHFaceRecognizer()      # Create LBPH FACE RECOGNISER

path = 'dataSet'                                     # path to the photos

def getImageWithID (path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    FaceList = []
    IDs = []

    for imagePath in imagePaths:
        faceImage = Image.open(imagePath).convert('L')  #   Open image and convert to gray
        faceImage = faceImage.resize((110,110))         #   resize the image so the EIGEN recogniser can be trained
        faceNP = np.array(faceImage, 'uint8')           # convert the image to Numpy array

        
        
        ID = int(os.path.split(imagePath)[-1].split('.')[1])    #   Retreave the ID of the array
        FaceList.append(faceNP)                         #   Append the Numpy Array to the list
        IDs.append(ID)                                  #   Append the ID to the IDs list

        cv2.imshow("Trainig Set", faceNP)               #   Show the images in the list
        cv2.waitKey(1)
    return np.array(IDs), FaceList                      #   The IDs are converted in to a Numpy array


IDs, FaceList = getImageWithID(path)


print('TRAINING......')
EigenFace.train(FaceList, IDs)             # The recongniser is trained using the images
print('EIGEN FACE RECOGNISER COMPLETE')
EigenFace.save('Recogniser/trainingDataEigan.xml')
print('FILE SAVED..')
FisherFace.train(FaceList, IDs)
print('Fisher Face Recogniser Training Complete...')
FisherFace.save('Recogniser/trainingDataFisher.xml')
print('Fisher Face XML saved... ')
LBPHFace.train(FaceList, IDs)
print('LBPH Face Recogniser Training Complete...')
LBPHFace.save('Recogniser/trainingDataLBPH.xml')


cv2.destroyAllWindows();
