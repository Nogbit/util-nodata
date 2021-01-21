import sys
from os import walk
import numpy as np
from PIL import Image

# converts to grayscale, then returns a percentage at the threshold
def blackness(path, threshold):
	image = Image.open(path).convert('L')
	pixels = np.asarray(image)
	threshold_level = threshold
	coords = np.column_stack(np.where(pixels < threshold_level))
	return round(coords.size / (pixels.size * 2), 2)

# assumes a single arg of something like... '/home/you/2015/tiffs'
path = sys.argv[1]

_, _, filenames = next(walk(path))
for i in filenames:
	file_name = path + '/' + i
	percent_black = blackness(file_name, 1)
	print('{0}	{1}'.format(percent_black, file_name))