# -*- coding: utf-8 -*-
from engine import processor as LynxCore
from engine.displays import con_display as LynxDisplay
from engine.displays import test_display as LynxDisplay
from engine.displays import nokia_display as LynxDisplay

from engine.inputs import keyboard_input as LynxInput
from engine.inputs import gpio_input as LynxInput

from scenes import menu as LynxMenu

def main():
	#Use for Nokia display
	# display = LynxDisplay.Nokia()
	#framerate = 2

	# Use for displaying as imgage
	# display = LynxDisplay.Test()

	# Use for displaying in console
	display = LynxDisplay.Console()
	framerate = 1

	# Use for RPi GPIO input
	# input_method = LynxInput.RPi_GPIO()

	# Use for Keyboard input (Numpad arrows on num lock eg. 8 as UP, [enter] sending command)
	input_method = LynxInput.Keyboard()

	LynxCore.init_processor(display, input_method, framerate)

	opts = [LynxMenu.MenuOption("Option 1"),
	        LynxMenu.MenuOption("Option 2"),
	        LynxMenu.MenuOption("Option 3"),
	        LynxMenu.MenuOption("Option 4"),
	        LynxMenu.MenuOption("Option 5"),
	        LynxMenu.MenuOption("Oprion 6"),
	        LynxMenu.MenuOption("Exit")]

	LynxMenu.init_menu(opts)

if __name__ == '__main__':
	main()