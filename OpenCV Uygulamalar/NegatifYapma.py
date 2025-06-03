import cv2 

img = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\kenan.jpeg")

negative = cv2.bitwise_not(img)
cv2.imshow("Negatif Goruntu", negative)

cv2.waitKey(0)
cv2.destroyAllWindows()