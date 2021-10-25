# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 17:51:38 2021

@author: danie
"""

'''
scrivere una funzione che prende in ingresso una lista di interi
e restituisce la somma degli elementi pari meno la somma dei dispari
'''
def somma_sottrai(lista):
    dispari = 0
    pari = 0
    for num in lista:
        if num % 2 == 0:
            pari += num
        else:
            dispari += num
    return pari - dispari


print(somma_sottrai([1,2,3,4,5,6,7,8,9,10]))