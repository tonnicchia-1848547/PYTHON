# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 15:03:41 2021

@author: danie
"""

def fai2volte(f, v):
    f(v)
    f(v)
    
def stampa_spam(valore):
    print(valore)
    
def stampa2volte(bruce):
    print(bruce)
    print(bruce)

def fai_quattro(f,v):
    fai2volte(f, v)
    fai2volte(f, v)

fai_quattro(print, 'spam')
