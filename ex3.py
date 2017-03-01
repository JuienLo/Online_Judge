#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 21:01:50 2017

@author: JuienLo
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
for i in a:
    if i < 5:
        print(i)
        #extra1
        new_list.append(i)

print(new_list)

#extra2
num = int(input("Enter a number: "))

for i in a:
    if i < num:
        print(i)


        
