#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 18:55:11 2020

@author: Kishan
"""


cube=9
epsilon=0.001

for n in range(0,cube+1):
    if (n**3)>=cube:
        break
low=0
high=n
guess=(high+low)/2.0

if n**3!=cube:
    while abs(cube-(guess**3))>=epsilon:
        if guess**3<cube:
            low=guess
        else:
            high=guess
        guess=(high+low)/2.0
    print(guess)
else:print(n)