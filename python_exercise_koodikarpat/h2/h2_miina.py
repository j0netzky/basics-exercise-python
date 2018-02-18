leveys = int(input("Anna kentän leveys: "))
korkeus = int(input("Anna kentän korkeus: "))

if leveys <= 0 or korkeus <= 0:
    print("Noin pienelle kentälle ei mahdu ainuttakaan pistettä!")
else:

    x = int(input("Anna x-koordinaatti: "))
    y = int(input("Anna y-koordinaatti: "))



    if x == leveys - 1 and y == korkeus - 1 or x == 0 and y == 0 or x == leveys - 1 and y == 0 or x == 0 and y == korkeus - 1:
        print("Antamasi piste ({x},{y}) on kentän nurkassa.".format(x=x, y=y))

    #Reuna

    elif x == leveys - 1 and 0 < y <= korkeus - 2 or y == korkeus - 1 and 0 < x <= leveys - 2:
        print("Antamasi piste ({x},{y}) on kentän laidalla.".format(x=x, y=y))

    #Ulkona

    elif x >= leveys or y >= korkeus or x < 0 or y < 0:
        print("Antamasi piste ({x},{y}) on kentän rajojen ulkopuolella!".format(x=x, y=y))

    #Keski = kaikki muut kuin edellä

    else:
        print("Antamasi piste ({x},{y}) on kentän keskellä.".format(x=x, y=y))
