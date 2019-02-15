cv2.imshow("images", np.hstack([image, cikti]))
Program Kodu:

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
image = cv2.imread("pokemon.png")
# renk kodları listesi
renkler = [
([17, 15, 100], [50, 56, 200]),
([86, 31, 4], [220, 88, 50]),
([25, 146, 190], [62, 174, 250]),
([103, 86, 65], [145, 133, 128])
]
# en alt ve en üst sınırları belirleme
for (dusuk, yuksek) in renkler:
# en alt ve en üst sınırları Numpy dizisi haline getirme
dusuk = np.array(dusuk, dtype="uint8")
yuksek = np.array(yuksek, dtype="uint8")
# sınırlara göre maskeleme işlemi yap
mask = cv2.inRange(image, dusuk, yuksek)
cikti = cv2.bitwise_and(image, image, mask=mask)
# resimi göster
cv2.imshow("images", np.hstack([image, cikti]))
cv2.waitKey(0)