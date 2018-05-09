#_*_coding:utf-8_*_
import csv
import math
from node import Node

def parse(filename):
  '''
  takes a filename and returns attribute information and all the data in array of dictionaries
  '''
  # initialize variables

  out = []  
  csvfile = open(filename,'rb')
  fileToRead = csv.reader(csvfile)

  headers = fileToRead.next()

  # iterate through rows of actual data
  for row in fileToRead:
    if '?' in row:
      row=['n' if x=='?' else x for x in row]

      out.append(dict(zip(headers, row)))
    else:
      out.append(dict(zip(headers, row)))
  return out
