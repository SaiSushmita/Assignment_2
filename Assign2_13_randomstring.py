# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 20:15:09 2020

@author: Sushmita
"""

import random
import string
s=input("Enter a string in lower case, preferably a short string\n")
length = len(s)

letters = string.ascii_lowercase
while(1):
    result_str = ''.join(random.choice(letters) for i in range(length))
    if result_str == s:
        break
print("Random string of length", length, "is:", result_str, " which is same as the given string", s)