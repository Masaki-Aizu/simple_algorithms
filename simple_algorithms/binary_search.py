#!/usr/bin/env python
# coding: utf-8
import random as rd

ls_len = 100
ls_range = 200

def binary_search(ls, item):
    i = 0
    low = 0
    high = len(ls) - 1
    
    while low <= high:
        mid = int((low + high ) / 2)
        mid_item = ls[mid]
        i += 1

        if mid_item == item:
            return mid, i 
        
        if mid_item < item:
            low = mid + 1
            
        else:
            high = mid - 1
            
    return None, i

ls = [rd.randint(0, ls_range) for i in range(ls_len)]
ls = list(set(ls))
    
item = input('0から%dの範囲で数字を入力してください: ' % ls_range)

print(ls)
print(binary_search(ls, int(item)))