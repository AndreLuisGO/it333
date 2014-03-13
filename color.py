def _convertColorDepth(self, color):
	"""
	Converts from 16 to 8 bit color depth. Necessary
	for OpenCV functions and GDK colors to interact as the
	former expects colors from 0-255 and the latter expects
	0-65535.
	
	Arguments:
	- self: The main object pointer
	- color: The integer color value to convert to 0-255
	"""
	return int ((color / 65535.0) * 255 )
