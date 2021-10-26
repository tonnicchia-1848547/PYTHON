
"""
Created on Wed Oct 20 16:16:10 2021

@author: danie
"""

'''
scrivere una funzione che prense in input una stringa composta da parole separate
da uno o più spazi, e ritorna una lista in cui ogni elemento è la lunghezza 
della parola nella lista originaria
'''


def conta_lunghezze(stringa):
    # elimino gli spazi e creo una lista di parole con la split
    l = stringa.split()
    lista_lunghezza = []
    for parola in l:
        lista_lunghezza.append(len(parola))
    return lista_lunghezza


# pythonic way
def conta_lunghezze2(stringa):
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
        
    
print(conta_lunghezze_ricorsivo('mammamia come stai messo'))   
        
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

def ordinata2(lista):
    if len(lista) <= 1:
        return True
    # se ho solo due elementi 
    elif lista[0] < lista[1]:
        # True chiama da i+1 nella lista escludendo quello che hai già controllato
        return ordinata2(lista[1:])
    # altrimenti se > 
    return False
    
print(ordinata([12,3,5,4]))
    

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
    if n == 0:
        return '0'
    return str(n) + " " + countdown_ricorsivo2(n-1)
        
    
#print(countdown_ricorsivo(5))



"""
scrivere una funzione ricorsiva che prende una lista di interi e 
stampa a video soltato gli elementi della lista multipli di 3
"""
def stampa_tre(lista):
    if len(lista) == 0:
        return
    if lista[0] % 3 == 0:
        print(lista[0])
    return stampa_tre(lista[1:])
    

stampa_tre([1,2,3,4,5,6,7,8,9])
            
