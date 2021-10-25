deb1 = -4
deb2 = -2
mitt = 3
int1 = 0
int2 = 0

# devo estinguere prima il deb1
def estinguere(deb1,deb2,mitt,int1,int2):
    # debito1 è maggiore di deb2
    if deb1 < deb2:
        if abs(deb1) < mitt:
            # capire se il mittente ha un numero maggiore di fondi
            # rispetto al debito che deve pagare per determinare
            # cosa fare prima o dopo
            print(True, "può estinguere il debito")
        else:
            # in questo caso non ha abbastanza fondi
            # quindi trasferisco quello che ha e abbasso il debito
            print("non ha abbastanza fondi per estinguere il debito")

    # debito2 è maggiore di deb1
    else:
        if abs(deb2) < mitt:
            # capire se il mittente ha un numero maggiore di fondi
            # rispetto al debito che deve pagare per determinare
            # cosa fare prima o dopo
            print(True, "può estinguere il debito 2")
        else:
            # in questo caso non ha abbastanza fondi
            # quindi trasferisco quello che ha e abbasso il debito
            print("non ha abbastanza fondi per estinguere il debito 2")

estinguere(deb1, deb2, mitt, int1, int2)
