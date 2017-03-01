#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 22:11:14 2017

@author: JuienLo
"""

import random

ans = random.randint(1,9)
tried = 0;

while True:
    cmd = input("Guess a number? ")
    if cmd == 'exit':
        break
    tried+=1
    if int(cmd) == ans:
       print("Right! Good Job!") 
       break
    elif int(cmd) < ans:
        print("Too Low!")
    else:
        print("Too High!")
    

print("You have tried", tried, "times")
print("Correct ans is",ans)