#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 21:27:23 2017

@author: JuienLo
"""

test = input("Enter a word: ")
index = int(len(test)/2)
print(index)
           
a = test[:index]
print(a)

b = test[:-index-1:-1]
print(b)

if a == b:
    print("palindrome!")
else:
    print("QAO")