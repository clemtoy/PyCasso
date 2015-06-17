# -*-coding:utf-8 -*

import re
import random

from geometry import *

class REMatcher(object):

	def __init__(self, matchstring):
		self.matchstring = matchstring

	def match(self,regexp):
		self.rematch = re.match(regexp, self.matchstring)
		return bool(self.rematch)

	def group(self,i):
		return self.rematch.group(i)



class Guideline:

	def random_length(self):
		""" Returns a length respecting the rule of aesthetics of the guideline. """

		horizontal = random.choice([True, False])
		if random.random() < 0.05:
			return random.gauss(1, self.thirds.x if horizontal else self.thirds.y)
		elif random.random < 0.3:
			return self.thirds.x if horizontal else self.thirds.y 
		else:
			return random.uniform(0, self.thirds.x if horizontal else self.thirds.y)


	def __init__(self, dimension, primary_points, secondary_points, thirds):
		""" Initialises the guideline. """

		self.dimension = dimension
		self.primary_points = primary_points
		self.secondary_points = secondary_points
		self.thirds = thirds


class RuleOfThirds(Guideline):

	def __init__(self, dimension):
		""" Initialises a rule of thirds object. """

		x_third = dimension.width / 3
		y_third = dimension.height / 3
		primary_points = [Point(x_third,y_third), Point(2*x_third,y_third), Point(x_third,2*y_third), Point(2*x_third,2*y_third)]
		secondary_points = Point.points_between(primary_points)
		Guideline.__init__(self, dimension, primary_points, secondary_points, Point(x_third,y_third))

class GoldenRatio(Guideline):

	def __init__(self, dimension):
		""" Initialises a golden ratio rule object. """

		gold = (1 + math.sqrt(5)) / 2
		x = dimension.width / (gold + 1)
		y = dimension.height / (gold + 1)
		primary_points = [Point(x,y), Point(dimension.width-x,y), Point(x,dimension.height-y), Point(dimension.width-x,dimension.height-y)]
		secondary_points = Point.points_between(primary_points)
		Guideline.__init__(self, dimension, primary_points, secondary_points, [x,y])



class Dimension:

	def _load_dimensions(self):
		""" Load formats from file. """

		dimensions = {}
		with open('data/formats.txt', 'r') as f:
			for line in f:
				name, ben1, width, ben2, height, ben3, ben4 = re.split(r'\t|( x )|\n', line)
				dimensions[name] = (float(width), float(height))
		return dimensions


	def __str__(self):
		""" Returns the format, string-formatted. """

		return "{0} x {1} cm".format(self.width, self.height)


	def __init__(self, name, guideline):
		""" Initialises the format. """

		dimensions = self._load_dimensions()
		default_size = dimensions[random.choice(dimensions.keys())]

		if name:
			dimensions = self._load_dimensions()
			m = REMatcher(name)

			if m.match(r'^([\d\.]+)x([\d\.]+)$'):
				size = float(m.group(1)), float(m.group(2))

			elif name.lower() in dimensions.keys():
				size = dimensions[name.lower()]
			else:
				size = default_size
		else:
			size = default_size

		self.width, self.height = size

		if guideline == 'golden_ratio':
			self.guideline = GoldenRatio(self)
		else:
			self.guideline = RuleOfThirds(self)