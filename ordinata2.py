# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 19:05:15 2021

@author: danie
"""

'''
scrivere una funzione che prende in ingresso una lista di inter e ritorna
True se la i numeri della lista sono ordinati in ordine crescente
'''

def ordinata(lista):
    o = 1
    for indice in range(len(lista)):
        if lista[indice] < lista[o]:
            o += 1
            if o == len(lista):
                break
            else:
                continue
        else:
            return False
    return True
            
def ordinata2(lista):           # soluzione del professore
    for i in range(len(lista)-1):
        if lista[i] > lista[i-1]:
            return False
    return False

print(ordinata([1,2,3,5,3,2,4,5]))
print(ordinata2([1,2,3,4,5,2]))
        
