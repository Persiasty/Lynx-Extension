# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class Display(object):
	__metaclass__ = ABCMeta
	WIDTH = 0
	HEIGHT = 0

	_contrast = 0
	_bias = 0

	_toggle = False

	def set_contrast(self, contrast):
		self._contrast = contrast

	def set_bias(self, bias):
		self._bias = bias

	def get_contrast(self):
		return self._contrast

	def get_bias(self):
		return self._bias

	@abstractmethod
	def clear(self):
		pass

	@abstractmethod
	def toggle_light(self):
		self._toggle = not self._toggle

	@abstractmethod
	def display_frame(self, frame):
		pass
