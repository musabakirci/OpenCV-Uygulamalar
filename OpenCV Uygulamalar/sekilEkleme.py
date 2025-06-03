import cv2

img = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\kenan.jpeg")

cv2.rectangle(img, (60,60), (200,200), (0,255,0), 3)
cv2.circle(img, (100,100), 50, (255, 0, 0), -1)
cv2.line(img, (40,40), (300, 300), (0, 0, 255), 2)
cv2.imshow("Sekiller Cizilmis Goruntu", img)

cv2.waitKey(0)
cv2.destroyAllWindows()