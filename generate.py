#!/usr/bin/python

# generate.py <rows_in_thousands>
#
# Generate realistic random postal addresses.
#

import random
import zipcode

# config
FS = '\t'
RS = '\n'
quotedStrings = False

# load CSV file of token, frequency and return a list of tuples
def loadfreqs(fname):
    runtotal = 0.0
    freqlist = []
    fp = open(fname,'r')
    for line in fp:
        fields = line.split(',')
        if (len(fields) == 2):
            token = fields[0]
            freq = float(fields[1])/10000
            runtotal += freq
            tup = (token, runtotal)
            freqlist.append(tup)
    return(freqlist)

# choose a token from a list of (token, cumulativeFreq) tuples using
# the weighted roullette method
def wtdchoice(freqlist):
    maxval = freqlist[len(freqlist)-1][1]
    r = random.random() * maxval
    imin = 0
    imax = len(freqlist)-1
    imid = imax

    while (imid > imin):
        if (r < freqlist[imid][1]):
            imax = imid
        else:
            imin = imid
        imid = (imin + imax) / 2
    return(freqlist[imax])


def randToken(tokenList):
    return(tokenList[random.randint(0, len(tokenList)-1)])

def randDigits(numDigits):
    token = ''
    for i in range(numDigits):
        token += chr(random.randint(48,57))
    return(token)

def randAlphaNumeric(len):
    token = ''
    for i in range(len):
        r = random.randint(97,132)
        if (r > 122):
            r -= 75
        token += chr(r)
    return(token)

def quoted(s):
    if (quotedStrings):
        return('"' + s + '"')
    else:
        return(s)


fnames = loadfreqs('names-female.csv')
mnames = loadfreqs('names-male.csv')
lnames = loadfreqs('names-last.csv')
gender = None
for i in range(30):
    if (random.random() > 0.5):
        gender = 'male'
        first = wtdchoice(mnames)[0]
    else:
        gender = 'female'
        first = wtdchoice(fnames)[0]

    last = wtdchoice(lnames)[0]

    print first + ' ' + last


