#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 09:13:45 2017

@author: jeffzhang
"""

# 02



string = "pc/def/map"

dic = {"k":"m","o":"q","e":"g"}

def decode(element):
    char = ''
    if element in [' ','.',"'","(",")",'/']:
        char = element
    else:
        number = ord(element)
        if number > ord('x'):
            char = chr(number - 24)
        else:
            char = chr(number +2)
    
    return char

def transform(string):
    string_transform = ""
    for element in string:
        string_transform += decode(element)
    return string_transform

print transform(transform(string))





           
