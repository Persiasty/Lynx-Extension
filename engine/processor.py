# -*- coding: utf-8 -*-
import hashlib
from engine import utils

__currentSceneUpdateMethod = None

__OldDataHash = None
__Display = None
def tick():
	global __OldDataHash, __currentSceneUpdateMethod
	if(__currentSceneUpdateMethod is None or not callable(__currentSceneUpdateMethod)):
		return

	image = __currentSceneUpdateMethod()
	pixelsHash = hashlib.sha1(image.load()).hexdigest()
	if(pixelsHash != __OldDataHash):
		__Display.display_frame(image)

def init_processor(display, framerate=2):
	utils.set_interval(tick, 1 / framerate)

def set_scene(scene):
	global __currentSceneUpdateMethod, __Display
	scene.set_display(__Display)
	__currentSceneUpdateMethod = scene.update
