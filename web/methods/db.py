# !/usr/bin/env python
# coding: utf-8

__author__ = 'Moch'

import MySQLdb
# Open database connection
conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="chinou", db="MXDB", port=3306, charset="utf8")

# prepare a cursor object using cursor() method
cursor = conn.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print "Database version : %s " % data

# disconnect from server
conn.close()