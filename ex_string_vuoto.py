#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Implementa una funzione leetv(line) che prende come input una stringa
line e la modifica in modo da avere una versione della stringa in
formato leetspeak. Esempio: `Programming Unit 1` diventa `pR09R4mm1N9_uN1t_1`
Per creare la stringa usare le seguenti regole:

    1) 'a', 'i', 'e', 'o', 'z', 's', 'g'
       devono essere sostituite con
       '4', '1', '3', '0', '7', '5', e '9' rispettivamente
       a prescindere che siano lower- or UPPER-case
       (quindi la solita regola si applica a
       'A', 'I', 'E', 'O', 'Z', 'S', e 'G', rispettivamente);

    2) 'f', 'n', 'r', 'w', 'l', 'y' e 'x'  (lower-case) devono essere
       sostituite con la loro versione UPPER-case
       ('F', 'N', 'R', 'W', 'L', 'Y' e 'X', rispettivamente);
    3) tutte gli altri caratteri UPPER-case non menzionati in
       in (1) e (2) devono diventare lower-case (e.g., 'B' diventa 'b',
       mentre 'N' rimane 'N');
    4) ' ' (spazio) deve diventare '_' (underscore);
    5) tutti gli altri caratteri non devono cambiare

   La funzione deve ritornare una tupla definita come:
   - primo elemento della tupla contiene la stringa in leet-version
   - il secondo elemento e' un numero che conta il numero di caratteri
     sostituiti

   Ad esempio input e' `"My name is Neo"`, la funzione
   deve ritornare `('mY_N4m3_15_N30', 12)`.
"""

def leetv(line):
    # la funzione torna il numero di parole modificate
    new_line = ''
    contatore = 0
    stringa_normale =  'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    stringa_anormale = '4bcd3F9h1jkLmN0pqR5tuvWXY7_4bcd3F9h1jkLmN0pqR5tuvWXY7'
    
    # per ogni carattere e spazio nella stringa fai qualcosa:
    for  c in line:
        i = stringa_normale.find(c)
        if i < 0:
            new_line +=c
            continue
        new_line += stringa_anormale[i]
        if stringa_anormale[i] != stringa_normale[i]:
            contatore +=1
    
    return (new_line, contatore)
        
        
def leetv2(line):
    c = 0
    
    
    


if __name__ == '__main__':
    # Valutazione
    tests = [('My name is Neo', ('mY_N4m3_15_N30', 12),),
             ('Follow the White Rabbit!', ('F0LL0W_th3_Wh1t3_R4bb1t!', 13)),
             ('What is the Matrix?', ('Wh4t_15_th3_m4tR1X?', 12))]

    # se assert vi da errore controllate il vostro output rispetto a
    # quello atteso. Se passate un test vi stampa > Test xx PASSED !
    for i, (inp, expt) in enumerate(tests, 1):
        out = leetv(inp)
        assert out == expt, f'\n{"="*50}\noutput {out}\nexpected {expt}\n{"="*50}'
        print(f'> Test {i} PASSED!')
