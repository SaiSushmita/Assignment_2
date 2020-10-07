# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 17:00:38 2020

@author: Sushmita
"""

number=float(input("enter the number="))
Rev = 0
x=number
while(number > 0):
    Rem = number %10
    Rev = (Rev *10) + Rem
    number = number //10
print("reverse of the entered number=",Rev)
if(x==Rev):
   print("the number and the reversed is same")
else:
   print("the number and the reversed number is different")
   