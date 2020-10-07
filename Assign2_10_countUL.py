# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 19:31:24 2020

@author: Sushmita
"""

s=input("Enter string:")
upper=lower=number=special=0
for i in range(len(s)): 
        if s[i].isupper(): 
            upper += 1
        elif s[i].islower(): 
            lower += 1

print("The number of lowercase characters are=",lower)
print("The number of uppercase characters are=",upper)
