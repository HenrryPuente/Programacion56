# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 11:33:02 2020

@author: PC
"""
def fibonacci(n):
    a, b = 0,1
    while a <= n:
        print(a, end=" ")
        """ c=a+b
        a=b
        b=c"""
        a, b = b, a+b
        print()
fibonacci(8)
        