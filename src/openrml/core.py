#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The elements of this script are very similar to trml2pdf by Fabien Pinckaers

import os
import sys

from openrml.lib import *

from xml.dom import minidom

from ast import literal_eval

#Core
import reportlab
from reportlab import rl_config
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet

#Units
import reportlab.lib.units

#Fonts
from reportlab.lib.fonts import addMapping
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFont

OPENRML_FORMAT_AUTO = 0
OPENRML_FORMAT_PDF = 1
OPENRML_FORMAT_PS = 2
OPENRML_FORMAT_SVG = 3

OPENRML_TTF_PATHS = ['/usr/share/fonts/truetype/ttf-bitstream-vera/',
                     '/usr/share/fonts/truetype/freefont/',
                    ]

OPENRML_T1_PATHS = []

#The following limit attribute matching
OPENRML_TTF_ATTRS = [u'faceName', u'fileName']

class RMLDocument():
  def __init__(self, in_file, in_file_type=OPENRML_FORMAT_AUTO):
    self.doc = minidom.parse(in_file).getElementsByTagName('document')[0]

    #Used in the document information only
    self.file_name = self.doc.getAttribute('filename')

    self.first_page_template_node = None
    self.later_pages_template_node = None

    self.doc_template_node = None
    self.styles = getSampleStyleSheet()

  def config(self, ttf_paths=[], t1_paths=[]):
    ### TODO: Add to optparse
    for path in set(OPENRML_TTF_PATHS).union(ttf_paths):
      rl_config.TTFSearchPath.append(path)
    for path in set(OPENRML_T1_PATHS).union(t1_paths):
      rl_config.T1SearchPath.append(path)

  def registerfont(self, **attrs):
    ### TODO: Add T1
    if set(attrs.keys()).issubset(OPENRML_TTF_ATTRS):
      registerFont(TTFont(attrs['faceName'].value, attrs['fileName'].value))

  def init_doc(self):
    #TODO: All docinit capable types
    self.config()

    for docinit in self.doc.getElementsByTagName('docinit'):
      for element in docinit.childNodes:
        if element.nodeName == 'registerTTFont':
          self.registerfont(**element._attrs)

  def init_template(self):
    for template in self.doc.getElementsByTagName('template'):
      self.doc_template_node = template #This is lame, but I like it
      for element in template.childNodes:
        if element.nodeName == 'pageTemplate':
          if 'id' in element._attrs:
            id = element._attrs['id'].value
            if id == u'main':
              self.later_pages_template_node = element
            elif id == u'firstpage':
              self.first_page_template_node = element

  def init_stylesheet(self):
    for stylesheet in self.doc.getElementsByTagName('stylesheet'):
      for element in stylesheet.childNodes:
        if element.nodeName == 'initialize':
          pass
        elif element.nodeName == 'paraStyle':
          print element.toxml()

  def doc_on_first_page(self, canvas, doc):
    pass

  def doc_on_later_pages(self, canvas, doc):
    pass

  def get_template(self, out_file):
    attrs = prepare_template_attrs(self.doc_template_node)
    print attrs
    return SimpleDocTemplate(out_file, onFirstPage=self.doc_on_first_page,
                             onLaterPages=self.doc_on_later_pages, **attrs)

  def render(self, out_file):
    self.init_doc()
    self.init_template()
    template = self.get_template(out_file)
    self.init_stylesheet()

def main():
  from optparse import OptionParser
  usage = "usage: %prog [options] inputfile"
  parser = OptionParser(usage=usage)
  parser.add_option("-o", "--output-file", dest="out_file",
    help="write output to FILE", metavar="FILE")
  parser.add_option("-q", "--quiet", action="store_false", dest="verbose",
    default=True, help="don't print status messages to stdout")

  (options, args) = parser.parse_args()

  doc = RMLDocument(open(args[0]))
  doc.render(open(options.out_file, 'w')) #what goes in, must come out.

if __name__ == '__main__':
  main()
