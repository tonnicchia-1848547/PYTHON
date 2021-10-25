def verifica_fermat():
    a = int(input('inserisci un numero: '))
    b = int(input('inserisci un numero: '))
    c = int(input('inserisci un numero: '))
    n = int(input('inserisci una potenza > di 2: '))
    if (n > 2) and (a**n + b**n == c**n):
        print('porcoddio')
    elif (n > 2) and (a**n + b**n != c**n):
        print('naggiacristo')

verifica_fermat()

        
