# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class Fonts:
	NovaMono = "fonts/NovaMono.ttf"
	SilkScreen = "fonts/SilkScreen.ttf"

class Scene(object):
	_display = None
	_buffer = None

	def __init__(self):
		pass

	def set_display(self, display):
		self._display = display

	def update(self):
		pass

	def action(self, channel):
		pass

	def _make_base(self):
		image = Image.new('1', (self._display.WIDTH, self._display.HEIGHT))
		draw = ImageDraw.Draw(image)
		draw.rectangle((0, 0, self._display.WIDTH, self._display.HEIGHT), outline="white", fill="white")

		return (image, draw)

	def _load_font(self, fontfile=None, size=8):
		font = None
		if(fontfile is not None):
			font = ImageFont.truetype(fontfile, size)
		else:
			font = ImageFont.load_default()
		return font