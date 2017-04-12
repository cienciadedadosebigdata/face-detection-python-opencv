import cv2
import numpy as np

Im1 = cv2.resize(cv2.imread("dataSet/User.13.1.jpg"), (100,100))
Im2 = cv2.resize(cv2.imread("dataSet/User.15.13.jpg"), (100, 100))

cv2.imshow(" T1", Im1)
cv2.imshow(" T2 ", Im2)



New = np.concatenate((Im1, Im2),1)
cv2.imshow("NEW", New)
cv2.waitKey(0)


