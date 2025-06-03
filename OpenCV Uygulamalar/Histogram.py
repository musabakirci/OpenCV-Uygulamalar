import cv2

img = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\kenan.jpeg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
equalized = cv2.equalizeHist(gray)
cv2.imshow("Kontrast Arttirilmis", equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()