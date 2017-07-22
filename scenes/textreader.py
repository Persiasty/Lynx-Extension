# -*- coding: utf-8 -*-
from engine.scenes import Scene
from engine.scenes import Fonts

from engine import utils

class TexReader(Scene):
	def __init__(self, display):
		super(TexReader, self).__init__(display)

	def display_text(self, lines, title=None, offset=(0, 0)):
		image, draw = self._make_base()
		font = self._load_font(Fonts.SilkScreen)
		ascend, descend = font.getmetrics()

		ox, oy = offset

		line_no = 0
		if(oy < 0):
			line_no = -int(-oy / (ascend + descend))
		else:
			line_no = int(oy / (ascend + descend))

		line_offset = line_no

		if(title is not None):
			line_offset += 1

		for line in lines[-line_no:]:
			y_off = line_offset * (ascend + descend) + oy
			draw.text((ox, y_off), utils.normalize_polish_leters(line), font=font)
			line_offset += 1

			if(y_off > self._display.HEIGHT + ascend + descend):
				break

		if (title is not None):
			draw.rectangle((0, 0, self._display.WIDTH, ascend + descend), outline=0, fill=0)
			draw.text((0, 0), utils.normalize_polish_leters(title), font=font, fill=255)

		return image