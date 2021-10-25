# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 15:53:45 2021

@author: danie
"""

import turtle

def disegna(t, lunghezza, n):
    if n == 0:
        return
    angolo = 90
    t.fd(lunghezza * n)
    t.lt(angolo)
    disegna(t, lunghezza, n-1)
    t.rt(2*angolo)
    disegna(t, lunghezza, n-1)
    t.lt(angolo)
    t.bk(lunghezza * n)
    
    
def koch(t, lunghezza, n):
    if n < 10:
        t.fd(n)
        return
    m = n/3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)
 
bob = turtle.Turtle()

disegna(bob, 5, 7)
