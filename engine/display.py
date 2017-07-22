# -*- coding: utf-8 -*-
try:
	import Adafruit_Nokia_LCD as LCD
	import Adafruit_GPIO.SPI as SPI
	import RPi.GPIO as GPIO
except ImportError as err:
	print err

from loader import Config as Config

class Display:
	WIDTH = 84
	HEIGHT = 48

	_display = None
	_toggle = False

	def __init__(self):
		GPIO.setup(Config.LIGHT, GPIO.OUT)
		self._toggle = False

		self._display = LCD.PCD8544(Config.DC, Config.RST, spi=SPI.SpiDev(Config.SPI_PORT, Config.SPI_DEVICE, max_speed_hz=4000000))
		self._display.begin(contrast=Config.CONTRAST)
		self.clear()

		pass

	def set_contrast(self, contrast):
		self._display.set_contrast(contrast)
		self._display.reset()

	def set_bias(self, bias):
		self._display.set_bias(bias)
		self._display.reset()

	def clear(self):
		self._display.clear()
		self._display.display()

	def toggle_light(self):
		self._toggle = not self._toggle
		GPIO.output(Config.LIGHT, self._toggle)

	def display_frame(self, frame):
		self._display.image(frame)
		self._display.display()

def init_display():
	return Display()

class Test:
	WIDTH = 84
	HEIGHT = 48

	_toggle = False

	def __init__(self):
		print "Initialized GPIO Light"
		self._toggle = False

		print "Initialized SPI LCD with contast: ", Config.CONTRAST
		self.clear()

		pass

	def set_contrast(self, contrast):
		print "Contrast set to: ", contrast

	def set_bias(self, bias):
		print "Bias set to: ", bias

	def clear(self):
		print "Cleaned"

	def toggle_light(self):
		self._toggle = not self._toggle
		print "Light is ", self._toggle

	def display_frame(self, frame):
		frame.show()

def init_test():
	return Test()