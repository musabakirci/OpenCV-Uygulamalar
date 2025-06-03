import cv2
import numpy as np

image = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\sekiller.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 100, 300)

# 4. Konturları bulalım
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 5. Konturları çizelim
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

cv2.imshow("Kontorlu Goruntu", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Kod Açıklaması
Görüntüyü Yükleme:
Görüntü yüklenir.

Gri Tonlamaya Çevirme:
Görüntü gri tonlamaya çevrilir, çünkü kenar algılaması gri görüntülerde daha sağlıklı olur.

Canny Algoritması ile Kenar Algılama:
cv2.Canny() fonksiyonu ile kenarlar tespit edilir.

Konturları Bulma:
cv2.findContours() fonksiyonu, tespit edilen kenarlardan konturları çıkarır.

Konturları Çizme:
cv2.drawContours() ile tespit edilen şekillerin çevresine çizgiler çizilir.
"""