__author__ = 'Moch'

#!/usr/bin/env python
# coding: utf-8

# import os
#
# for (k, v) in os.environ.items():
#     # print "%s=%s" % (k, v)
#     # print("%s = %s" % (k, v))
#     print ",".join(k)
#
# import sys
#
# print "\n".join(sys.modules.keys())

# import  os

# import urllib2

# request = urllib2.Request('https://github.com/atcuan/')
# opener = urllib2.build_opener()
# feeddata = opener.open(request).read()

# print feeddata


# list = os.sysconf('ls -la')
# print list


# request = urllib2.Request('http://diveintomark.org/xml/atom.xml')
# first_data_stream = urllib2.build_opener().open(request.get_full_url())
# print first_data_stream.headers.dict

import re

# def plural(noun):
#     if re.search('[sxz]$', noun):             1
#         return re.sub('$', 'es', noun)        2
#     elif re.search('[^aeioudgkprt]h$', noun):
#         return re.sub('$', 'es', noun)
#     elif re.search('[^aeiou]y$', noun):
#         return re.sub('y$', 'ies', noun)
#     else:
#         return noun + 's'



import re

rules = \
  (
    (
     lambda word: re.search('[sxz]$', word),
     lambda word: re.sub('$', 'es', word)
    ),
    (
     lambda word: re.search('[^aeioudgkprt]h$', word),
     lambda word: re.sub('$', 'es', word)
    ),
    (
     lambda word: re.search('[^aeiou]y$', word),
     lambda word: re.sub('y$', 'ies', word)
    ),
    (
     lambda word: re.search('$', word),
     lambda word: re.sub('$', 's', word)
    )
   )

def plural(noun):
    for matchesRule, applyRule in rules:
        if matchesRule(noun):
            return applyRule(noun)

''' 动态生成 '''
def buildMatchAndApplyFunctions((pattern, search, replace)):
    matchFunction = lambda word: re.search(pattern, word)
    applyFunction = lambda word: re.sub(search, replace, word)
    return (matchFunction, applyFunction)

patterns = \
  (
    ('[sxz]$', '$', 'es'),
    ('[^aeioudgkprt]h$', '$', 'es'),
    ('(qu|[^aeiou])y$', 'y$', 'ies'),
    ('$', '$', 's')
  )
rules = map(buildMatchAndApplyFunctions, patterns)

