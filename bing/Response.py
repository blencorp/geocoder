#!/usr/bin/python

import sys
import requests

def GetResponse(key, place):
  """Returns response from Bing.
  See https://msdn.microsoft.com/en-us/library/ff701711.aspx.
  https://realpython.com/blog/python/api-integration-in-python/
  https://msdn.microsoft.com/en-us/library/ff701711.aspx
  """

  base = 'http://dev.virtualearth.net/REST/v1/Locations'
  rmax = 1
  url = base + '?q=' + place + '&key=' + key

  response = requests.get(url)

  if response.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /Locations/ {}'.format(response.status_code))

  return response.text

