import cv2
import mediapipe as mp

"""
cv2 → OpenCV kutuphanesi, goruntu isleme ve kamera kullanimi icin.
mediapipe → Google'in gelistirdigi el takibi modelini kullanabilmemiz icin.
"""

# MediaPipe modüllerini başlat
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

"""
mp.solutions.hands → El takibi modelini iceren MediaPipe modulu.
mp.drawing_utils → Elin eklem noktalarini ve bunlar arasindaki baglantilari cizmek icin kullanilir.
"""


# El algılama modelini başlat
hands = mp_hands.Hands(min_detection_confidence = 0.5, min_tracking_confidence = 0.5 )

"""
Hands() → El tespiti icin MediaPipe'nin el algilama modelini baslatir.
min_detection_confidence = 0.5 → Elin tespit edilmesi icin gereken minimum guven seviyesi.
min_tracking_confidence = 0.5 → Elin izlenmesi icin gereken minimum guven seviyesi.
"""

# Kamerayı aç
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    """
    cap.isOpened() → Kamera aciksa, while dongusu baslar.
    cap.read() → Kameradan bir kare alinir. ret True doner, frame ise bu karenin goruntusudur.
    if not ret → Kare alinamazsa (kamera problemi vb.), dongu sonlanir.
    """
    # BGR'den RGB'ye çevir (MediaPipe RGB formatını kullanır)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # El tespiti yap
    result = hands.process(rgb_frame)

    """
    hands.process() → MediaPipe el tespit modelini kullanarak, goruntu uzerindeki elleri ve eklem noktalarini tespit eder. Sonuc result degiskenine atanir.
    """

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Elin eklem noktalarını çiz
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            """
            result.multi_hand_landmarks → Birden fazla el tespit edilirse, her birinin eklem noktalarina erisilmesini saglar.
            mp_drawing.draw_landmarks() → Her bir elin eklem noktalarini ve bu noktalar arasindaki baglantilari cizer.
            """

            # Elin eklem noktalarının koordinatlarını al ve ekrana yazdır
            for id, landmark in enumerate(hand_landmarks.landmark):
                h, w, _ = frame.shape
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                cv2.putText(frame, str(id), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

            """
            enumerate(hand_landmarks.landmark) → Her bir eklem noktasini, ID'si ile birlikte gezdirir.
            cx, cy → Her bir eklem noktasinin x ve y koordinatlari, goruntunun boyutuna orantilanarak hesaplanir.
            cv2.putText() → Bu koordinatlara eklem numarasini yazar.

            """

    # Görüntüyü ekranda göster
    cv2.imshow("El Takibi", frame)

    # "q" tuşuna basınca çık
    if cv2.waitKey(1) & 0xFF == ord( "q"):
        break

# Temizlik işlemleri
cap.release()
cv2.destroyAllWindows()    


"""

📌 Algoritma
Gerekli kutuphaneleri ice aktar

OpenCV ve MediaPipe kutuphaneleri yuklenir.
MediaPipe el tespiti modelini baslat

mp_hands: El algilama modeli baslatilir.
mp_drawing: Tespit edilen eklem noktalarini cizmek icin kullanilir.
Hands() fonksiyonu ile el tespit modeli olusturulur.
Kamera baslat

Bilgisayarin kamerasi acilir (cv2.VideoCapture(0)).
Gercek zamanli video akisinda el tespiti yap

Kameradan alinan her kare BGR'den RGB'ye cevrilir.
MediaPipe modeli bu goruntu uzerinde el tespiti yapar.
Elin eklem noktalarini tespit et ve ekrana yazdir

Eger el tespit edilirse, 21 eklem noktasinin (x, y) koordinatlari alinir.
Her eklem noktasi bir numara ile isaretlenir ve goruntu uzerine yazilir.
Goruntuyu ekranda goster ve cikis kontrolu yap

cv2.imshow() ile goruntu gosterilir.
Kullanici "q" tusuna bastiginda dongu sonlanir.

"""