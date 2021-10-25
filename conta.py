# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 17:42:59 2021

@author: danie
"""

'''
scrivi una funzione che prende una stringa e un carattere e ritorna quante volte quel 
carattere è ripetuto nella stringa
'''

def conta(stringa, carattere):
    contatore = 0
    for c in stringa:
        if c == carattere:
            contatore += 1
        
    return contatore

print(conta('mammamia', 'm'))