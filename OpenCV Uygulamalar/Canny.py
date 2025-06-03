import cv2
import numpy

# 1. Görüntüyü yükleyelim
image = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\trafik-stok.png")
cv2.imshow("Gorsel", image)

# 2. Görüntüyü gri seviyeye çevirelim
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gri Goruntu", gray)

# 3. Gürültüyü azaltmak için Gaussian Blur uygulayalım
blurred = cv2.GaussianBlur(gray, (5,5), 0)
cv2.imshow("Bulanik Goruntu", blurred)

# 4. Canny kenar tespiti yapalım
edges = cv2.Canny(blurred, 50, 150)
cv2.imshow("Kenar tespiti", edges)


cv2.waitKey(0)
cv2.destroyAllWindows()



"""
Kod Açıklaması
Görüntünün Yüklenmesi:

cv2.imread('example.jpg'): Görüntüyü okur.
cv2.imshow('Orijinal Görüntü', image): Orijinal görüntüyü ekranda gösterir.
Gri Tonlamaya Çevirme:

cv2.cvtColor(image, cv2.COLOR_BGR2GRAY): Renkli görüntüyü gri tonlamalı hale getirir.
Kenar tespiti algoritmaları gri seviyede daha verimli çalışır.
Gaussian Blur Uygulama:

cv2.GaussianBlur(gray, (5,5), 0): Gürültüyü azaltarak kenar tespitinin daha doğru yapılmasını sağlar.
Canny Edge Detection:

cv2.Canny(blurred, 50, 150):
50 ve 150, kenar belirleme için alt ve üst eşik değerleridir.
Daha yüksek üst eşik, daha az ama belirgin kenarları tespit eder.
Daha düşük alt eşik, fazla gürültü içeren kenarlar çıkarabilir.
Sonuçları Gösterme:

cv2.imshow('Kenar Tespiti', edges): Kenar tespit edilen görüntüyü ekranda gösterir.
cv2.waitKey(0) ve cv2.destroyAllWindows(): Pencerelerin açık kalmasını ve programın bitince kapanmasını sağlar.
Bu örnek, kenarları belirgin hale getirerek nesne tespitine yardımcı olabilir. Örneği kendi görüntünüzle çalıştırarak farklı eşik değerleriyle oynayabilirsiniz.
"""