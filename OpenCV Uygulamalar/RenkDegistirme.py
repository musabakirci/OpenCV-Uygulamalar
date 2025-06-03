import cv2
import numpy as np

img = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\kenan.jpeg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])
mask = cv2.inRange(hsv, lower_red, upper_red)
img[mask>0] = (0, 255, 0)
 
cv2.imshow("Degistirilmis Renkler", img)

cv2.waitKey(0)
cv2.destroyAllWindows()