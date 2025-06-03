import cv2

img = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\kenan.jpeg")

bordered = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value=(255, 0, 0))
cv2.imshow("Cerceveli Goruntu", bordered)

cv2.waitKey(0)
cv2.destroyAllWindows()