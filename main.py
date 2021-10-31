# -*- coding: utf-8 -*-
'''
Created on Tue Apr 12 15:36 2016
Last update on Sat 16 10:57 2021
'''

__author__ = "Erick Andres Obregon Fonseca"
__copyright__ = "Copyright 2021"
__credits__ = []
__license__ = "GPL"
__version__ = "1.1"
__maintainer__ = "Erick Andres Obregon Fonseca"
__email__ = "erickobregonf@gmail.com"
__status__ = "Production"


import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import sys

from imgfilter import Filter


def main():
    sys.setrecursionlimit(10**9)

    # Open image
    img_path: str = input('Path of the image: ')
    gray_img = np.asarray(Image.open(img_path).convert('L'))

    # Show gray image
    plt.imshow(gray_img, plt.get_cmap('gray'))
    plt.title('Gray image')
    plt.show()

    # Get image dimensions
    dim: tuple = gray_img.shape

    # Ask for window size
    window_size: int = int(input('Window size of the filter: '))

    # Empty image for result
    filtered_img: np.ndarray = np.zeros(dim)

    # Filter instance
    filter: Filter = Filter(dim[0], dim[1]) 

    # Filter image
    filter.median(gray_img, window_size, filtered_img)

    # Show filtered image
    plt.imshow(filtered_img, plt.get_cmap('gray'))
    plt.title('Filtered image')
    plt.show()

    # Save filtered image
    filtered_img_path: str = input('Filtered image path and name to save: ')
    plt.imsave(filtered_img_path, filtered_img)

    print('Image saved successfully!')
    print('Finished!')


if __name__ == '__main__':
    main() 
