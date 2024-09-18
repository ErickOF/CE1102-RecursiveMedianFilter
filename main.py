"""
This script applies a median filter to an image provided by the user.
It converts the image to grayscale, applies the median filter with a specified
window size, and then displays and saves the filtered image.

Usage:
1. Run the script.
2. Provide the path to the image file to be filtered.
3. Specify the window size for the median filter.
4. Specify the path and name to save the filtered image.

Author: Erick Andres Obregon Fonseca
"""
import matplotlib.pyplot as plt
import numpy as np
import sys

from PIL import Image
from typing import Tuple

from imgfilter import Filter


def main():
    # Increase recursion limit to prevent RecursionError for large images
    sys.setrecursionlimit(10**9)

    # Open the image
    img_path: str = input('Path of the image: ')
    gray_img: np.ndarray = np.asarray(Image.open(img_path).convert('L'))

    # Display the grayscale image
    plt.imshow(gray_img, plt.get_cmap('gray'))
    plt.title('Gray image')
    plt.show()

    # Get the dimensions of the image
    dim: Tuple[int, int] = gray_img.shape

    # Prompt the user to enter the filter's window size
    window_size: int = int(input('Window size of the filter: '))

    # Create an empty array for the filtered image
    filtered_img: np.ndarray = np.zeros(dim)

    # Create a Filter instance for the image dimensions
    filter: Filter = Filter(dim[0], dim[1])

    # Apply the median filter to the image
    filter.median(gray_img, window_size, filtered_img)

    # Display the filtered image
    plt.imshow(filtered_img, plt.get_cmap('gray'))
    plt.title('Filtered image')
    plt.show()

    # Prompt the user to enter the path and name to save the filtered image
    filtered_img_path: str = input('Filtered image path and name to save: ')
    plt.imsave(filtered_img_path, filtered_img)

    print('Image saved successfully!')
    print('Finished!')


if __name__ == '__main__':
    main()
