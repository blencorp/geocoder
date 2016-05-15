#!/usr/bin/python

import sys
import os.path
import csv
import ConfigParser
from Geocode import GetGeocode

def main(argv):
  """Main function to drive the program.
  """
  if argv is None:
    argv = sys.argv

  if len(argv) != 2:
    print "usage: {0} <filename> <csv column numer>".format(__file__)
    exit(1)
  else:
    # Get args.
    filename = argv[0]
    col = int(argv[1])

    # Check if file exists.
    if (os.path.isfile(filename) == False):
      exit("{0} does not exist.".format(filename))

    # Read API Key.
    keyfile = 'settings.ini'
    config = ConfigParser.ConfigParser()
    config.read(keyfile)

    apikey = config.get('Bing','Key')

    # Read CSV
    with open(filename, 'rb') as csvfile:
      spamreader = csv.reader(csvfile, delimiter='|')
      for row in spamreader:
        # Get column based on arg
        place = row[col]

        # Get geocode for each "Place"
        geocode = GetGeocode(apikey, place)

  return 0

if __name__ == "__main__":
  main(sys.argv[1:])

