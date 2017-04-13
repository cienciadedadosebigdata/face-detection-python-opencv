import cv2                  #   Importing the opencv
import numpy as np          #   Import Numarical Python
import NameFind


face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')

cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)




while True:
    ret, img1 = cap1.read()
    ret, img2 = cap2.read()
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    face1 = face_cascade.detectMultiScale(gray1, 1.3, 5)
    face2 = face_cascade.detectMultiScale(gray2, 1.3, 5)

    for (x1, y1, w1, h1) in face1:
        roi_gray1 = cv2.resize((gray1[y1: y1+h1, x1: x1+w1]), (110, 110))

    
        cv2.imshow("CAM1", roi_gray1)

    for (x2, y2, w2, h2) in face2:
        roi_gray2 = cv2.resize((gray2[y2: y2+h2, x2: x2+w2]), (110, 110))

    
        cv2.imshow("CAM2", roi_gray2)


    if (('roi_gray1')in locals() and ('roi_gray2')in locals()):
        print "True"
        newArr = np.add(roi_gray1, roi_gray2)
        newArr = newArr/2.0
        cv2.imshow("BOTH", newArr)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
