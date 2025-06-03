import cv2

image = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\trafik-stok.png")

# Metin Ekleyelim 
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, "Hiz sinirini asmayin", (250,60), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

cv2.imshow("Metinli Görüntü", image)

cv2.waitKey(0)
cv2.destroyAllWindows()