#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 20:48:45 2017

@author: JuienLo
"""
try:
    num = int(input("Enter a number:"))
    if num % 4 == 0:
        print("Can be divided by four!")
    elif num % 2 ==0:
        print("Even!")
    else:
        print("Odd!")
    
except:
    print("Plz enter the corrct format!")