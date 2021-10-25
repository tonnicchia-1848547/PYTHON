# -*- coding: utf-8 -*-


"""
3 0 4 0 3 1 0 1 0 1 0 0 5 0 4 2
# se il primo elemento non è uguale a 9 
3 --> no
# allora aggiunto un altro elemento  e lo riconfronto
3 0 --> no
3 0 4 --> no
3 0 4 0 --> no
# se somma dei numeri nella lista è > di 9
3 0 4 0 3 --> NO!
"""

"""
# corri avanti di un indice da dove ti trovavi
0 4 0 3 --> no
# continua con le somme ripetute finche non trovi TRUE o FALSE
0 4 0 3 1 --> no
0 4 0 3 1 0 --> no
# aggiorno il contatore
# controllo anche se la situazione successiva mi da True
0 4 0 3 1 0 1 --> SI! aggiorna il contatore
# aggiorno il contatore 
# controllo se anche la situazione successiva mi da True
0 4 0 3 1 0 1 0 --> SI! aggiorna il contatore
# somma dei numedi nella lista è > di 9
0 4 0 3 1 0 1 0 1 --> NO! 
"""

"""
# corri avanti di un indice 
# 
4 0 3 1 0 1 0 --> SI! aggiorna il contatore
4 0 3 1 0 1 0 1 --> NO!

0 3 1 0 1 0 1 --> no
0 3 1 0 1 0 1 0 --> no
0 3 1 0 1 0 1 0 0 --> no
0 3 1 0 1 0 1 0 0 5 --> NO!

3 1 0 1 0 1 0 0 5 --> NO!

1 0 1 0 1 0 0 5 --> no
1 0 1 0 1 0 0 5 0 --> no
1 0 1 0 1 0 0 5 0 4 --> NO!

0 1 0 1 0 0 5 0 4 --> NO!

1 0 1 0 0 5 0 4 --> NO!

0 1 0 0 5 0 4 --> NO!

1 0 0 5 0 4 --> NO!

0 0 5 0 4 --> SI! aggiorna il contatore

0 5 0 4 --> SI! aggiorna il contatore

5 0 4 --> SI! aggiorna il contatore








"""