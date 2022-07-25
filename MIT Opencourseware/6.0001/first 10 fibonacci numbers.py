#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 18:44:12 2020

@author: Kishan
"""


a=0
b=1
n=2
print(0)
print(1)
while n<10:
    a=a+b
    n+=1
    if n>10:
        break
    print(a)
    b=a+b
    n+=1
    print(b)