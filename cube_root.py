# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 20:35:13 2021

@author: anves
"""

x=int(input("enter the number to see if it has cube root"))

count=0

while(count**3<x):
    count=count+1
if(count**3!=x):
    print("Cube root doesn't exist")
else:
    print("Cube root exists")
    
