# -*-coding:utf-8 -*

import subprocess
import sys
import getopt
import time

import svgwrite
from svgwrite import cm

from dimension import *
from palette import *




class Painting:

	def sign(self, svg):
		""" Prints the signature on the SVG. """ 

		signature = svg.g(transform="translate({0},{1}) scale(0.00035,-0.00035)".format(self.dimension.width-3, self.dimension.height-0.5), fill=self.palette.rand_color(), stroke="none")
		signature.add(svg.path(d="M7037 3855 c-334 -200 -500 -335 -592 -480 -48 -75 -112 -220 -155 -350 l-33 -100 -272 -270 c-149 -148 -286 -292 -303 -319 -39 -61 -41 -99 -7 -122 34 -22 85 -9 295 73 230 91 240 96 240 135 0 17 27 130 60 252 170 621 249 751 590 976 58 38 168 107 245 153 130 77 140 85 140 112 0 55 -35 44 -208 -60z m-870 -1260 l-43 -158 -104 -44 c-58 -24 -143 -57 -189 -74 -83 -29 -84 -29 -66 -7 30 36 439 448 442 445 1 -2 -17 -74 -40 -162z"))
		signature.add(svg.path(d="M5626 2763 c-49 -27 -110 -67 -135 -90 l-47 -41 1 51 c0 49 -1 52 -27 55 -36 4 -41 -8 -73 -176 -33 -173 -47 -307 -43 -412 3 -82 4 -85 27 -88 40 -6 51 21 51 122 0 112 16 225 34 245 7 9 28 45 46 79 42 79 91 123 211 187 87 46 94 53 94 80 0 46 -35 43 -139 -12z"))
		signature.add(svg.path(d="M4930 2576 c-41 -18 -122 -60 -180 -93 -95 -55 -105 -63 -105 -89 0 -49 32 -42 182 39 212 115 243 121 243 47 0 -40 -7 -49 -171 -223 -199 -211 -248 -272 -256 -320 -4 -30 -2 -38 21 -52 36 -24 86 -16 259 42 144 48 179 68 171 100 -3 10 9 98 26 196 16 98 30 205 30 238 0 148 -67 183 -220 115z m99 -407 c-11 -68 -23 -126 -25 -128 -7 -8 -230 -81 -247 -81 -16 0 -15 4 8 33 45 53 280 304 283 302 2 -2 -7 -59 -19 -126z"))
		signature.add(svg.path(d="M4101 2562 c-6 -11 -53 -147 -105 -303 -74 -219 -104 -325 -131 -464 -42 -210 -42 -239 -3 -243 36 -4 39 5 73 183 14 77 35 174 46 216 l21 77 126 60 c70 33 149 66 176 73 77 19 79 11 39 -227 -14 -89 -23 -169 -20 -178 10 -25 56 -20 67 7 13 30 48 236 55 322 7 81 -11 129 -57 154 -37 21 -112 4 -241 -54 -56 -24 -102 -43 -104 -41 -2 2 28 93 66 203 72 210 75 233 26 233 -13 0 -29 -8 -34 -18z"))
		signature.add(svg.path(d="M6270 2259 c-1707 -668 -3548 -1331 -4425 -1594 -779 -234 -1227 -307 -1327 -217 -43 38 -5 147 106 306 36 50 125 172 200 271 287 381 362 567 287 713 -25 49 -100 109 -146 118 -42 7 -55 0 -55 -31 0 -18 10 -30 37 -45 106 -56 132 -121 97 -241 -35 -116 -111 -239 -344 -548 -226 -301 -280 -397 -280 -499 0 -104 69 -152 230 -160 456 -21 1774 388 4250 1318 1013 381 1723 657 1737 676 18 25 -1 54 -35 53 -15 -1 -164 -55 -332 -120z"))
		signature.add(svg.path(d="M3686 2228 c-96 -149 -289 -477 -333 -565 -89 -178 -78 -243 44 -243 55 0 183 25 216 42 22 11 22 57 0 65 -9 4 -53 -1 -97 -10 -45 -10 -96 -17 -114 -17 -30 0 -33 2 -27 23 15 47 127 251 251 452 138 226 154 267 102 273 -19 2 -31 -3 -42 -20z"))
		signature.add(svg.path(d="M2812 2205 c-84 -37 -209 -180 -381 -435 -65 -96 -135 -203 -156 -238 -21 -34 -39 -61 -41 -59 -2 2 10 48 27 102 71 238 90 445 49 531 -42 86 -121 101 -231 43 -84 -44 -261 -220 -356 -354 -191 -268 -341 -584 -417 -873 -34 -129 -32 -157 9 -157 33 0 28 -11 79 173 141 508 532 1092 779 1163 24 7 33 4 53 -16 25 -26 28 -45 25 -155 -5 -142 -90 -435 -218 -755 -35 -88 -62 -169 -61 -180 2 -15 11 -20 33 -20 27 0 34 9 93 110 342 586 622 983 734 1041 25 13 28 12 38 -5 30 -58 2 -305 -73 -621 -23 -96 -41 -193 -42 -215 0 -36 3 -40 27 -43 35 -4 38 3 81 183 91 382 119 625 83 720 -12 30 -28 51 -46 60 -35 18 -46 18 -88 0z"))
		signature.add(svg.path(d="M3191 2028 c-19 -43 -152 -661 -149 -687 4 -36 53 -43 68 -9 18 42 151 660 148 687 -4 36 -53 43 -67 9z"))
		signature.add(svg.circle(cx="3260", cy="2200", r="45"))
		svg.add(signature)


	def toSVG(self):
		""" Writes the SVG."""

		w,h = self.dimension.width, self.dimension.height
		svg = svgwrite.Drawing(self.filename, size=("{0}cm".format(w), "{0}cm".format(h)),  viewBox=('0 0 {0} {1}'.format(w,h)))
		for figure in self.figures:
			figure.draw(svg)
		self.sign(svg)
		return svg


	def __init__(self, filename, size, guideline, palette, nb_figures):
		""" Initializes the painting. """

		self.filename = filename
		self.dimension = Dimension(size, guideline)
		self.palette = Palette(palette)
		self.figures = []
		background = Polygon([Point(0,0), Point(0,self.dimension.height), Point(self.dimension.width,self.dimension.height), Point(self.dimension.width,0)], self.palette.rand_color())
		background.primary_points = self.dimension.guideline.primary_points
		background.secondary_points = self.dimension.guideline.secondary_points
		self.figures.append(background)
		for i in range(nb_figures):
			fig = Figure.rand(self)
			self.figures.append(fig)



