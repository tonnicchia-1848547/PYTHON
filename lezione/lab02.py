# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 15:52:52 2021

@author: danie

scrivere una funzione che prende in ingresso che prende tre interi(g, m, a)
e ritorna TRUE se (g,m,a) se corrisponde ad una data valida 
FALSE altrimenti
"""


def date(g,m,a):
    bis = bisestile(a)
    
    if m  in  (1,3,5,7,9,10,12):
        if g > 31 and g < 1:
            return False
        else:
            return True, bis
    elif m in (11,4,6,8):
        if g > 30 and g < 1:
            return False
        else:
            return True, bis
    elif m == 2:
        if g > 28 and g < 1:
            return False
        else:
            return True, bis
    else:
        return False
    
    
def bisestile(anno):
    
    if anno % 400 == 0 or anno % 4 == 0 and anno % 100 != 0:
        return 'bisestile'
    else:
        return 'non bisestile'
print(date(11, 5, 2000))


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
            

'''
scrivere una funzione che prense in ingresso una lista di coppie di numeri
e rutornra True se le  tutte le coppie sono composte da  interi di cui uno è divisibile 
per l'altro, False altrimenti
'''

def coppie(lista):
    controllo = 0
    for coppia in lista:
        a,b = coppia
        if a % b == 0:
            controllo += 1
        elif b % a == 0:
            controllo += 1
    if controllo == len(lista):
        return True
    else:
        return False
        
print(coppie([(4,2), (3,6), (10,1)]))
        
def coppie2(lista):
    for coppia in lista:
        if coppia[0] % coppia[1] == 0 or coppia[1] % coppia[0] == 0:
            continue
        else:
            return False
    return True
        
print(coppie2([(4,2), (3,6), (10,1)]))        
            
def coppie3(lista):
    for coppia in lista:
        a,b = coppia
        if a % b == 0:
            return True
        elif b % a == 0:
            return True
        else:
            return False
        

def coppia4(lista):     # versione del professore lol tre righe di codice lol2
    for c in lista:
        a,b = c
        if a % b != 0 and b % a != 0:
            return False
    return True
     

     
def divisibile(a,b):
    return a % b == 0

def coppia5(lista):
    for c in lista:
        a,b = c
        if not divisibile(a, b) and not divisibile(b, a):
            return False
    return True


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
        



























