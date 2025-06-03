import cv2
import numpy as np

img = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\kenan.jpeg")

print(f"Piksel Değerleri: {img[100, 50]}")
img[100, 50] = (0, 255, 0)