import cv2

# Görüntüyü yükle
img = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\kenan.jpeg")

# Görüntünün yüklenip yüklenmediğini kontrol et
if img is None:
    print("Görüntü yüklenemedi! Dosya yolunu kontrol edin.")
else:
    # Görüntüye metin ekleme
    cv2.putText(img, "Kenan Yildiz", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 
                1, (0, 255, 0), 2, cv2.LINE_AA)

    # Görüntüyü gösterme
    cv2.imshow("Metin Eklenmis Goruntu", img)

    # Pencerenin açık kalmasını sağla
    cv2.waitKey(0)
    cv2.destroyAllWindows()
