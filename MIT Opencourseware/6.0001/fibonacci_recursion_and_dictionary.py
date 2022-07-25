#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 18:00:15 2020

@author: kishanpatel
"""


def fib(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib(n - 1, d) + fib(n - 2, d)
        d[n] = ans
        return ans

d = {0:0, 1:1}

print(fib(34, d))