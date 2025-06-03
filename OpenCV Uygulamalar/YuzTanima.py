import cv2
import matplotlib.pyplot as plt

# Yüz algılama için Haar Cascade yükleme
face_cascade = cv2.CascadeClassifier(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\UdemyNesneTespiti\haarcascade_frontalface_default.xml")

# ---- Einstein Görüntüsü ----
einstein = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\UdemyNesneTespiti\albert-einstein.jpg")
gray_einstein = cv2.cvtColor(einstein, cv2.COLOR_BGR2GRAY)

# Yüz tespiti
face_rect = face_cascade.detectMultiScale(gray_einstein, scaleFactor=1.1, minNeighbors=5)

# Tespit edilen yüzleri dikdörtgen içine alma
for (x, y, w, h) in face_rect:
    cv2.rectangle(einstein, (x, y), (x + w, y + h), (255, 255, 255), 7)

# Sonucu gösterme
plt.figure()
plt.imshow(cv2.cvtColor(einstein, cv2.COLOR_BGR2RGB))
plt.axis("off")

# ---- Milli Takım Görüntüsü ----
milli_takim = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\UdemyNesneTespiti\MilliTakim.jpg")

# Görüntüyü yeniden boyutlandır (Gerekirse)
milli_takim_resized = cv2.resize(milli_takim, (800, 600))

# Griye çevir
gray_milli_takim = cv2.cvtColor(milli_takim_resized, cv2.COLOR_BGR2GRAY)

# Yüz tespiti
face_rect = face_cascade.detectMultiScale(gray_milli_takim, scaleFactor=1.1, minNeighbors=5)

# Tespit edilen yüzleri dikdörtgen içine alma
for (x, y, w, h) in face_rect:
    cv2.rectangle(milli_takim_resized, (x, y), (x + w, y + h), (255, 255, 255), 7)

# Sonucu gösterme
plt.figure()
plt.imshow(cv2.cvtColor(milli_takim_resized, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.show()
