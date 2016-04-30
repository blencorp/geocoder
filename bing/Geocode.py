#!/usr/bin/python

import sys
import urllib2
from suds.client import Client
from suds.client import WebFault

def GetGeocode(key, arrAddr):
  _geocode = list()
  application_key = key

  domain = 'http://dev.virtualearth.net'
  virdir = '/webservices/v1/geocodeservice/'
  wsdl = 'geocodeservice.svc?wsdl'
  url = domain + virdir + wsdl

  c = Client(url)

  greq = c.factory.create('GeocodeRequest')

  #Credentials
  cred = c.factory.create('ns0:Credentials')
  cred.ApplicationId = application_key
  greq.Credentials = cred

  #Address
  address = c.factory.create('ns0:Address')

  # street
  address.AddressLine = arrAddr[0]

  # city
  address.Locality = arrAddr[1]

  # state
  address.AdminDistrict = arrAddr[2]

  # country
  address.CountryRegion = "USA"

  greq.Address = address

  #Select 1st port and set request options:
  c.set_options(port='BasicHttpBinding_IGeocodeService')

  try:
    response = c.service.Geocode(greq)
  except WebFault, e:
    print "ERROR!"
    print e

  locations = response['Results']['GeocodeResult'][0]['Locations']['GeocodeLocation']

  for loc in locations:
    _geocode.append(loc['Latitude'])
    _geocode.append(loc['Longitude'])

  return _geocode
