import cv2
import numpy as np

# 1. Büyük resmi ve aramak istediğimiz şablonu yükleyelim
image = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\K_Ali.jpeg") #Büyük resim
template = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\K_Ali2.png", 0) #Aramak istediğimiz nesne (gri)

# 2. Büyük resmi de gri tonlamaya çevirelim 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 3. Şablon eşleme algoritmasını çalıştıralım
result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)

# 4. Eşleşmenin en iyi olduğu konumu bulalım
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# 5. Eşleşen bölgeyi dikdörtgen ile çizelim
w, h = template.shape[::-1]
cv2.rectangle(image, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 0), 2)

#Sonucu gösterelim
cv2.imshow("Eslesen Nesne", image)

cv2.waitKey(0)
cv2.destroyAllWindows()


"""
Kod Açıklaması
Resmi ve Şablonu Yükleme:

scene.jpg: Büyük resim (örneğin bir masa üstü sahnesi).
object.jpg: Aramak istediğimiz nesnenin şablonu.
Griye Çevirme:

cv2.cvtColor(image, cv2.COLOR_BGR2GRAY): Ana sahneyi griye çeviriyoruz.
Şablon Eşleme:

cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED): Şablonun en iyi eşleştiği bölgeyi bulur.
En İyi Eşleşmeyi Bulma:

cv2.minMaxLoc(result): En iyi eşleşme bölgesini belirler.
Eşleşen Alanı İşaretleme:

cv2.rectangle(): Eşleşen nesnenin çevresine yeşil bir dikdörtgen çizer.
"""