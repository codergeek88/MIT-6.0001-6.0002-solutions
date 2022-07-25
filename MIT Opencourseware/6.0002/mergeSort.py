#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 19:42:27 2020

@author: kishanpatel
"""
import time
def merge(list1, list2):
    new_list = []
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] < list2[0]:
            new_list.append(list1.pop(0))
        else:
            new_list.append(list2.pop(0))
    while len(list1) == 0 and len(list2) > 0:
        new_list.append(list2.pop(0))
    while len(list2) == 0 and len(list1) > 0:
        new_list.append(list1.pop(0))
    return new_list
    
def mergeSort(some_list):
    if len(some_list) == 0 or len(some_list) == 1:
        return some_list
    else:
        middle = len(some_list)//2
        left = mergeSort(some_list[:middle])
        right = mergeSort(some_list[middle:])
        return merge(left, right)

def isIn(e, unsorted_list):
    L = mergeSort(unsorted_list)
    def bisection_search_helper(e, L, low=0, high=len(L)-1):
        if high - low == 0:
            return False
        elif high - low == 1:
            return L[0] == e
        else:
            middle = (low + high)//2
            if L[middle] == e:
                return True
            elif L[middle] < e:
                return bisection_search_helper(e, L, middle, high)
            else:
                return bisection_search_helper(e, L, low, middle)
    return bisection_search_helper(e, L)

def merge_lecture(left, right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge_lecture(left, right)

test_list = [1,3,5,7,2,6,25,18,13]

def test_merge():
    start_mine = time.time()
    solution_mine = mergeSort(test_list)
    end_mine = time.time()
    time_mine = end_mine - start_mine
    
    start_lecture = time.time()
    solution_lecture = merge_sort(test_list)
    end_lecture = time.time()
    time_lecture = end_lecture - start_lecture
    
    print("my solution:", solution_mine)
    print("my time:", time_mine)
    print()
    print("lecture solution:", solution_lecture)
    print("lecture time:", time_lecture)