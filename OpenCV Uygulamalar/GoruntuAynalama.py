import cv2

img = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\kenan.jpeg")
flipped = cv2.flip(img, 1) # 1:Yatay çevirme, 0: Dikey çevirme
cv2.imshow("Aynalanmiş Görüntü", flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()