import cv2
import cv2.data

#Görüntüdeki Yüzleri Algılama (Haar Cascade Classifier)

# 1. Yüz algılama için Haar Cascade sınıflandırıcıyı yükleyelim
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# 2. Görüntüyü yükleyelim
image = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\yuz.jpg")

# 3. Görüntüyü gri tonlamaya çevirelim
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 4. Yüzleri tespit edelim
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# 5. Tespit edilen yüzleri dikdörtgenle çizelim
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Sonucu gösterelim
cv2.imshow("Yüz Algilama", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
