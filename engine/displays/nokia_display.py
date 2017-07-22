# -*- coding: utf-8 -*-
from engine.display import Display
try:
	import Adafruit_Nokia_LCD as LCD
	import Adafruit_GPIO.SPI as SPI
	import RPi.GPIO as GPIO
except ImportError as err:
	print err

class Config:
	# Raspberry Pi hardware SPI config:
	DC = 23
	RST = 24
	SPI_PORT = 0
	SPI_DEVICE = 0

	# Display settings
	LIGHT = 18
	CONTRAST = 50

class Nokia(Display):
	WIDTH = 84
	HEIGHT = 48

	_display = None
	_toggle = False

	def __init__(self):
		super(Nokia, self).__init__()
		GPIO.setup(Config.LIGHT, GPIO.OUT)
		self._toggle = False

		self._display = LCD.PCD8544(Config.DC,
									Config.RST,
									spi = SPI.SpiDev(Config.SPI_PORT, Config.SPI_DEVICE, max_speed_hz=4000000))
		self._display.begin(contrast=Config.CONTRAST)
		self.clear()

		pass

	def set_contrast(self, contrast):
		self._display.set_contrast(contrast)
		self._contrast = contrast
		self._display.reset()

	def set_bias(self, bias):
		self._display.set_bias(bias)
		self._bias = bias
		self._display.reset()

	def clear(self):
		self._display.clear()
		self._display.display()

	def toggle_light(self):
		super(Nokia, self).toggle_light()
		GPIO.output(Config.LIGHT, self._toggle)

	def display_frame(self, frame):
		self._display.image(frame)
		self._display.display()
