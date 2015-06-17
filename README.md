# PyCasso
PyCasso, SVG painting generator.

© Clément Michard 2015 - All rights reserved

## Installation

PyCasso needs Python 2.x

The only thing to install is svgwrite.
With pip:

    pip install svgwrite
or from source:

    python setup.py install
    
## Execution:

    python pycasso.py

## Optional arguments:

    -s (--size)
Size of the painting (Examples: "21x29.7", "raisin", "A4", ...)

    -p (--palette)
Palette of colors (Examples: "bleu_beige", "data/palettes/bleu_beige.txt", "http://coolors.co/app/463730-1f5673-759fbc-90c3c8-b9b8d3", ...)

    -o (--ouput)
Output path (Example: "../tests/first_try.svg")
