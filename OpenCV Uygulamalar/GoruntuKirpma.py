import cv2
import numpy as np

img = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\kenan.jpeg")
cropped = img[50:150, 100:250]
cv2.imshow("Kirpilmis Goruntu", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()