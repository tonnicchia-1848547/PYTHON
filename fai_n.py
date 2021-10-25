



def fai_n(f, n):
    if n <= 0:
        return 
    f()
    fai_n(f,n-1)

def stampa():
    print('ciao')

fai_n(stampa,5)
