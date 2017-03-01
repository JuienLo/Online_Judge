#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 21:59:32 2017

@author: JuienLo
"""
while(True):
    a = input("A player? ")
    b = input("B player? ")
    if a == b:
        print("Tie")
    elif a == "rock":
        if b == "scissors":
            print("A Wins")
        else:
            print("B Wins")
    elif a == "scissors":
        if b == "rock":
            print("B Wins")
        else:
            print("A Wins")
    elif a == "paper":
        if b == "scissors":
            print("B Wins")
        else:
            print("A Wins")
        
    cmd = input("Again?(y/n) ")
    if cmd == "n":
        break
