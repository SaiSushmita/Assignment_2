# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 20:39:37 2020

@author: Sushmita
"""

class InpOutString:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())

strObj = InpOutString()
strObj.getString()
strObj.printString()