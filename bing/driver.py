#!/usr/bin/python

import sys
import os.path
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
      # Expects one place per line.
      # Using splitlines to avoid newline.
      places = f.read().splitlines()

      for place in places:
        try:
          response = GetResponse(apikey, place)
          g = GetGeocode(response)
          print '{0}|{1}|{2}'.format(g['name'], g['lat'], g['long'])
        except Exception:
          pass

  return 0

if __name__ == "__main__":
  main(sys.argv[1:])

