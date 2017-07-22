# -*- coding: utf-8 -*-
from engine.scenes import Scene
from engine.scenes import Fonts

from engine import utils

#TODO: Not tested
class TexReader(Scene):
	__offset = (0, 0)
	__title = None
	__lines = None

	def __init__(self, lines, title=None):
		super(TexReader, self).__init__()
		self.__lines = lines
		self.__title = title

	def update(self):
		image, draw = self._make_base()
		font = self._load_font(Fonts.SilkScreen)
		ascend, descend = font.getmetrics()

		ox, oy = self.__offset

		line_no = 0
		if(oy < 0):
			line_no = -int(-oy / (ascend + descend))
		else:
			line_no = int(oy / (ascend + descend))

		line_offset = line_no

		if(self.__title is not None):
			line_offset += 1

		for line in self.__lines[-line_no:]:
			y_off = line_offset * (ascend + descend) + oy
			draw.text((ox, y_off), utils.normalize_polish_leters(line), font=font)
			line_offset += 1

			if(y_off > self._display.HEIGHT + ascend + descend):
				break

		if (self.__title is not None):
			draw.rectangle((0, 0, self._display.WIDTH, ascend + descend), outline=0, fill=0)
			draw.text((0, 0), utils.normalize_polish_leters(self.__title), font=font, fill=255)

		return image