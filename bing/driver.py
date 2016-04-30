#!/usr/bin/python

import sys
from Database import GetDBN
from Database import UpdateTable
from AddressParser import GetAddressByNumber
from Geocode import GetGeocode

def main(argv=None):
  """Main function to drive the process.
  """
  dbhost = '_server'
  dbuser = '_user'
  dbpass = '_pass'
  dbname = "_dbname"
  apikey = "AAAAAABBBBBBBBBBBCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDDEEEEEEEEEEEEFFF"

  # Get a list of DBNs from DB table.
  numbers = GetDBN(dbhost, dbuser, dbpass, dbname, 5)

  # For each DBN, get address, get geocode, and update table.
  for number in numbers:
    addrs = GetAddressByNumber(number)
    geocode = GetGeocode(apikey, addrs)
    addrs.append(geocode[0])
    addrs.append(geocode[1])
    UpdateTable(dbhost, dbuser, dbpass, dbname, addrs, number)

  return 0

if __name__ == "__main__":
  sys.exit(main())
