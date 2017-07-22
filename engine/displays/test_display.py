# -*- coding: utf-8 -*-
from engine.display import Display

class Test(Display):
	WIDTH = 84
	HEIGHT = 48

	def __init__(self):
		super(Test, self).__init__()
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
		super(Test, self).toggle_light()
		print "Light is ", self._toggle

	def display_frame(self, frame):
		frame.show()
