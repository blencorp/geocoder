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
  g['name'] = data['resourceSets'][0]['resources'][0]['name']
  g['code'] = data['resourceSets'][0]['resources'][0]['geocodePoints'][0]['coordinates']

  return g

