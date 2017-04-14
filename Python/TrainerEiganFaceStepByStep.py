#   ------------ TRAINER FOR THE EIGEN FACE RECOGNISER VARIABLE CONT 
#   ------------ FOR THE FACE RECOGNITION ALL THE FACES ARE REQUIRED TO BE SAME SIZE

import os               #   importing the OS for path
import cv2              #   importing the OpenCV library
import numpy as np      #   importing Numpy library
from PIL import Image   #   importing Image library
import NameFind

Info = open("EIGEN_TRAINER.txt", "r+")

face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
path = 'dataSet'                                     # path to the photos
img = cv2.imread('Me2.jpg')

def getImageWithID (path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    FaceList = []
    IDs = []

    for imagePath in imagePaths:
        faceImage = Image.open(imagePath).convert('L')  #   Open image and convert to gray
        print(str((faceImage.size)))

        faceImage = faceImage.resize((110,110))         #   resize the image so the EIGEN recogniser can be trained
        
        faceNP = np.array(faceImage, 'uint8')           # convert the image to Numpy array
        print(str((faceNP.shape)))

        
        
        ID = int(os.path.split(imagePath)[-1].split('.')[1])    #   Retreave the ID of the array
        FaceList.append(faceNP)                         #   Append the Numpy Array to the list
        IDs.append(ID)                                  #   Append the ID to the IDs list

        cv2.imshow("Trainig Set", faceNP)               #   Show the images in the list
    return np.array(IDs), FaceList                      # The IDs are converted in to a Numpy array


IDs, FaceList = getImageWithID(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                #   Convert the Camera to gray
faces = face_cascade.detectMultiScale(gray, 1.3, 4)                         #   Detect the faces and store the positions
Table  = []
for (x, y, w, h) in faces:
    Face = cv2.resize((gray[y: y+h, x: x+w]), (110, 110))
    Lev = 1

    for _ in range(3):
        recog = cv2.face.createEigenFaceRecognizer(Lev)     # creating EIGEN FACE RECOGNISER 
        print('TRAINING......')
        recog .train(FaceList, IDs)             # The recongniser is trained using the images
        print('EIGEN FACE RECOGNISER COMPLETE')
        ID, conf = recog.predict(Face)
        NAME = NameFind.ID2Name(ID, conf)
        NameFind.DispID(x, y, w, h, NAME, gray)
        cv2.imshow("RESULT", gray)
        cv2.waitKey(1)
        Info.write(str(ID) + "," + str(conf) + "\n")
        Table.append((ID, conf))
        print str(Table)
        Lev = Lev + 1

    Info.close()
        
cv2.destroyAllWindows();
