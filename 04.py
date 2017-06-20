#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 17:05:56 2017

@author: jeffzhang
"""

# 04

import requests
import re

add = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

num = 75635

address_list = []

for i in range(0,410):
    r = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(num))
    pattern = re.compile(r'\d*$')
    match = pattern.search(r.text)
    if match.group()!="":
        num = match.group()
        address = add+str(num)
        print "round{},done. The address is {}".format(i,address)
    else:
        print "answer:\nhttp://www.pythonchallenge.com/pc/def/{}".format(r.text)
        break
