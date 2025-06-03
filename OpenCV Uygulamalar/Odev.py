import cv2

import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV Uygulamalar\UdemyUygulamaGoruntuIsleme\K_Ali.jpeg",0)

cv2.imshow("Ustad", img)

print(img.shape)

imgResized = cv2.resize(img, (int(img.shape[1]*4/5), int(img.shape[0]*4/5)))
cv2.imshow("Yeniden Boyutlandirilan", imgResized)

cv2.putText(img, "Kivircik Ali", (375,100), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0))
cv2.imshow("Kivircik Ali", img)

_, thresh_img = cv2.threshold(img, thresh=50, maxval=255, type=cv2.THRESH_BINARY)
cv2.imshow("Threshold", thresh_img)

gaussBlur = cv2.GaussianBlur(img, ksize=(3,3), sigmaX=7)
cv2.imshow("Gaussian Blur", gaussBlur)

lpc = cv2.Laplacian(img, ddepth=cv2.CV_64F)
cv2.imshow("Laplacian", lpc)

imgHist = cv2.calcHist([img], channels=[0], mask=None, histSize=[256], ranges=[0,256])
plt.figure()
plt.plot(imgHist)

plt.show()