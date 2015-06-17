# -*-coding:utf-8 -*

import random
import math

import svgwrite
from svgwrite import cm

class Point:

	@staticmethod
	def _points_between(a, b, n):
		middle = Point((a.x + b.x) / 2, (a.y + b.y) / 2)
		out = [middle]
		if n is not 0:
			out += Point._points_between(a, middle, n-1)
			out += Point._points_between(b, middle, n-1)
		return out

	@staticmethod
	def points_between(points):
		""" Returns points on the edges of the polygon described by the given list of points. """

		out = []
		for i in range(len(points) - 1):
			out += Point._points_between(points[i], points[i+1], 5)
		return out


	@staticmethod
	def pseudo_random(painting=None):
		""" Returns a random point (random is guided by the current painting content). """

		if painting and random.random() < 0.8:
			if random.random() < 0.8:
				return random.choice(painting.figures[-1].primary_points).clone()
			else:
				return random.choice(painting.figures[-1].secondary_points).clone()
		else:
			x = random.uniform(0, painting.dimension.width)
			y = random.uniform(0, painting.dimension.height)
			return Point(x,y)


	def clone(self):
		""" Returns a clone of the point. """

		return Point(self.x, self.y)


	def distance(self, point):
		""" Returns the distance from self to the point. """

		return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)


	def isInPainting(self, painting):
		""" Returns True if the point position is inside the painting. """

		return self.x >= 0 and self.y >= 0 and self.x <= painting.dimension.width and self.y <= painting.dimension.height

	def __init__(self, x, y):
		""" Initialises a point. """

		self.x = x
		self.y = y


class Figure:

	@staticmethod
	def rand(painting):
		""" Returns a pseudo-random figure. """

		return painting.figures[-1].similar(painting) if random.random() < 0.8 else random.choice([Circle, Polygon]).rand(painting)

	def __init__(self, primary_points, secondary_points, color):
		""" Initialises a figure. """

		self.primary_points = primary_points
		self.secondary_points = secondary_points
		self.color = color


class Polygon(Figure):

	@staticmethod
	def rand(painting):
		""" Returns a random polygon. """

		nb_points = random.choice([3,3,4,4,4,4,5,6])
		points = []
		for i in range(nb_points):
			points.append(Point.pseudo_random(painting))
		return Polygon(points, painting.palette.rand_color())


	def clone(self):
		""" Returns a clone of the polygon. """

		return Polygon([p.clone() for p in self.points], self.color.clone())


	def draw(self, svg):
		""" Adds the polygon to the SVG. """

		svg.add(svg.polygon(points=[(p.x, p.y) for p in self.points], fill=str(self.color)))


	def similar(self, painting):
		""" Creates a similar polygon as self with some changes (color, angles, position,...) """

		figure = self.clone()
		coord = random.choice(['x','y','xy'])
		delta = painting.dimension.guideline.random_length()
		direction = random.choice([1,-1])
		for point in figure.points:
			if coord in ('x', 'xy'):		
				point.x += direction * delta
			if coord in ('y', 'xy'):
				point.y += direction * delta
		if random.random() < 0.5:
			figure.color = painting.palette.rand_color()
		return figure


	def __init__(self, points, color):
		""" Initialises a polygon. """

		self.points = points
		Figure.__init__(self, self.points, Point.points_between(self.points), color)




class Circle(Figure):

	@staticmethod
	def rand(painting):
		""" Returns a pseudo-random circle. """

		center = Point.pseudo_random(painting)
		if random.random() < 0.8:
			radius = center.distance(Point.pseudo_random(painting))
		else:
			radius = painting.dimension.guideline.random_length() / 20
		return Circle(center, radius, painting.palette.rand_color())


	def clone(self):
		""" Returns a clone of the circle. """

		return Circle(self.center.clone(), self.radius, self.color.clone())


	def draw(self, svg):
		""" Adds the circle to the SVG. """

		svg.add(svg.circle(center=(self.center.x, self.center.y), r=self.radius, fill=str(self.color)))


	def similar(self, painting):
		""" Returns a similar circle with some changes (color, radius, position,...) """

		figure = self.clone()
		change_other_property = True
		while change_other_property:
			r = random.choice(['color', 'color', 'color', 'radius', 'radius', 'coord', 'coord', 'coord', 'coord', 'coord'])
			if r is 'color':
				figure.color = painting.palette.rand_color()
			elif r is 'radius':
				figure.radius = painting.dimension.guideline.random_length()
			elif r is 'coord':
				coord = random.choice(['x','y','xy'])
				delta = figure.radius if random.random() < 0.6 else painting.dimension.guideline.random_length()
				direction = random.choice([1,-1])
				if coord is 'x':
					figure.center.x += direction * delta
					if not figure.center.isInPainting(painting):
						figure.center.x *= -1
				if coord is 'y':
					figure.center.y += direction * delta
					if not figure.center.isInPainting(painting):
						figure.center.y *= -1
				else:
					figure.center.x += direction * delta
					figure.center.y += direction * delta
					#TODO if not figure.center.isInPainting(painting):
			change_other_property = random.random() < 0.2
		return figure

	def __init__(self, center, radius, color):
		""" Initialises a circle. """

		self.center = center
		self.radius = radius

		a,b,c,d = [self.center.clone() for i in range(4)]
		a.x += self.radius
		b.x -= self.radius
		c.y += self.radius
		d.y -= self.radius
		Figure.__init__(self, [self.center], [a,b,c,d], color)
