#!/usr/bin/env python
"""Returns geocode response in parts.
"""
import sys
import os.path
import json

def GetData(filename):
  """Creates a file using the year and month as the name.
  :param filename: the name of the file that contains the HTML data.
  https://msdn.microsoft.com/en-us/library/ff701711.aspx
  """
  if (os.path.isfile(filename) == False):
    exit("{0} does not exist.".format(filename))

  f = open(filename)
  jsondata = f.read()
  f.close()

  data = json.loads(jsondata)
  print data['resourceSets'][0]['resources'][0]['name']
  print data['resourceSets'][0]['resources'][0]['geocodePoints'][0]['coordinates']

