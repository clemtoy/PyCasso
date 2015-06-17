# -*-coding:utf-8 -*

import os
import random
import dircache
import re

class Color:
	def __str__(self):
		""" Returns a string-formatted color. """
		return 'rgb({0},{1},{2})'.format(self.r, self.g, self.b)


	def clone(self):
		""" Returns a clone of the color. """

		return Color(self.r, self.g, self.b)

	@staticmethod
	def normalize_hex(hex_value):
		""" From webcolors package. """

		try:
			HEX_COLOR_RE = re.compile(r'^#([a-fA-F0-9]{3}|[a-fA-F0-9]{6})$')
			hex_digits = HEX_COLOR_RE.match(hex_value).groups()[0]
		except AttributeError:
			raise ValueError("'%s' is not a valid hexadecimal color value." % hex_value)
		if len(hex_digits) == 3:
			hex_digits = ''.join(map(lambda s: 2 * s, hex_digits))
		return '#%s' % hex_digits.lower()

	@staticmethod
	def hex_to_rgb(hex_value):
		""" From webcolors package. """

		hex_digits = Color.normalize_hex(hex_value)
		return tuple(map(lambda s: int(s, 16), (hex_digits[1:3], hex_digits[3:5], hex_digits[5:7])))


	def __init__(self, r, g, b):
		""" Initialises a color. """
		self.r = r
		self.g = g
		self.b = b


class Palette:

	def rand_color(self):
		""" Returns a random color from the palette. """

		return random.choice(self.colors)


	def __init__(self, name):
		""" Initialises a palette. """

		self.colors = []
		directory = 'data/palettes/'
		if not name or 'http://' not in name:
			if not name:
				name = '_'
			if not '.txt' in name:
				filename = directory + name + '.txt'
			if not os.path.exists(filename):
				filename = random.choice(dircache.listdir(directory))
				filename = os.path.join(directory, filename)
			with open(filename, 'r') as f:
				for line in f:
					line = line.rstrip()
					r,g,b = line.split('\t')
					self.colors.append(Color(r,g,b))
		else:
			for hexcolor in name.split('/')[-1].split('-'):
				r, g, b = Color.hex_to_rgb('#' + hexcolor)
				self.colors.append(Color(r,g,b))

		
		
