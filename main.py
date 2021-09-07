import cv2
import numpy as np

# загружаем изображение, меняем цвет на оттенки серого и уменьшаем резкость
image = cv2.imread("example.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
cv2.imwrite("gray.jpg", gray)


