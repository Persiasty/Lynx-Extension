# -*- coding: utf-8 -*-
from engine.scenes import Scene
from engine.scenes import Fonts
from engine.input import Config
from engine import processor

from engine import utils

class Menu(Scene):
	__options = None
	__currentPosition = 0
	__currentSelectorPosition = 0

	def __init__(self, options):
		super(Menu, self).__init__()
		self.__options = options

	def __down(self):
		options_size = len(self.__options)
		self.__currentPosition = (self.__currentPosition + 1) % options_size
		self.__currentSelectorPosition = self.__currentPosition

	def __up(self):
		self.__currentPosition = max(self.__currentPosition - 1, 0)
		self.__currentSelectorPosition = max(self.__currentSelectorPosition - 1, 0)

	def action(self, channel):
		if(channel == Config.BT_UP): self.__up()
		elif(channel == Config.BT_DOWN): self.__down()
		#TODO: selected option action on enter

	def update(self):
		image, draw = self._make_base()
		font = self._load_font(Fonts.SilkScreen)
		ascend, descend = font.getmetrics()

		self.__currentSelectorPosition = min(self.__currentSelectorPosition, self._display.HEIGHT / (ascend + descend) - 1)

		cutter = self.__currentPosition - self.__currentSelectorPosition
		line_offset = 0
		# if(title is not None):
		# 	line_offset += 1
		for option in self.__options[cutter:]:
			y_off = line_offset * (ascend + descend)

			if (y_off + ascend + descend > self._display.HEIGHT):
				break

			line = option.name
			if (line_offset == self.__currentSelectorPosition):
				line = "> " + line

			draw.text((0, y_off), utils.normalize_polish_leters(line), font=font)

			line_offset += 1

		# if (title is not None):
		# 	draw.rectangle((0, 0, self._display.WIDTH, ascend + descend), outline=0, fill=0)
		# 	draw.text((0, 0), utils.normalize_polish_leters(title), font=font, fill=255)

		return image

class MenuOption:
	name = None
	action = None
	def __init__(self, name, action = None):
		self.name = name
		if(action is not None):
			self.action = action
		else:
			self.action = MenuOption.empty_action

	@staticmethod
	def empty_action():
		pass

def init_menu(options):
	processor.set_scene(Menu(options))