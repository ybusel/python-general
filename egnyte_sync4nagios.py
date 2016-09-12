#!/usr/bin/python
import requests
import datetime
import time
import urlparse
import re
from bs4 import BeautifulSoup
import sys, getopt


hostname = ''
usr = ''
pwd = ''

try:
        myopts, args = getopt.getopt(sys.argv[1:], "H:u:p:")
        if not myopts:
                print 'Please supply options.'
                print ("Usage: %s -H hostname -u usr -p pwd" % sys.argv[0])
                sys.exit()

except getopt.GetoptError as e:
        print (str(e))
        print ("Usage: %s -H hostname -u usr -p pwd" % sys.argv[0])
        sys.exit(2)

for o, a in myopts:
        if o == '-H':
                hostname = a
        elif o == '-u':
                usr = a
        elif o == '-p':
                pwd = a

url_d = list(urlparse.urlsplit('http://localhost:8806'))
url_d[1] = re.sub('^[^:]*', hostname, url_d[1])
url = urlparse.urlunsplit(url_d)
print url
r = requests.get(url, auth=(usr,pwd), stream=True)
page = r.content
soup = BeautifulSoup(page)
status = soup.find("div",{"class": "last-sync ok"}).a.contents

for dt in status:
        date_format = "%b/%d/%y %I:%M:%S %p"
        synctime = ' '.join(dt.string.split())
        dt_synctime = datetime.datetime.strptime(synctime, date_format)
#       print dt_synctime

now = datetime.datetime.now()

#print now

delta = datetime.timedelta(minutes=45)

diff = now - dt_synctime

#print diff

# CRITICAL = 2
# WARNING = 1
# OK = 0

if diff > delta:
        print "Sync is taking too long and now is more than %s minutes." % diff
        sys.exit(2)
else:
        print "Sync is OK"
        sys.exit(0)
