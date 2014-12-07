
# zipcode.py
# simple class for accessing zip code information
#
# data from: http://www.unitedstateszipcodes.org/zip-code-database/

import sys
import csv

class zipcode():

    dataPath = 'app/zipcodes.csv'

    timezones = [ ['America/Puerto_Rico'],                                     \
                  ['America/Detroit', 'America/Indiana/Indianapolis',          \
                   'America/Indiana/Marengo', 'America/Indiana/Vevay',         \
                   'America/Indiana/Vincennes', 'America/Kentucky/Louisville', \
                   'America/New_York'],                                        \
                  ['America/Chicago', 'America/Indiana/Knox',                  \
                   'America/Indiana/Petersburg', 'America/Indiana/Tell_City',  \
                   'America/Indiana/Winamac', 'America/Kentucky/Monticello',   \
                   'America/Menominee'],                                       \
                  [ 'America/Boise', 'America/Denver',                         \
                    'America/North_Dakota/Center', 'America/Phoenix',          \
                    'America/Shiprock' ],                                      \
                  [ 'America/Los_Angeles', 'America/Yakutat' ],                \
                  [ 'America/Anchorage', 'America/Juneau', 'America/Nome' ]    \
                ]
    
    # accessible class vars
    zip = []
    city = {}
    state = {}
    gmtoffset = {}

    # constructor
    def __init__(self, path=dataPath):

        ntz = len(self.timezones)
        zfile  = open(path, 'r')
        reader = csv.reader(zfile)

        rownum = 0
        for row in reader:
            if rownum > 0:

                # find GMT offset from timezone
                offset = 0
                tzname = row[7]
                for i in range(ntz):
                    if (tzname in self.timezones[i]):
                        offset = -i - 4
                
                # only keep clean data
                city = row[2]
                state = row[5]
                country = row[12]
                if ((country == 'US') and (offset != 0) and (len(city)>0) and (len(state)>0)):
                    zc = row[0]
                    self.zip.append(zc)
                    self.city[zc] = row[2]
                    self.state[zc] = row[5]
                    self.gmtoffset[zc] = offset

            rownum += 1
        zfile.close()
