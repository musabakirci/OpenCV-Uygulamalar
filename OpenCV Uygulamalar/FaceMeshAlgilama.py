import cv2
import mediapipe as mp

# MediaPipe Face Mesh modelini yükle
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

"""
mp_face_mesh: MediaPipe kütüphanesinde yer alan yüz mesh modeline referans verir. Bu model yüz üzerindeki 468 farkli noktayi tespit eder.
mp_drawing: Yüzdeki tespit edilen noktalari çizmek için kullanilan yardimci fonksiyonlari içerir.
mp_drawing_styles: Çizim stillerini içerir. Çizim için farkli stiller seçilebilir.
"""

# kamera baslatma
cap = cv2.VideoCapture(0)

# Face Mesh modelini başlat
with mp_face_mesh.FaceMesh(
    static_image_mode = False,
    max_num_faces = 1,
    refine_landmarks = True,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5
) as face_mesh:

    """
    mp_face_mesh.FaceMesh: MediaPipe yüz mesh modelini başlatir. Yüzleri analiz etmek için bu modeli kullanacağiz.
    static_image_mode=False: Kameradan alinan sürekli akişla çalişacağimiz için bu parametre False yapilir. Eğer bir fotoğraf üzerinden çalişmak istenirse True yapilir.
    max_num_faces=1: Ayni anda yalnizca bir yüz tespit edilmesini sağlar.
    refine_landmarks=True: Yüzdeki noktalari daha hassas bir şekilde tespit eder.
    min_detection_confidence=0.5: Yüz algilamada minimum güven eşiği. Yüz algilandiğinda, doğruluk orani bu değerin üzerinde olmali.
    min_tracking_confidence=0.5: Yüz takip etme için minimum güven eşiği. Yüz tespit edildikten sonra, modelin yüzü izlemeye devam etme güveni.
    """    


    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        """
        while cap.isOpened(): Kameradan gelen video akişi açik olduğu sürece bu döngü devam eder.
        ret, frame = cap.read(): Her bir video karesi (frame) alinir. ret değeri, görüntü başariyla alindiysa True, alinamadiysa False döner.
        if not ret: Eğer kare alinamazsa (ret == False), döngüden çikilir.
        """

        # Görüntüyü RGB formatına çevir (MediaPipe için gerekli)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


        # Yüz mesh işlemi uygula
        result = face_mesh.process(rgb_frame)

        # Eğer yüz algılandıysa landmark'ları çiz
        if result.multi_face_landmarks:
            for face_landmarks in result.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    face_landmarks,
                    mp_face_mesh.FACEMESH_TESSELATION,
                    mp_drawing_styles.get_default_face_mesh_tesselation_style()
                )

                """
                if result.multi_face_landmarks: Yüz algilanip, yüz noktalari (landmarks) başariyla tespit edilirse, bu kismin içi çalişir.
                for face_landmarks in result.multi_face_landmarks: Eğer birden fazla yüz varsa, her yüz için bu döngü çalişir. Ancak burada max_num_faces=1 olduğu için sadece bir yüz tespit edilir.
                mp_drawing.draw_landmarks: Bu fonksiyon, tespit edilen yüzün üzerine çizim yapar.
                frame: Çizimin yapilacaği görüntü.
                face_landmarks: Yüzdeki tespit edilen önemli noktalar (landmark'lar).
                mp_face_mesh.FACEMESH_TESSELATION: Yüzdeki tüm noktalara çizgi ile bağlanti yapacak şekilde yüzün ağ yapisini çizmek için kullanilir.
                mp_drawing_styles.get_default_face_mesh_tesselation_style(): Çizim stilini belirler.
                """

        # Görüntüyü ekrana göster
        cv2.imshow("Face Mesh", frame)

        # "q" tuşuna basılırsa çık
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

# Kamerayı kapat
cap.release()
cv2.destroyAllWindows()



"""
Algoritma:
Gerekli Kütüphanelerin İçe Aktarilmasi:

cv2: OpenCV, görüntü işleme için kullanilir.
mediapipe: MediaPipe, yüz tespiti ve çeşitli görüntü işleme görevleri için kullanilir.
MediaPipe Face Mesh Modeli Başlatma:

mp.solutions.face_mesh: MediaPipe Face Mesh modelini yükler.
mp_drawing: Landmark'lari çizmek için kullanilir.
mp_drawing_styles: Yüz üzerinde çizim stilini belirlemek için kullanilir.
Kamerayi Başlatma:

cv2.VideoCapture(0): Bilgisayarin varsayilan kamerasini başlatir.
Face Mesh Modelinin Yapilandirilmasi:

static_image_mode = False: Kamera ile sürekli bir görüntü akişi kullanacağimiz için bu parametre False olarak ayarlanir.
max_num_faces = 1: Maksimum tespit edilecek yüz sayisi (1 yüz tespit etmeye çalişiyoruz).
refine_landmarks = True: Landmark'lari daha hassas bir şekilde tespit etmek için aktif edilir.
min_detection_confidence = 0.5: Yüzün algilanabilmesi için minimum güven seviyesi.
min_tracking_confidence = 0.5: Yüz tespiti sürekli takip edilebilmesi için minimum takip güveni seviyesi.
Video Akişinin Sürekli İzlenmesi ve İşlenmesi:

while cap.isOpened(): Kamera açildiği sürece döngü çalişir.
ret, frame = cap.read(): Her bir video karesi alinir.
Eğer kare alinamazsa (ret değeri False ise), döngüden çikilir.
cv2.cvtColor(frame, cv2.COLOR_BGR2RGB): OpenCV, renkleri BGR formatinda işler; MediaPipe ise RGB formatini kullanir, bu yüzden görüntü formati dönüştürülür.
Yüz Mesh İşleminin Uygulanmasi:

result = face_mesh.process(rgb_frame): MediaPipe modeline RGB formatindaki görüntü gönderilir ve yüz mesh analizini yapar.
if result.multi_face_landmarks: Eğer yüz veya yüzler tespit edildiyse, tespit edilen her bir yüz için for döngüsü çalişir.
Landmark Çizimi:

mp_drawing.draw_landmarks: Yüz üzerindeki önemli noktalari (landmark'lari) çizer.
frame: Görüntü üzerinde çizim yapilacak olan kare.
face_landmarks: Yüzdeki tespit edilen noktalar.
mp_face_mesh.FACEMESH_TESSELATION: Yüz üzerinde çizilecek tüm yüzey noktalarini belirtir.
mp_drawing_styles.get_default_face_mesh_tesselation_style(): Çizim stilini ayarlar.
Görüntüyü Ekranda Gösterme:

cv2.imshow("Face Mesh", frame): Yüz mesh ile işlenmiş görüntü ekrana yansitilir.
Kullanicidan Çikiş Komutu Alma:

if cv2.waitKey(1) & 0xFF == ord("q"): Kullanici "q" tuşuna bastiğinda, program döngüsünden çikar.
Kaynaklari Serbest Birakma:

cap.release(): Kamera kaynağini serbest birakir.
cv2.destroyAllWindows(): Tüm OpenCV pencerelerini kapatir.
"""