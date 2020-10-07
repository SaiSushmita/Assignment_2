# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 19:34:53 2020

@author: Sushmita
"""

hour=float(input("Enter the hour in decimals\n"))
ampm=input("Enter whether it is AM or PM in capitals\n")

if ampm == 'AM':
    print( int(hour), ":", int((hour%int(hour)*60)), "Hrs")
elif int(hour)==12:
    print( (int(hour)),":", int((hour%int(hour))*60), "Hrs")
else:
    print( (int(hour)+12),":", int((hour%int(hour))*60), "Hrs")