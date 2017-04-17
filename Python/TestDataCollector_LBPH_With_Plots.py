# ------------ COLLECTS DATA ON LBPH BY RUNNING IT ON A GIVEN IMAGE AND SAVING DATA TO A TEXT FILE -------------
# ------------------------------ SAVES THE DATA IN 3 TEXT FILES ----------------------------------------------

import os               # importing the OS for path
import cv2              # importing the OpenCV library
import numpy as np      # importing Numpy library
from PIL import Image   # importing Image library
import matplotlib.pyplot as plt
import NameFind

face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml')
path = 'dataSet'                                     # path to the photos

img = cv2.imread('Me4.jpg')        # -------------->>>>>>>>>>>>>>>>>>  The Image to be checked

def getImageWithID(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    FaceList = []
    IDs = []

    for imagePath in imagePaths:
        faceImage = Image.open(imagePath).convert('L')          # Open image and convert to gray
        print(str((faceImage.size)))
        faceImage = faceImage.resize((110, 110))                 # resize the image
        faceNP = np.array(faceImage, 'uint8')                   # convert the image to Numpy array
        print(str((faceNP.shape)))
        ID = int(os.path.split(imagePath)[-1].split('.')[1])    # Get the ID of the array
        FaceList.append(faceNP)                                 # Append the Numpy Array to the list
        IDs.append(ID)                                          # Append the ID to the IDs list

    return np.array(IDs), FaceList                              # The IDs are converted in to a Numpy array


IDs, FaceList = getImageWithID(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                # Convert the Camera to gray
faces = face_cascade.detectMultiScale(gray, 1.3, 4)                         # Detect the faces and store the positions
radTrain = open("SaveData/LBPH/LBPH_PIXEL_RADIUS.txt", "w+")  # open the file to write data
neiTrain = open("SaveData/LBPH/LBPH_NEIGHBOURS.txt", "w+")   # open the file to write data
cellTrain = open("SaveData/LBPH/LBPH_CELLS.txt", "w+")       # open the file to write data

for (x, y, w, h) in faces:
    Face = cv2.resize((gray[y: y+h, x: x+w]), (110, 110))
    radPix = 1
    rad_tabal_ID = []
    rad_tabal_conf = []
    # --------------------------- Run tests for the radius from the centre ----------------
    for _ in range(54):
        recog = cv2.face.createLBPHFaceRecognizer(radPix)     # creating EIGEN FACE RECOGNISER
        print('TRAINING FOR  ' + str(radPix) + ' PIXELS FROM CENTRE')
        recog.train(FaceList, IDs)                                          # The recogniser is trained using the images
        print('LBPH FACE RECOGNISER TRAINED')
        ID, conf = recog.predict(Face)
        rad_tabal_ID.append(ID)
        rad_tabal_conf.append(conf)
        radTrain.write(str(ID) + "," + str(conf) + "\n")
        print ("FOR RADIUS: " + str(radPix) + " ID IS: " + str(ID) + " THE CONFIDENCE: " + str(conf))
        radPix = radPix + 1
    plt.subplot(3, 2, 1)
    plt.plot(rad_tabal_ID)
    plt.title('ID against Pixel Radius')
    plt.axis([10, 25, 0, 53])
    plt.ylabel('ID')
    plt.xlabel('Radius (Pixels)')
    plt.subplot(3, 2, 2)
    plt.plot(rad_tabal_conf, 'red')
    plt.title('Confidence against Pixel Radius')
    plt.ylabel('Confidence')
    plt.xlabel('Radius (Pixels)')
    # ---------------------------  Run tests for the neighbours -----------------------------
    radPixel = 2    # ------>> CHANGE THE PIXEL RADIUS IF A BETTER VALUE IS FOUND
    neighbour = 1
    nei_ID = []
    nei_conf = []
    for _ in range(13):
        recog = cv2.face.createLBPHFaceRecognizer(radPixel, neighbour)  # creating FACE RECOGNISER
        print('TRAINING FOR  ' + str(neighbour) + ' NEIGHBOURS')
        recog.train(FaceList, IDs)                                          # The recogniser is trained using the images
        print('LBPH FACE RECOGNISER TRAINED')
        ID, conf = recog.predict(Face)
        nei_ID.append(ID)
        nei_conf.append(conf)
        neiTrain.write(str(ID) + "," + str(conf) + '\n')
        print ('FOR RADIUS: ' + str(radPixel) + " AND " + str(neighbour) + "NEIGHBOURS, ID IS: " + str(ID) + " THE CONFIDENCE: " + str(conf))
        neighbour = neighbour + 1
    plt.subplot(3, 2, 3)
    plt.plot(nei_ID)
    plt.title('ID against number of neighbours')
    plt.axis([10, 25, 0, 12])
    plt.ylabel('ID')
    plt.xlabel('Number of neighbours')
    plt.subplot(3, 2, 4)
    plt.plot(nei_conf, 'red')
    plt.title('ID against number of neighbours')
    plt.ylabel('Confidence')
    plt.xlabel('Number of neighbours')
    # ---------------------------  Run tests for the Cell Number -----------------------------
    neighbour = 2   # ------>> CHANGE THE NEIGHBOUR IF BETTER VALUE IS FOUND
    cellVal = 1
    cell_ID = []
    cell_conf = []
    for _ in range(50):
        recog = cv2.face.createLBPHFaceRecognizer(radPixel, neighbour, cellVal, cellVal)  # creating FACE RECOGNISER
        print('TRAINING FOR  ' + str(cellVal) + ' CELLS')
        recog.train(FaceList, IDs)                                          # The recogniser is trained using the images
        print('LBPH FACE RECOGNISER TRAINED')
        ID, conf = recog.predict(Face)
        cell_ID.append(ID)
        cell_conf.append(conf)
        cellTrain.write(str(ID) + "," + str(conf) + "\n")
        print ('FOR RADIUS: ' + str(radPixel) + " , " + str(neighbour) + "NEIGHBOURS AND CELL VALUE " + str(cellVal) + ", ID IS: " + str(ID) + " THE CONFIDENCE: " + str(conf))
        cellVal = cellVal + 1
    plt.subplot(3, 2, 5)
    plt.plot(cell_ID)
    plt.title('ID against number of cells')
    plt.axis([10, 25, 0, 49])
    plt.ylabel('ID')
    plt.xlabel('Number of Cells')
    plt.subplot(3, 2, 6)
    plt.plot(cell_conf, 'red')
    plt.title('ID against number of cells')
    plt.ylabel('Confidence')
    plt.xlabel('Number of Cells')
    plt.show()
radTrain.close()
neiTrain.close()
cellTrain.close()

print 'All FILES ARE WRITTEN...'
cv2.destroyAllWindows()