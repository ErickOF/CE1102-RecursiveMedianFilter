import numpy as np


class Filter:
    def __init__(self, row_number: int, col_number: int):
        """Filter class

        Args:
            row_number (int): number of rows
            col_number (int): number of columns
        """
        self.__row_number: int = row_number
        self.__col_number: int = col_number

    def median(self, gray_img: np.ndarray, window_size: int,
               filtered_img: np.ndarray) -> None:
        """Filter image using median method

        Args:
            gray_img (np.ndarray): image to filter
            window_size (int): window size of the filter
            filtered_img (np.ndarray): output with the filtered image
        """
        self.__filter(gray_img, window_size // 2, filtered_img)

    def __filter(self, gray_img: np.ndarray, mid_window: int,
                 filtered_img: np.ndarray, i: int = 0) -> None:
        """Auxiliary function

        Args:
            gray_img (np.ndarray): image to filter
            mid_window (int): mid of the window
            filtered_img (np.ndarray): output with the filtered image
            i (int): current row
        """
        # End of the image
        if (i == self.__row_number - mid_window):
            return
        # Filter image
        else:
            # Filter row
            self.__filter_row(gray_img, mid_window, filtered_img, i)
            # Next row
            self.__filter(gray_img, mid_window, filtered_img, i + 1)
    
    def __filter_row(self, gray_img: np.ndarray, mid_window: int,
                     filtered_img: np.ndarray, i: int, j: int = 0) -> None:
        """Filter by row

        Args:
            gray_img (np.ndarray): image to filter
            mid_window (int): mid of the window
            filtered_img (np.ndarray): output with the filtered image
            i (int): current row
            j (int): current column
        """
        # End of the row
        if (j == self.__col_number - mid_window):
            return
        else:
            # Get the new pixel for the image
            filtered_img[i, j] = self.__get_median(gray_img, mid_window, i, j)
            # Next pixel
            self.__filter_row(gray_img, mid_window, filtered_img, i, j + 1)

    def __get_median(self, gray_img: np.ndarray, mid_window: int, i: int,
                     j: int) -> float:
        """Get the median of the window

        Args:
            gray_img (np.ndarray): input image
            mid_window (int): mid of the window
            i (int): current row of the image
            j (int): current column of the image

        Returns:
            float: median of the window
        """
        # Get window
        window: np.ndarray = gray_img[max(0, i - mid_window):min(i + mid_window + 1, self.__row_number),
                                      max(0, j - mid_window):min(j + mid_window + 1, self.__col_number)].flatten()
        self.__sort(window, window.size)

        # Return median of the window
        return window[window.size // 2]

    def __sort(self, array: np.array, i: int, j: int = 1) -> None:
        """Sorting using bubble algorithm

        Args:
            array (np.array): array to sort
            i (int): current index of the array
            j (int): pivote
        """
        # Array is sorted
        if (i == 0):
            return
        # Start again
        elif (j == i):
            self.__sort(array, i - 1, 1)
        else:
            # Check if the previous element is greater
            if (array[j - 1] > array[j]):
                array[j - 1], array[j] = array[j], array[j - 1]

            # Next element
            self.__sort(array, i, j + 1)
