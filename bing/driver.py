#!/usr/bin/python

import sys
import os.path
import csv
import ConfigParser
from Response import GetResponse
from Geocode import GetGeocode

def main(argv):
  """Main function to drive the program.
  """
  if argv is None:
    argv = sys.argv

  if len(argv) != 1:
    print "usage: {0} <filename>".format(__file__)
    exit(1)
  else:
    # Get args.
    filename = argv[0]

    # Check if file exists.
    if (os.path.isfile(filename) == False):
      exit("{0} does not exist.".format(filename))

    # Read API Key.
    keyfile = 'settings.ini'
    config = ConfigParser.ConfigParser()
    config.read(keyfile)

    apikey = config.get('Bing','Key')

    # Read input file.
    with open(filename, 'rb') as f:
      places = f.read()

      # Expects one place per line.
      for place in places:
        response = GetResponse(apikey, place)
        g = GetGeocode(response)
        print g['name'], g['code']

  return 0

if __name__ == "__main__":
  main(sys.argv[1:])

