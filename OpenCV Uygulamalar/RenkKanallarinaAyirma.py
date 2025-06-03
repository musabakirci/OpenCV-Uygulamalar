import cv2

img = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\kenan.jpeg")
b, g, r=cv2.split(img)
cv2.imshow("Mavi Kanal", b)
cv2.imshow("Yesil Kanal", g)
cv2.imshow("Kirmizi Kanal", r)
cv2.waitKey(0)
cv2.destroyAllWindows()