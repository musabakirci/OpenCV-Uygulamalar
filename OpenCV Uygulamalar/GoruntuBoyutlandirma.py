import cv2

img = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\kenan.jpeg")
resized = cv2.resize(img,(450,350))
cv2.imshow("Yeni Hali", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()