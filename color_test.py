import unittest

class color_test(unittest.TestCase)

def test_convertColorDepth_ErrorIfNotInColorRange(self, color):  # Checks if the color value is bigger than 255 or smaller than 0
	"""
	Arguments:
	- self: The main object pointer
	- color: The integer color value to convert to 0-255
	"""

	if color > 255 or < 0:
	print "Error: color is out of the range! (0 - 255)"
	else:
	return int ((color / 65535.0) * 255 )
	
	#how to use the assert methods in this case?
