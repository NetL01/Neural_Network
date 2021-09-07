import cv2
import numpy as np
import matplotlib.pyplot as plt


def Origin_histogram(img):
    # Создайте таблицу соответствия между значением серого каждого уровня серого исходного изображения и количеством пикселей
    histogram = {}
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            k = img[i][j]
            if k in histogram:
                histogram[k] += 1
            else:
                histogram[k] = 1

    sorted_histogram = {}  # Создать отсортированную таблицу сопоставления
    sorted_list = sorted(histogram)  # Сортировка от низкого до высокого в соответствии со значением серого

    for j in range(len(sorted_list)):
        sorted_histogram[sorted_list[j]] = histogram[sorted_list[j]]

    return sorted_histogram


def equalization_histogram(histogram, img):
    pr = {}  # Создать таблицу отображения распределения вероятностей

    for i in histogram.keys():
        pr[i] = histogram[i] / (img.shape[0] * img.shape[1])

    tmp = 0
    for m in pr.keys():
        tmp += pr[m]
        pr[m] = max(histogram) * tmp

    new_img = np.zeros(shape=(img.shape[0], img.shape[1]), dtype=np.uint8)

    for k in range(img.shape[0]):
        for l in range(img.shape[1]):
            new_img[k][l] = pr[img[k][l]]

    return new_img


def GrayHist(img):
    # Рассчитать серую гистограмму
    height, width = img.shape[:2]
    grayHist = np.zeros([256], np.uint64)
    for i in range(height):
        for j in range(width):
            grayHist[img[i][j]] += 1
    return grayHist


if __name__ == '__main__':
    # Прочитать оригинальное изображение
    img = cv2.imread('example.jpg', cv2.IMREAD_GRAYSCALE)
    # Рассчитать гистограмму градаций серого исходного изображения
    origin_histogram = Origin_histogram(img)
    # Выравнивание гистограммы
    new_img = equalization_histogram(origin_histogram, img)

    origin_grayHist = GrayHist(img)
    equaliza_grayHist = GrayHist(new_img)
    x = np.arange(256)
    # Нарисовать гистограмму в оттенках серого
    cv2.imwrite("backtrack.jpg", new_img)
    image = cv2.imread("example1.jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)

    edged = cv2.Canny(gray, 10, 250)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite("result_smoke.jpg", closed)


