# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 18:20:25 2021

@author: danie
"""
"""
scrivere una funzione che prende in input una lista di interi
ed incrementa ogni elemento di 1 nella lista
"""

def incrementa_lista(lista):
    for e in range(len(lista)):
        lista[e] += 1
    return lista

def incrementa_lista2(lista):
    for i, e in enumerate(lista):
    #   0, 1
    #   1, 2
    #   2, 3
        lista[i] = e+1
    return lista

# PYTONATA
def incrementa_lista3(lista):
    l = [valore +1 for valore in lista]
    # schiaffa tutti i valori di l nella lista LISTA 
    lista[:] = l
    
    
print(incrementa_lista([1,2,3,4,5]))
print(incrementa_lista2([1,2,3,4,5]))

