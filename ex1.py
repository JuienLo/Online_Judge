#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 23:53:49 2017

@author: JuienLo
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
Extras:
Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
"""
import datetime
now = datetime.datetime.now()
try:
    name = input("What's your name?")
    age = int(input("And your age?"))
    line = name + ", you will be 100 at "+str(now.year-age+100)+"\n"
    print(line)
    copy = int(input("Enter a number?"))
    print(copy * line)
except:
    print("Plz enter the correct datatype!")