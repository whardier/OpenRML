# The elements of this script are very similar to trml2pdf by Fabien Pinckaers

import reportlab.lib.units

def get_unit_value(text):
  if text.endswith('in'):
    return float(text.replace('in','')) * reportlab.lib.units.inch
  if text.endswith('cm'):
    return float(text.replace('cm','')) * reportlab.lib.units.cm
  if text.endswith('mm'):
    return float(text.replace('mm','')) * reportlab.lib.units.mm
  if text.endswith('pt'):
    return float(text.replace('pt','')) * reportlab.lib.units.pica
  return float(text)
      
def convert_page_size_to_tuple(text):
  return tuple([get_unit_value(x.strip()) for x in text.replace('(','').replace(')','').split(',')])

def prepare_template_attrs(element):
  if not hasattr(element, '_attrs'):
    return {}

  attrs = {}

  for attr in element._attrs.keys():
    value = element._attrs[attr].value
    attr = attr.lower()
    if attr == 'pagesize':
      attrs['pageSize'] = convert_page_size_to_tuple(value)
    if attr == 'showboundary':
      attrs['showBoundary'] = int(value)
    if attr == 'leftmargin':
      attrs['leftMargin'] = int(value)
    if attr == 'rightmargin':
      attrs['rightMargin'] = int(value)
    if attr == 'topmargin':
      attrs['topMargin'] = int(value)
    if attr == 'bottommargin':
      attrs['bottomMargin'] = int(value)
    if attr == 'id':
      attrs['id'] = unicode(value)

  return attrs

