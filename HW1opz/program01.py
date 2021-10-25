# -*- coding: utf-8 -*-

''' 
Abbiamo una stringa int_seq contenente una sequenza di interi non-negativi
    separati da virgole ed un intero positivo subtotal.

Progettare una funzione ex1(int_seq, subtotal) che
    riceve come argomenti la stringa int_seq e l'intero subtotal e
    restituisce il numero di sottostringhe di int_seq
    la somma dei cui valori è subtotal.

Ad esempio, per int_seq='3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2' e subtotal=9,
    la funzione deve restituire 7.

Infatti:
'3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2'
 _'0,4,0,3,1,0,1,0'_____________
 _'0,4,0,3,1,0,1'_______________
 ___'4,0,3,1,0,1,0'_____________
____'4,0,3,1,0,1'_______________
____________________'0,0,5,0,4'_
______________________'0,5,0,4'_
 _______________________'5,0,4'_

NOTA: è VIETATO usare/importare ogni altra libreria a parte quelle già presenti

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test (sulla VM)

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
    (ad esempio editatelo dentro Spyder)



sum(list, tuple, dict) ---> somma gli elementi all'interno

si può usare per le anche con le sottosequenze dei tipi iterabili
es:
    l = [1,2,3,4,5]
    sum(l[0:1])
out: 1

'''
def ex1(int_seq, subtotal):
    """
    Parameters
    ----------
    int_seq : Sequenza di interi.
    
    subtotal : Intero rappresentante 
    le sottostringhe da cercare in int_seq

    Returns: 
    Il numero di sottostringhe trovate all'interno della int_seq.
    
    -------
    None.

    """
    # trasformo la sequenza di interi in una lista di interi type(int)
    lista_interi = [int(n) for n in int_seq.split(',')]
    # creo un contatore da aggiornare ongi volta che sum(lista_interi[i:i+i^e]) == 9
    counter = 0
    # creo una sottolista
    substr = []
    for el in range(len(lista_interi)):
        elemento = lista_interi[el]
        print(f'\nSubstr: {substr} Elemento: {elemento}')
        # se substrin[1,2,3] = 6 + 3 == 9 
        if (sum(substr)+ elemento) == subtotal:
            # aggiorna il contatore 
            counter += 1
            # appendi elemento
            substr.append(elemento)
        elif (sum(substr)+ elemento) > subtotal:
            
        
    
    return counter

        

if __name__ == '__main__':
    int_seq='3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2'
    subtotal=9
    ex1(int_seq, subtotal)
    

