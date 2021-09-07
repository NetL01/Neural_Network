import cv2
import numpy as np

# загружаем изображение, меняем цвет на оттенки серого и уменьшаем резкость
image = cv2.imread("example.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
cv2.imwrite("gray.jpg", gray)

# распознаём контуры
edged = cv2.Canny(gray, 10, 250)
cv2.imwrite("edged.jpg", edged)

# создаём и применяем закрытие
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
cv2.imwrite("closed.jpg", closed)
