
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
