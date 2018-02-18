#Funktiot

#Yhteenlaskufunktio
def yhteenlasku():
    try:
        luku1 = float(input("Anna luku 1: "))
        luku2 = float(input("Anna luku 2: "))
    except ValueError:
        print("Ei tämä ole mikään luku")
    else:
        luku = luku1 + luku2
        print("Tulos: {l}".format(l = luku))
#Vähennyslaskufunktio
def vahennyslasku():
    try:
        luku1 = float(input("Anna luku 1: "))
        luku2 = float(input("Anna luku 2: "))
    except ValueError:
        print("Ei tämä ole mikään luku")
    else:
        luku = luku1 - luku2
        print("Tulos: {l}".format(l = luku))
#Kertolaskufunktio
def kertolasku():
    try:
        luku1 = float(input("Anna luku 1: "))
        luku2 = float(input("Anna luku 2: "))
    except ValueError:
        print("Ei tämä ole mikään luku")
    else:
        luku = luku1 * luku2
        print("Tulos: {l}".format(l = luku))
#Jakolaskufunktio
def jakolasku():
    try:
        luku1 = float(input("Anna luku 1: "))
        luku2 = float(input("Anna luku 2: "))
    except ValueError:
        print("Ei tämä ole mikään luku")
    if luku2 == 0:
        print("Tällä ohjelmalla ei pääse äärettömyyteen")
    else:
        luku = luku1 / luku2
        print("Tulos: {l}".format(l = luku))

#Input

valinta = input("Valitse operaatio (+, -, *, /) : ")

#Päävalikko

if valinta == "+" or valinta == "yhteenlasku":
    yhteenlasku()
elif valinta == "-" or valinta == "vahennyslasku":
    vahennyslasku()
elif valinta == "*" or valinta == "kertolasku":
    kertolasku()
elif valinta == "/" or valinta == "jakolasku":
    jakolasku()
else:
    print("Operaatiota ei ole olemassa.")
