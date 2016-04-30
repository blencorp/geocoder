#!/usr/bin/python

import sys
import urllib2
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):

  def __init__(self):
    HTMLParser.__init__(self)
    self._tag = ""
    self._name = ""
    self._value = ""

    self.street = ""
    self.city = ""
    self.state = ""
    self.zipcode = ""

  def handle_starttag(self, tag, attrs):
    self._tag = tag

    for name, value in attrs:
      self._value = value

  def handle_data(self, data):
    if self._tag == 'span':
      if 'lblSchoolStreet' in self._value:
        if self.street == "":
          self.street = data
      elif 'lblSchoolCity' in self._value:
        if self.city == "":
          self.city = data
      elif 'lblSchoolState' in self._value:
        if self.state == "":
          self.state = data
      elif 'lblSchoolZip' in self._value:
        if self.zipcode == "":
          self.zipcode = data

def GetAddressByNumber(DBN):
  # declare list to hold the address
  addrList = list()

  # extract the first two characters
  sid = DBN[:2]

  # extract the rest of the string
  snum = DBN[len(sid):]

  domain = "http://schools.nyc.gov/"
  url = domain + "SchoolPortals/{0}/{1}/default.htm".format(sid, snum)

  content = urllib2.urlopen(url).read()

  parser = MyHTMLParser()
  parser.feed(content)

  addrList.append(parser.street)
  addrList.append(parser.city)
  addrList.append(parser.state)
  addrList.append(parser.zipcode)

  parser.close()

  return addrList
