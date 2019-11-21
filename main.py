from scipy import misc;
import matplotlib.pyplot as plotter

import numpy;
import sys;

if __name__ == '__main__':
  # Change the recursion limit
	sys.setrecursionlimit(10**6);
	rows = 60;
	cols = 60;
  # Init image with zeros
	filtered_img = numpy.zeros((rows, cols));
	print('Test 1 running');
  # Read image in gray scale
	gray_img = misc.imread('manNoisy.png', 1);
  # Show image in gray scale
	plotter.imshow(gray_img, plotter.get_cmap('gray'));
	plotter.show();
	# window_size = 3;
	# filtered_img = imageFilter.medians(gray_img, window_size);
	
	misc.imsave('filtrada.jpg', filtered_img);
	misc.imsave('original.jpg', gray_img);
	print('Terminado!');
	plotter.imshow(filtered_img, plotter.get_cmap('gray'));
	plotter.show();
