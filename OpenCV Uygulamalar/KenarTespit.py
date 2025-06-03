import cv2

img = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\kenan.jpeg", cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(img, 50, 150)
cv2.imshow("Kenar Tespit", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()