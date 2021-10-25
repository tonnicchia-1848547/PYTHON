import turtle
import math
bob = turtle.Turtle()

print(bob)




def quadrato(t,lunghezza):
    for i in range(4):
        t.fd(lunghezza)
        t.lt(90)

def poligono(t,lunghezza, n):
    angolo = 360/n
    for i in range(n):
        t.fd(lunghezza)
        t.lt(angolo)

def cerchio(t, r):
    circonferenza = 2 * math.pi * r
    n = int(circonferenza / 3) + 3
    lunghezza = circonferenza/n
    poligono(t, lunghezza, n)

def arco(t, r , angolo):
    arco_lunghezza = 2 * math.pi * r * angolo/360
    n = int(arco_lunghezza / 3) + 1
    passo_lunghezza = arco_lunghezza / n
    passo_angolo = angolo / n
    
    for i in range(n):
        t.fd(passo_lunghezza)
        t.lt(passo_angolo)

    
angolo(bob, 100, 90)
cerchio(bob, 10)
poligono(bob, 100, 9)
quadrato(bob, 50)

turtle.mainloop()
