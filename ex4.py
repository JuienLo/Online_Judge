#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 21:08:58 2017

@author: JuienLo
"""

num = int(input("Enter a number: "))
num_list = range(1,num+1)
d_list = []
for i in num_list:
    if num % i ==0:
        d_list.append(i)
        
print(d_list)