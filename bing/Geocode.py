#!/usr/bin/env python
"""Returns geocode response in parts.
"""
import sys
import os.path
import json

def GetGeocode(jsondata):
  """Returns the geocode from the response.
  :param jsondata: the json data.
  """

  # Load json.
  data = json.loads(jsondata)

  # Instantiate associative array.
  g = {}

  # Set name and geocode.
  try:
    g['name'] = data['resourceSets'][0]['resources'][0]['name']
    g['lat'] = data['resourceSets'][0]['resources'][0]['geocodePoints'][0]['coordinates'][0]
    g['long'] = data['resourceSets'][0]['resources'][0]['geocodePoints'][0]['coordinates'][1]
  except:
    pass

  return g

