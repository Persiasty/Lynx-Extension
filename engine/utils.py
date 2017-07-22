# -*- coding: utf-8 -*-
import threading

def set_interval(func, sec):
	def func_wrapper():
		func()
		set_interval(func, sec)
	t = threading.Timer(sec, func_wrapper)
	t.start()
	return t

def normalize_polish_leters(text):
	letters = [('ą', 'a'), ('ć', ''), ('ę', 'e'), ('ł', 'l'), ('ń', 'n'), ('ó', 'o'), ('ś', 's'), ('ź', 'z'), ('ż', 'z'),
	 ('Ą', 'A'), ('Ć', 'C'), ('Ę', 'E'), ('Ł', 'L'), ('Ń', 'N'), ('Ó', 'O'), ('Ś', 'S'), ('Ź', 'Z'), ('Ż', 'Z')]
	for old, new in letters:
		text = text.replace(old, new)
	return text