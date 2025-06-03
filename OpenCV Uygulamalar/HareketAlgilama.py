import cv2

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    fgmask = fgbg.apply(frame)

    cv2.imshow("Original", frame)
    cv2.imshow("Foreground Mask", fgmask)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()    


"""
Kod Açiklamasi
Bu kod, OpenCV kullanarak bilgisayar kamerasindan gerçek zamanli görüntü alir ve arka plan çikarma (background subtraction) islemi uygular.

Kamera Açma: cv2.VideoCapture(0) ile bilgisayar kamerasi açilir.
Arka Plan Çikarici Olusturma: cv2.createBackgroundSubtractorMOG2() kullanilarak bir arka plan çikarma nesnesi olusturulur.
Sürekli Döngü (while True):
    Kameradan kare okunur.
    Eger görüntü okunamadiysa döngü sonlandirilir.
    fgbg.apply(frame) ile güncel çerçeveden arka plan çikartilarak ön plan maskesi (fgmask) olusturulur.
    Orijinal görüntü ve ön plan maskesi ekranda gösterilir.
    q tusuna basilinca döngü sonlandirilir.
Kaynaklari Serbest Birakma: Kamera kapatilir ve tüm pencereler kapatilir.
"""


"""
Algoritma
Kamerayi aç.
Arka plan çikarma nesnesi olustur.
Sonsuz döngü baslat.
    Kameradan bir kare al.
    Eger kare alinamadiysa döngüyü bitir.
    Arka plan çikarma islemini uygula ve ön plan maskesini al.
    Orijinal görüntüyü ve maskeyi ekranda göster.
    Eger q tusuna basilirse döngüyü kir.
Kamerayi serbest birak ve tüm pencereleri kapat.
"""