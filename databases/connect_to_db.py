__author__ = 'mircea'

import MySQLdb

db = MySQLdb.connect(host="127.0.0.1", # your host, usually localhost
                     user="zeeguu", # your username
                      passwd="sla2012", # your password
                      db="zeeguu") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM User")

# print all the first cell of all the rows
for row in cur.fetchall() :
    print row[1]



