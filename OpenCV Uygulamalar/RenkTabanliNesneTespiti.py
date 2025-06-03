import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Orijinal", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()    
cv2.destroyAllWindows()


"""
Kod Açiklamasi
Bu kod, OpenCV kullanarak bilgisayar kamerasindan gerçek zamanli görüntü alir ve kirmizi renk tespiti yapar.

Kamera Açma: cv2.VideoCapture(0) ile bilgisayar kamerasi açilir.
Sürekli Döngü (while True):
    Kameradan kare okunur.
    RGB formatindaki görüntü HSV formatina çevrilir.
    Kirmizi renk için alt ve üst HSV degerleri belirlenir.
    cv2.inRange() fonksiyonu ile kirmizi renk tespiti için bir maske olusturulur.
    cv2.bitwise_and() ile sadece kirmizi alanlari içeren bir çikti görüntüsü olusturulur.
    Orijinal görüntü, maske ve sonuç görüntüsü ekranda gösterilir.
    q tusuna basilinca döngü sonlanir.
Kaynaklari Serbest Birakma: Kamera kapatilir ve tüm pencere kapatilir.
"""

"""
Algoritma
Kamerayi aç.
Sonsuz döngü baslat.
    Kameradan bir kare al.
    Görüntüyü HSV renk uzayina çevir.
    Kirmizi renk için alt ve üst esik degerlerini belirle.
    cv2.inRange() ile kirmizi bölgeleri içeren bir maske olustur.
    cv2.bitwise_and() ile sadece kirmizi renkleri içeren bir çikti olustur.
    Orijinal görüntüyü, maskeyi ve sonucu ekranda göster.
    Eger q tusuna basilirse döngüyü kir.
Kamerayi serbest birak ve tüm pencereleri kapat.

"""