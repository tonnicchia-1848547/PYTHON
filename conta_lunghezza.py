# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 16:34:51 2021

@author: danie
"""

'''
scrivere una funzione che prense in input una stringa composta da parole separate
da uno o più spazi, e ritorna una lista in cui ogni elemento è la lunghezza 
della parola nella lista originaria
'''


def conta_lunghezza(stringa):
    l = stringa.split()
    lista_lunghezza = []
    for parola in l:
        lista_lunghezza.append(len(parola))
    return lista_lunghezza
    

# pythonic way
def conta_lunghezze_2(stringa):
    l = [len(parola) for parola in stringa.split()]
    return l    

def conta_lunghezze_ricorsivo(stringa):
    stringa = stringa.strip()
    if stringa == " ":
        return []
    if " " not in stringa:
        return [len(stringa)]
    i = 1
    while " " not in stringa[:i+1]:
        i += 1
    return [i] + conta_lunghezze_ricorsivo(stringa[i:])
    
print(conta_lunghezza('devo comprare   il   regalo a mio zio'))