def usage():
	""" Prints the usage of the command. """
	print "PyCasso, painting generator."
	print "© Clément Michard 2015 - All rights reserved"
	print "\nOptional arguments:"
	print '\n-s (--size):\n\tSize of the painting (Examples: "21x29.7", "raisin", "A4", ...)'
	print '\n-p (--palette):\n\tPalette of colors (Examples: "bleu_beige", "data/palettes/bleu_beige.txt", "http://coolors.co/app/463730-1f5673-759fbc-90c3c8-b9b8d3", ...)'
	print '\n-o (--ouput):\n\tOutput path (Example: "../tests/first_try.svg")'




if __name__ == "__main__":
	size = None
	guideline = None
	palette = None
	n = 50
	output = 'painting_{0}.svg'.format(time.strftime("%Y%m%d-%H%M%S"))
	display = False

	try:
		options, args = getopt.getopt(sys.argv[1:], "s:g:p:n:o:d", ["size=", "guideline=", "palette=", "nb_figures=", "output=", "display"])
	except getopt.GetoptError as err:
		print str(err)
		sys.exit(2)
	if not options:
		usage()
	for option, value in options:
		if option in ('-s', '--size'):
			size = value
		elif option in ('-g', '--guideline'):
			guideline = value
		elif option in ('-p', '--palette'):
			palette = value
		elif option in ('-n', '--nb_figures'):
			n = int(value)
		elif option in ('-o', '--output'):
			output = value
		elif option in ('-d', '--display'):
			display = True

	painting = Painting(output, size, guideline, palette, n)
	svg = painting.toSVG()
	svg.save()
	if display:
		subprocess.call(["xdg-open", output])

