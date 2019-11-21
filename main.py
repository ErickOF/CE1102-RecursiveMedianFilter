from scipy import misc;
import matplotlib.pyplot as plt
import sys;

from imgfilter import ImageFilter


if __name__ == '__main__':
    # Change the recursion limit
    sys.setrecursionlimit(10**6);
    print('Test 1 running');
    # Read image in gray scale
    gray_img = misc.imread('imgs/input/manNoisy.png', 1);
    # Show image in gray scale
    plt.imshow(gray_img, plt.get_cmap('gray'));
    plt.show();
    # Filter image
    window_size = 3;
    img_filter = ImageFilter()
    filtered_img = img_filter.medians(gray_img, window_size);
    
    misc.imsave('imgs/output/filter.jpg', filtered_img);
    misc.imsave('imgs/output/original.jpg', gray_img);
    print('Finish!');
    plt.imshow(filtered_img, plt.get_cmap('gray'));
    plt.show();
