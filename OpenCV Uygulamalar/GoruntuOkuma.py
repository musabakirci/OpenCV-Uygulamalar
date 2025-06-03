import cv2

img = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\kenan.jpeg")
cv2.imshow("Görüntü", img)
cv2.waitKey(0)
cv2.destroyAllWindows()