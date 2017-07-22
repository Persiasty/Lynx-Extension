# -*- coding: utf-8 -*-
from engine.input import Input, Config

try:
	import RPi.GPIO as GPIO
except ImportError as err:
	print err

class RPi_GPIO(Input):
	BOUNCE_TIME = 300

	_handler = None
	def __init__(self):
		super(RPi_GPIO, self).__init__()

		Config.BT_UP = 4
		Config.BT_DOWN = 17
		Config.BT_RIGHT = 27
		Config.BT_LEFT = 22
		Config.BT_ENTER = 25

		GPIO.setmode(GPIO.BCM)

		GPIO.setup(Config.BT_UP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(Config.BT_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(Config.BT_RIGHT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(Config.BT_LEFT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(Config.BT_ENTER, GPIO.IN, pull_up_down=GPIO.PUD_UP)

		GPIO.add_event_detect(Config.BT_UP, GPIO.FALLING, callback=self._handler, bouncetime=RPi_GPIO.BOUNCE_TIME)
		GPIO.add_event_detect(Config.BT_DOWN, GPIO.FALLING, callback=self._handler, bouncetime=RPi_GPIO.BOUNCE_TIME)
		GPIO.add_event_detect(Config.BT_RIGHT, GPIO.FALLING, callback=self._handler, bouncetime=RPi_GPIO.BOUNCE_TIME)
		GPIO.add_event_detect(Config.BT_LEFT, GPIO.FALLING, callback=self._handler, bouncetime=RPi_GPIO.BOUNCE_TIME)
		GPIO.add_event_detect(Config.BT_ENTER, GPIO.FALLING, callback=self._handler, bouncetime=RPi_GPIO.BOUNCE_TIME)
