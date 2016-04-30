#!/usr/bin/python

import sys
import MySQLdb as mdb

def GetDBN(dbhost, dbuser, dbpass, dbname, limit):
  conn = None
  dbnlist = list()

  try:
    conn = mdb.connect(dbhost, dbuser, dbpass, dbname)
    cursor = conn.cursor()

    cursor.execute("""
      SELECT DBN
      FROM ds_NYC_SAT_2010
      LIMIT %s
      """, (limit)
    )

    rows = cursor.fetchall()

    for row in rows:
      dbnlist.append(row[0])

    cursor.close()
    conn.commit()

    return dbnlist

  except mdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

  finally:
    if conn:
      conn.close()

def UpdateTable(dbhost, dbuser, dbpass, dbname, arrAddr, DBN):

  conn = None

  try:
    conn = mdb.connect(dbhost, dbuser, dbpass, dbname)
    cursor = conn.cursor()

    cursor.execute("""
      UPDATE ds_NYC_SAT_2010
      SET
        Street=%s,
        City=%s,
        State=%s,
        Zipcode=%s,
        Lat=%s,
        Lon=%s
      WHERE DBN=%s
      """,
      (
        arrAddr[0],
        arrAddr[1],
        arrAddr[2],
        arrAddr[3],
        arrAddr[4],
        arrAddr[5],
        DBN
      )
    )
    cursor.close()
    conn.commit()
  except mdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

  finally:
    if conn:
      conn.close()

