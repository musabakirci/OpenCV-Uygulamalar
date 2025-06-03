import cv2

img = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\kenan.jpeg")

_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Siyah-Beyaz Görüntü", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()