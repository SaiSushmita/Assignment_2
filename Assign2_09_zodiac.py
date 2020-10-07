# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 18:42:58 2020

@author: Sushmita
"""
month=input("Enter the month in lower case:\n")
day=int(input("enter the date in digits:\n"))

if month == 'december': 
    z = 'Sagittarius' if (day < 22) else 'capricorn'
      
elif month == 'january': 
    z = 'Capricorn' if (day < 20) else 'aquarius'
          
elif month == 'february': 
    z = 'Aquarius' if (day < 19) else 'pisces'
        
elif month == 'march': 
    z = 'Pisces' if (day < 21) else 'aries'
          
elif month == 'april': 
    z = 'Aries' if (day < 20) else 'taurus'
        
elif month == 'may': 
    z = 'Taurus' if (day < 21) else 'gemini'
          
elif month == 'june': 
    z = 'Gemini' if (day < 21) else 'cancer'
          
elif month == 'july': 
    z = 'Cancer' if (day < 23) else 'leo'
          
elif month == 'august': 
    z = 'Leo' if (day < 23) else 'virgo'
          
elif month == 'september': 
    z = 'Virgo' if (day < 23) else 'libra'
          
elif month == 'october': 
    z = 'Libra' if (day < 23) else 'scorpio'
          
elif month == 'november': 
    z = 'scorpio' if (day < 22) else 'sagittarius'
          
print("Your zodiac sign is:",z)