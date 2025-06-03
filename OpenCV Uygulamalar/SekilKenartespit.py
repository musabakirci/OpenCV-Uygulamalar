import cv2
import numpy as np

image = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\kasaba.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 300)

contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
    cv2.drawContours(image, [approx], 0, (0,255,0),3)

cv2.imshow("Shapes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()    


"""
Kod Açiklamasi
Bu kod, OpenCV kullanarak bir görüntüdeki sekilleri algilar ve konturlarini çizer.

Görüntüyü Yükleme: cv2.imread("shapes.png") ile belirtilen görüntü yüklenir.
Gri Tonlamaya Çevirme: cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) ile görüntü gri tonlamaya çevrilir.
Kenar Tespiti: cv2.Canny(gray, 50, 150) fonksiyonu ile Canny kenar algilama islemi uygulanir.
Konturlari Bulma: cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) ile görüntüdeki sekillerin konturlari bulunur.
Konturlari Yaklasarak Çizme:
    cv2.approxPolyDP() fonksiyonu ile konturlar yaklasilarak (approximation) daha düzgün hale getirilir.
    cv2.drawContours() ile bulunan konturlar yesil renk (0, 255, 0) ile çizilir.
Görüntüyü Gösterme: cv2.imshow("Shapes", image) ile sekillerin konturlari çizilmis hali ekranda gösterilir.
Bekleme ve Pencereleri Kapatma: cv2.waitKey(0) ile kullanici bir tusa basana kadar beklenir, ardindan cv2.destroyAllWindows() ile tüm pencereler kapatilir.
"""

"""
Algoritma
Görüntüyü yükle.
Görüntüyü gri tonlamaya çevir.
Canny kenar algilama islemini uygula.
Konturlari bul.
Her kontur için:
    Konturu yaklasarak (approximate) düzelt.
    Konturu görüntü üzerine çiz.
Sekillerin konturlarini göster.
Kullanici bir tusa basinca tüm pencereleri kapat.
"""