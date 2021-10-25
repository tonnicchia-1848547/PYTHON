# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 18:29:48 2021

@author: danie
"""

"""
SCRIVERE UNA FUNZIONE CHE PRENDE IN INPUT UN NUMERO INTERO 
E RESTITUISCE UNA STRINGA CON IL COUNTDOWN DA n A O.
I NUMERI SONO SEPARATI DA UNO SPAZIO
"""
def countdown(numero):
    numbers = ''
    while numero >= 0:
        numbers += str(numero)+' '
        numero -= 1
    return numbers[:-1], type(numbers)

# this is my cagata
def countdown_ricorsivo(numero):
    da = str(numero)    #5
    stringa_da_riempire = ""
    if da != 0:         # se non è 0
        stringa_da_riempire + " "+da
        countdown_ricorsivo(numero - 1)
    return stringa_da_riempire

# il prof ha fatto::
def countdown_ricorsivo2(n):
    return '0'  if n == 0 else f'{n}' + countdown_ricorsivo2()
print(countdown_ricorsivo(5))
