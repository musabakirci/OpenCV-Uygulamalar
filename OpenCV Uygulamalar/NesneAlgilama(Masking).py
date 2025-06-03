import cv2
import numpy as np

image = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\trafik-stok.png")
cv2.imshow("Orijinal Goruntu", image)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_blue = np.array([100, 50, 50])
upper_blue = np.array([130, 255, 255])

mask = cv2.inRange(hsv, lower_blue, upper_blue)

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Makse", mask)
cv2.imshow("Filtrelenmis Goruntu", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Kod Açıklaması
Görüntüyü Yükleme ve HSV'ye Çevirme:

cv2.cvtColor(image, cv2.COLOR_BGR2HSV): BGR renk uzayından HSV renk uzayına çeviriyoruz. HSV, renkleri daha iyi analiz etmek için kullanılır.
Renk Aralığını Belirleme:

lower_blue ve upper_blue: Mavi rengi tespit etmek için belirlenen alt ve üst sınırlar.
HSV aralıklarını değiştirerek farklı renkleri algılayabilirsiniz.
Maske Oluşturma:

cv2.inRange(hsv, lower_blue, upper_blue): Belirtilen aralıktaki renkleri tespit eder ve bir maske oluşturur.
Sonucu Birleştirme:

cv2.bitwise_and(image, image, mask=mask): Sadece belirtilen renkleri içeren bir görüntü oluşturur.
Sonuçları Gösterme:

cv2.imshow('Maske', mask): Siyah-beyaz maske gösterilir.
cv2.imshow('Filtrelenmiş Görüntü', result): Sadece seçilen rengin olduğu görüntü gösterilir.
"""