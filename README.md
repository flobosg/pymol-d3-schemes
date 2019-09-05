# pymol-d3-schemes

This script adds to PyMOL the color schemes present at [d3-scale-chromatic](https://observablehq.com/@d3/color-schemes?collection=@d3/d3-scale-chromatic).
Visit [this repository](https://github.com/d3/d3-scale-chromatic) for more info.
Sequential, diverging and cyclical schemes are discretized to 11 elements.

The color naming uses the following convention: d3*SchemeName*-*i*, where *i* is an integer between 1 and the number of colors in the scheme.
For instance, `d3Blues-1` refers to the first color of the Blues scheme.