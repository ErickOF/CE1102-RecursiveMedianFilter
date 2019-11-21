import numpy as np


class ImageFilter:
    def medians(self, img, windows_size):
        filtered = np.zeros(img.shape)
        return self.__medians_aux(img, filtered, windows_size, 0, 0)

    def __medians_aux(self, img, filtered, windows_size, i, j):
        print(i, j)
        if i == img.shape[0]:
            return filtered
        elif j == img.shape[1]:
            return self.__medians_aux(img, filtered, windows_size, i + 1, 0)
        else:
            filtered[i][j] = self.__get_new_pixel(img, windows_size, i, j)
            return self.__medians_aux(img, filtered, windows_size, i, j + 1)

    def __get_new_pixel(self, img, windows_size, i, j):
        return img[i][j]
