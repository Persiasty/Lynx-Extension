# -*- coding: utf-8 -*-
from engine.scenes import Scene
from engine.scenes import Fonts
from engine import processor

import menu

import time

class Splash(Scene):
	__firstUpdateTime = 0

	def __init__(self):
		super(Splash, self).__init__()

	def update(self):
		if(self._buffer is None):
			self._buffer = self.__display_splash()
			self.__firstUpdateTime = time.time()

		if(time.time() - self.__firstUpdateTime > 3):
			#TODO: move to menu when enter clicked
			#TODO: add clock?
			menu.init_mainmenu()
		return self._buffer

	def __display_splash(self):
		image, draw = self._make_base()
		font = self._load_font(Fonts.NovaMono, 32)

		draw.rectangle((0, 0), fill="black", outline="black")
		draw.text((8, 0), "Lynx", font=font, fill="white")

		return image

def init_splash_screen():
	processor.set_scene(Splash())
