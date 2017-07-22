# -*- coding: utf-8 -*-
import hashlib
from engine import display as LynxDisplay, input as LynxInput, utils as LynxUtils

__currentSceneUpdateMethod = None

__OldDataHash = None
__Display = None
__Input = None
def __tick():
	global __OldDataHash, __currentSceneUpdateMethod
	if(__currentSceneUpdateMethod is None or not callable(__currentSceneUpdateMethod)):
		return

	image = __currentSceneUpdateMethod()
	pixelsHash = hashlib.sha1(image.tobitmap()).hexdigest()
	if(pixelsHash != __OldDataHash):
		__Display.display_frame(image)

def init_processor(display, input_method, framerate=2):
	global __Display, __Input
	if(not isinstance(display, LynxDisplay.Display)):
		raise Exception("Error while display cast")
	__Display = display

	if (not isinstance(input_method, LynxInput.Input)):
		raise Exception("Error while display cast")
	__Input = input_method

	LynxUtils.set_interval(__tick, 1 / framerate)

def set_scene(scene):
	global __currentSceneUpdateMethod, __Display, __Input
	scene.set_display(__Display)
	__Input.set_input_handler(scene.action)
	__currentSceneUpdateMethod = scene.update
