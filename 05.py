#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 11:01:39 2017

@author: newchama
"""

import urllib
import pickle

url = 'http://www.pythonchallenge.com/pc/def/banner.p'

lines = urllib.urlopen(url).readlines()
data = pickle.loads( ''.join(lines) )

for row in data:
    result = ''
    for chars in row:
        result += chars[0] * chars[1]
    print result