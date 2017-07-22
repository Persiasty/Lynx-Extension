# -*- coding: utf-8 -*-
from engine import display as LynxDisplay, scenes as LynxScenes
from scenes import menu as LynxMenu
import time


def main():
	display = LynxDisplay.init_test()

	opts = [LynxMenu.MenuOption("Starts"),
	        LynxMenu.MenuOption("Times"),
	        LynxMenu.MenuOption("Settingss"),
	        LynxMenu.MenuOption("Connects"),
	        LynxMenu.MenuOption("Views"),
	        LynxMenu.MenuOption("Exits"),
	        LynxMenu.MenuOption("xD")]
	frame = LynxMenu.Menu(opts)
	frame.set_display(display)

	for i in range(5):
		display.display_frame(frame.display_text())
		frame._up()
	for i in range(6):
		display.display_frame(frame.display_text())
		frame._down()

	# lines = [x for x in open("plik.txt", 'r')]
	# for i in range(500):
	# 	LynxScenes.display_text(display, lines, title="Hej",offset=(0, -i))
	#LynxScenes.display_splash(display)


if __name__ == '__main__':
	main()