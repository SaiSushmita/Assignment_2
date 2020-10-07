# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 20:43:56 2020

@author: Sushmita
"""
balance = 0
while(1):
    s = input("Enter Deposit or Withdral data\n")
    sarr = s.split(' ')
    transac = sarr[0]
    amount = int(sarr[1])
    if transac == 'D':
        balance = balance + amount
    else:
        balance = balance - amount
    print("Balance is:",balance)
    x = input("Do you want to continue? y/n\n")
    if x == 'y' or x =='Y':
        continue
    else:
        break
