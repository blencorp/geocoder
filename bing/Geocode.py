#!/usr/bin/python

import sys
import requests

def GetGeocode(key, place):
  """See https://msdn.microsoft.com/en-us/library/ff701711.aspx.
  https://realpython.com/blog/python/api-integration-in-python/
  https://msdn.microsoft.com/en-us/library/ff701711.aspx
  """

  base = 'http://dev.virtualearth.net/REST/v1/Locations'
  rmax = 10
  url = base + '?q=' + place + '&key=' + key

  resp = requests.get(url)

  if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /Locations/ {}'.format(resp.status_code))
  for todo_item in resp.json():
    #print('{} {}'.format(todo_item['id'], todo_item['summary']))
    print('{}'.format(todo_item))

  #http://dev.virtualearth.net/REST/v1/Locations?q=Greenville&maxResults=10&key=BingMapsKey
  #http://dev.virtualearth.net/REST/v1/Locations?q=Greenville&maxResults=10&key=BingMapsKey
  _geocode = 'coming soon'

# request = urllib2.Request(url)
# request.add_header('Authorization', credentialBing)
# requestOpener = urllib2.build_opener()
# response = requestOpener.open(request)
#
# results = json.load(response)
#
# # process results
#  print results

#  try:
#    response = c.service.Geocode(greq)
#  except WebFault, e:
#    print "ERROR!"
#    print e
#
#  locations = response['Results']['GeocodeResult'][0]['Locations']['GeocodeLocation']
#
#  for loc in locations:
#    _geocode.append(loc['Latitude'])
#    _geocode.append(loc['Longitude'])

  return _geocode

def GetResponse():
  # http://stackoverflow.com/questions/27606478/search-bing-via-azure-api-using-python
  keyBing = ''        # get Bing key from: https://datamarket.azure.com/account/keys
  credentialBing = 'Basic ' + (':%s' % keyBing).encode('base64')[:-1] # the "-1" is to remove the trailing "\n" which encode adds
  searchString = '%27Xbox+One%27'
  top = 20
  offset = 0

  url = 'https://api.datamarket.azure.com/Bing/Search/Image?' + \
        'Query=%s&$top=%d&$skip=%d&$format=json' % (searchString, top, offset)

  request = urllib2.Request(url)
  request.add_header('Authorization', credentialBing)
  requestOpener = urllib2.build_opener()
  response = requestOpener.open(request)

  results = json.load(response)

  # process results
  print results

