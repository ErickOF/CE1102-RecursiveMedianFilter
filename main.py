import matplotlib.pyplot as plt
import sys

from imgfilter import ImageFilter


if __name__ == '__main__':
    # Change the recursion limit
    sys.setrecursionlimit(10**9)
    print('Test 1 running')
    # Read image in gray scale
    # imgs/input/manNoisy.png
    img_path = input('Input image name: ')
    # imgs/output/filter.jpg
    out_path = input('Output image name: ')
    gray_img = plt.imread(img_path, 1)
    # Show image in gray scale
    plt.imshow(gray_img, plt.get_cmap('gray'))
    plt.show()
    # Filter image
    window_size = int(input('Windows size: '))
    img_filter = ImageFilter()
    filtered_img = img_filter.medians(gray_img, window_size)

    plt.imsave(out_path, filtered_img)
    print('Finish!')
    plt.imshow(filtered_img, plt.get_cmap('gray'))
    plt.show()
