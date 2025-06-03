import cv2

# Yüz algilama Modelini yükle
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Kamerayı başlat
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Görüntüyü griye çevir (Haar Cascade gri görüntülerle daha iyi çalışır)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüzleri algıla
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30,30))

    # Algılanan yüzleri dikdörtgen içine al
    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # Görüntüyü ekrana göster
    cv2.imshow("Yuz Algilama", frame)

    # "q" tuşuna basınca çık
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()        


"""
📌 Kod Açiklamasi
1️⃣ Haar Cascade Modelini Yukleme
cv2.CascadeClassifier() fonksiyonu ile OpenCV'nin hazir Haar cascade yuz tespit modelini yukluyoruz.
2️⃣ Gercek Zamanli Kamera Acma
cv2.VideoCapture(0) ile bilgisayar kamerasindan goruntu aliyoruz.
3️⃣ Gri Tonlamaya Cevirme
Haar Cascade modeli gri tonlamali goruntulerde daha iyi calistigi icin cv2.cvtColor() ile donusturme yapiyoruz.
4️⃣ Yuz Algilama
detectMultiScale() fonksiyonu ile yuzler tespit ediliyor.
scaleFactor=1.1 → Yuzun farkli boyutlarda algilanmasini saglayan olcek faktoru.
minNeighbors=5 → Yanlis tespitleri azaltmak icin komsu kutularin sayisini belirler.
minSize=(30, 30) → Minimum algilanabilir yuz boyutu.
5️⃣ Yuz Cizimi
Algilanan yuzlerin etrafina dikdortgen cizmek icin cv2.rectangle() kullaniliyor.
6️⃣ Goruntuyu Gosterme ve Cikis Kontrolu
cv2.imshow() ile goruntu ekrana veriliyor.
'q' tusuna basildiginda dongu sonlandiriliyor.
📌 Algoritma
1️⃣ Baslat
2️⃣ Kutuphaneleri yukle ve Haar Cascade modelini yukle
3️⃣ Kamerayi ac
4️⃣ WHILE dongusu:

Kameradan goruntu al
Goruntuyu gri tonlamaya cevir
Yuz tespiti yap (detectMultiScale kullanarak)
Eger yuz algilandiysa:
Yuzlerin etrafina dikdortgen ciz
Goruntuyu ekranda goster
Eger 'q' tusuna basilirsa donguden cik
5️⃣ Kamerayi kapat ve programi sonlandir

"""
