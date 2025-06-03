import cv2

img = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\kenan.jpeg")
blur = cv2.GaussianBlur(img, (15,15), 0)
cv2.imshow("Bulanik Görüntü", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()