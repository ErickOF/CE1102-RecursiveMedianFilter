"""
Filter Class for Image Processing

This class provides a median filter for grayscale images. The filter is applied using a recursive 
approach to traverse and process the image. The median filter helps in reducing noise while 
preserving edges by taking the median of the pixels in a specified window around each pixel.

The class provides the following functionalities:
- Median filtering of an image (`median` method).
- Recursive filtering through rows and columns (`__filter` and `__filter_row` methods).
- Extracting the median of a given window in the image (`__get_median` method).
- Sorting the window using the bubble sort algorithm (`__sort` method).

Usage:
1. Instantiate the `Filter` class with the number of rows and columns of the image.
2. Call the `median` method to apply the median filter to the image.

Author: Erick Andres Obregon Fonseca
"""
import numpy as np

from typing import Final


class Filter:
    """
    Filter Class for Image Processing

    This class provides a median filter for grayscale images. The filter is
    applied using a recursive approach to traverse and process the image. The
    median filter helps in reducing noise while  preserving edges by taking
    the median of the pixels in a specified window around each pixel.

    Usage:
    1. Instantiate the `Filter` class with the number of rows and columns of
    the image.
    2. Call the `median` method to apply the median filter to the image.
    """

    def __init__(self, row_number: int, col_number: int):
        """
        Initializes the Filter class with the specified number of rows and
        columns.

        Args:
            row_number (int): Number of rows in the image.
            col_number (int): Number of columns in the image.
        """
        self.__row_number: Final[int] = row_number
        self.__col_number: Final[int] = col_number

    def median(
            self,
            gray_img: np.ndarray,
            window_size: int,
            filtered_img: np.ndarray
        ) -> None:
        """
        Apply a median filter to the image using the specified window size.

        Args:
            gray_img (np.ndarray): Grayscale image to filter.
            window_size (int): Size of the window to calculate the median.
            filtered_img (np.ndarray): Output array to store the filtered
                                       image.
        """
        # Call the private filter method to apply the median filter
        self.__filter(gray_img, window_size // 2, filtered_img)

    def __filter(
            self,
            gray_img: np.ndarray,
            mid_window: int,
            filtered_img: np.ndarray,
            i: int = 0
        ) -> None:
        """
        Recursively filter the image by processing each row.

        Args:
            gray_img (np.ndarray): Grayscale image to filter.
            mid_window (int): Half the window size.
            filtered_img (np.ndarray): Output array to store the filtered
                                       image.
            i (int): Current row being processed.
        """
        # End of the image; stop recursion
        if i == (self.__row_number - mid_window):
            return
        else:
            # Filter the current row
            self.__filter_row(gray_img, mid_window, filtered_img, i)
            # Recur to the next row
            self.__filter(gray_img, mid_window, filtered_img, i + 1)
    
    def __filter_row(
            self, 
            gray_img: np.ndarray,
            mid_window: int,
            filtered_img: np.ndarray,
            i: int,
            j: int = 0
        ) -> None:
        """
        Recursively filter each pixel in the current row.

        Args:
            gray_img (np.ndarray): Grayscale image to filter.
            mid_window (int): Half the window size.
            filtered_img (np.ndarray): Output array to store the filtered
                                       image.
            i (int): Current row being processed.
            j (int): Current column being processed.
        """
        # End of the row; stop recursion
        if j == (self.__col_number - mid_window):
            return
        else:
            # Get the median value for the current window and update the pixel
            filtered_img[i, j] = self.__get_median(gray_img, mid_window, i, j)
            # Recur to the next pixel in the row
            self.__filter_row(gray_img, mid_window, filtered_img, i, j + 1)

    def __get_median(
            self,
            gray_img: np.ndarray,
            mid_window: int,
            i: int,
            j: int
        ) -> float:
        """
        Calculate the median of the pixel values in the specified window.

        Args:
            gray_img (np.ndarray): Grayscale image.
            mid_window (int): Half the window size.
            i (int): Current row of the image.
            j (int): Current column of the image.

        Returns:
            float: Median of the pixel values in the window.
        """
        # Extract the window around the current pixel and flatten it into a 1D
        # array
        window: np.ndarray = gray_img[max(0, i - mid_window):min(i + mid_window + 1, self.__row_number),
                                      max(0, j - mid_window):min(j + mid_window + 1, self.__col_number)].flatten()
        # Sort the window to find the median
        self.__sort(window, window.size)

        # Return the median value of the window
        return window[window.size // 2]

    def __sort(self, array: np.array, i: int, j: int = 1) -> None:
        """
        Sort the array using the bubble sort algorithm.

        Args:
            array (np.array): Array to be sorted.
            i (int): Current index of the array being processed.
            j (int): Pivot index for the current sorting pass.
        """
        # Array is sorted; stop recursion
        if i == 0:
            return
        # Reset j to 1 and reduce i for the next pass
        elif j == i:
            self.__sort(array, i - 1, 1)
        else:
            # Swap if the previous element is greater than the current element
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]

            # Recursive to the next element in the current pass
            self.__sort(array, i, j + 1)
