#!/usr/bin/python
import sys
import re

try:
    if sys.argv[1:]:
        print "File: %s" % (sys.argv[1])
        dnsfile = sys.argv[1]
    else:
        dnsfile = raw_input("Please enter dns file to parse: ")

        file = open(dnsfile,"r")

        for line in file.readlines():
                regex = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",line)
                if regex:
                        print(", ".join(regex))
#                       print line

except IOError, (errno, strerror):
        print "I/O Error(%s) : %s" % (errno, strerror)

