#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The elements of this script are very similar to trml2pdf by Fabien Pinckaers

import os

from xml.dom import minidom

import reportlab

from reportlab.pdfgen import canvas
from reportlab import platypus

from reportlab.pdfbase import pdfmetrics

from reportlab.lib.fonts import addMapping
from reportlab.pdfbase.ttfonts import TTFont

OPENRML_FORMAT_AUTO = 0
OPENRML_FORMAT_PDF = 1
OPENRML_FORMAT_PS = 2
OPENRML_FORMAT_SVG = 3

OPENRML_FONT_PATHS = ['/usr/share/fonts/truetype/ttf-bitstream-vera/',
                      '/usr/share/fonts/truetype/freefont/',]

class RMLDocument():
  def __init__(self, infile, infiletype=OPENRML_FORMAT_AUTO):
    pass

  def render(self, outfile):
    pass

def main():
  from optparse import OptionParser
  usage = "usage: %prog [options] inputfile"
  parser = OptionParser(usage=usage)
  parser.add_option("-o", "--output-file", dest="output-filename",
    help="write output to FILE", metavar="FILE")
  parser.add_option("-q", "--quiet", action="store_false", dest="verbose",
    default=True, help="don't print status messages to stdout")

  (options, args) = parser.parse_args()

  doc1 = RMLDocument(open(args[0]))
  #doc.render(open(options['outfile'], 'w')) #what goes in, must come out.
  doc1.doweird('sexy','Vera.ttf')
  doc2 = RMLDocument(open(args[0]))
  #doc.render(open(options['outfile'], 'w')) #what goes in, must come out.
  doc2.doweird('pants','Vera.ttf')

  from reportlab.lib import fonts
  print fonts._tt2ps_map
  
if __name__ == '__main__':
  main()
