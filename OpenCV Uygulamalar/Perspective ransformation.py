import cv2
import numpy as np

image = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\joker.jpg")

# 2. perspektif dönüşüm için dört nokta seçelim
# Bu noktalar, orijinal görüntüdeki dört köşe noktası olmalı
pts1 = np.float32([[50,50],[200,50],[50,200],[200,200]]) # Kaynak noktaları
pts2 = np.float32([[10,100], [300, 50], [100, 250], [300,300]]) # Hedef noktalar

# 3. Perspektif dönüşüm matrisini hesaplayalım
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# 4. Perspektif dönüşümü uygulama
result = cv2.warpPerspective(image, matrix, (image.shape[1], image.shape[0]))

cv2.imshow("Orijinal Goruntu", image)
cv2.imshow("Perspektif Goruntu", result)

cv2.waitKey(0)
cv2.destroyAllWindows()


"""
Kod Açıklaması
Görüntüyü Yükleme:
cv2.imread() ile görüntü yüklenir.

Kaynak ve Hedef Noktalar:
Perspektif dönüşüm için kaydedilecek ve hedeflenen noktalar belirlenir. Bu noktalar, görüntüdeki dört kenar noktasını temsil eder.

Dönüşüm Matrisi Hesaplama:
cv2.getPerspectiveTransform(pts1, pts2) ile bir dönüşüm matrisi oluşturulur. Bu matris, kaynak noktaları hedef noktalara dönüştürür.

Perspektif Dönüşüm:
cv2.warpPerspective() ile perspektif dönüşüm uygulanır. Bu işlem, görüntüyü yeni açıyla gösterir.


"""