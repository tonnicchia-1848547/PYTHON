# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 16:34:23 2021

@author: danie
"""

def a(m,n):
    if m == 0:
        n+1
    elif m > 0 and n == 0:
        a(m-1,1)
    elif m > 0 and n > 0:
        a(m-1,a(m, n-1))
    else:
        return
    
a(3,4)