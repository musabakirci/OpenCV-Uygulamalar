import cv2

img = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\kenan.jpeg")

cv2.putText(img, "Terminator", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imshow("Yazi Eklenmiş Görüntü" , img)
cv2.waitKey(0)
cv2.destroyAllWindows()