# -*- coding: utf-8 -*-
import threading

from engine.input import Input, Config

class Keyboard(Input):

	def __init__(self):
		super(Keyboard, self).__init__()
		threading.Thread(target=self.keyboard_worker).start()

	def keyboard_worker(self):
		while(True):
			inp = raw_input()
			try:
				input_num = int(inp)
				if(input_num in [Config.BT_UP, Config.BT_DOWN, Config.BT_RIGHT, Config.BT_LEFT, Config.BT_ENTER]):
					self._handler(input_num)
			except:
				pass
