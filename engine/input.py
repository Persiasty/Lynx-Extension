# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class Config:
	#Buttons hw config
	BT_UP = 8
	BT_DOWN = 2
	BT_RIGHT = 6
	BT_LEFT = 4
	BT_ENTER = 5

class Input(object):
	__metaclass__ = ABCMeta
	_handler = lambda x: None

	def set_input_handler(self, handler):
		if(handler is None):
			self._handler = lambda x: None
			return

		if(not callable(handler)):
			return

		self._handler = handler