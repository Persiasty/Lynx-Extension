# -*- coding: utf-8 -*-
import sys
from engine.display import Display

class Console(Display):
	WIDTH = 84
	HEIGHT = 48
	ROWPIXELS = HEIGHT / 6

	def __init__(self):
		super(Console, self).__init__()
		print "Initialized GPIO Light"
		self._toggle = False
		self.clear()

		pass

	def set_contrast(self, contrast):
		self._contrast = contrast
		print "Contrast set to: ", contrast

	def set_bias(self, bias):
		self._bias = bias
		print "Bias set to: ", bias

	def clear(self):
		print "Cleaned"

	def toggle_light(self):
		super(Console, self).toggle_light()
		print "Light is ", self._toggle

	def display_frame(self, frame):
		if frame.mode != '1':
			raise ValueError('Image must be in mode 1.')
		index = 0
		# Iterate through the 6 y axis rows.
		# Grab all the pixels from the image, faster than getpixel.
		pix = frame.load()
		for row in range(Console.HEIGHT):
			for col in range(Console.WIDTH):
				sys.stdout.write(u"#" if(pix[(col, row)]) else u" ")
			sys.stdout.write("\r\n")
