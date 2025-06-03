import cv2

img = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\kenan.jpeg")
cropped = img[50:200,100:300]
cv2.imshow("Kesilen Görüntü", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()