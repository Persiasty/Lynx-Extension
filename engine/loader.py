# -*- coding: utf-8 -*-
try:
	import RPi.GPIO as GPIO
except ImportError as err:
	print err

__handlers = []

class Config:
	# Raspberry Pi hardware SPI config:
	DC = 23
	RST = 24
	SPI_PORT = 0
	SPI_DEVICE = 0
	LIGHT = 18

	#Buttons hw config
	BT1 = 4
	BT2 = 17
	BT3 = 27
	BT4 = 22
	BT5 = 25

	BOUNCE_TIME = 300

	#LCD
	CONTRAST = 50

def __input_handler(channel):
	for handler in __handlers:
		handler(channel)

def init_input():
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(Config.BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(Config.BT2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(Config.BT3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(Config.BT4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(Config.BT5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	GPIO.add_event_detect(Config.BT1, GPIO.FALLING, callback=__input_handler, bouncetime=Config.BOUNCE_TIME)
	GPIO.add_event_detect(Config.BT2, GPIO.FALLING, callback=__input_handler, bouncetime=Config.BOUNCE_TIME)
	GPIO.add_event_detect(Config.BT3, GPIO.FALLING, callback=__input_handler, bouncetime=Config.BOUNCE_TIME)
	GPIO.add_event_detect(Config.BT4, GPIO.FALLING, callback=__input_handler, bouncetime=Config.BOUNCE_TIME)
	GPIO.add_event_detect(Config.BT5, GPIO.FALLING, callback=__input_handler, bouncetime=Config.BOUNCE_TIME)

def add_input_handler(handler):
	if(not callable(handler)):
		return

	if(handler in __input_handler):
		return

	handler.append(handler)

