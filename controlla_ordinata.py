# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 17:50:22 2021

@author: danie
"""

"""
scrivere una funzione che prende in input una lista di numeri
e ritorna True se la lista è ordinata crescente
False altrimenti
"""
def ordinata(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return False
    return True

def ordinata_ricorsiva(lista):
    if len(lista) <= 1:
        return True
    # se ho solo due elementi 
    elif lista[0] < lista[1]:
        # True chiama da i+1 nella lista escludendo quello che hai già controllato
        return ordinata_ricorsiva(lista[1:])
    # altrimenti se > 
    return False

print(ordinata([12,3,5,4]))