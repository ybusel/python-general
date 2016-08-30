#!/usr/bin/python
import requests
import datetime
import time
from bs4 import BeautifulSoup
import sys


url = raw_input( "Please enter hostname(http://hostname:8806): ")
user = raw_input( "Login username: ")
pwd = raw_input( "Login password: ")

r = requests.get(url, auth=(user,pwd), stream=True)
page = r.content
soup = BeautifulSoup(page)
status = soup.find("div",{"class": "last-sync ok"}).a.contents

for dt in status:
        date_format = "%b/%d/%y %I:%M:%S %p"
        synctime = ' '.join(dt.string.split())
        dt_synctime = datetime.datetime.strptime(synctime, date_format)
        print dt_synctime

now = datetime.datetime.now()

print now

delta = datetime.timedelta(minutes=45)

diff = now - dt_synctime

print diff

# CRITICAL = 2
# WARNING = 1
# OK = 0

if diff > delta:
        print "Sync is taking too long and now is more than %s minutes." % diff
        sys.exit(2)
else:
        print "Sync is OK"
        sys.exit(0)
"check_egnyte_sync.py" 44L, 892C                                               
