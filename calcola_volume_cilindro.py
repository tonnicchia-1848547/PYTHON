

# volume cilintro = pi*r^2
import math

def calcola_volume_cilindro(raggio, altezza):
    pi = math.pi
    volume = (pi * raggio**2) * altezza
    return volume

print(calcola_volume_cilindro(20, 10))
