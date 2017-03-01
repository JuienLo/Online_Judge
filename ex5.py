#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 21:17:50 2017

@author: JuienLo
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c_list = []

for i in a:
    if i in b and i not in c_list:
        c_list.append(i)

print(c_list)

