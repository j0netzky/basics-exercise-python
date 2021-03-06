def tarkista_koordinaatit(x, y, leveys, korkeus):
    """Tarkistaa ovatko annetut x, y -koordinaatit annettujen rajojen sisällä.
    Palauttaa True, jos koordinaatit ovat rajojen sisällä; muuten palautetaan False."""

    print("Tarkistetaan koordinaatit")
    if x <= leveys - 1 and y <= korkeus - 1 and x >= 0 and y >= 0:
        print("Koordinaatit ovat alueella")
        return True
    else:
        print("Koordinaatit eivät ole alueella")
        return False

def kysy_koordinaatit(leveys, korkeus):
    """Pyytää käyttäjältä koordinaatteja kunnes käyttäjä antaa kaksi kokonaislukua,
    joista molemmat ovat annetun kentän rajojen sisäpuolella, tai tyhjän syötteen.
    Palauttaa saadut koordinaatit. Jos käyttäjä antaa tyhjän syötteen, palautetaan kaksi None-arvoa."""

    while True:
        try:
            koordinaatit = input("Anna koordinaatit tai lopeta tyhjällä: ").split(" ", 1)
            print(koordinaatit)
            if koordinaatit == ['']:
                print("X tai Y on tyhjä arvo")
                break

            x = int(koordinaatit [0])
            y = int(koordinaatit [1])

        except ValueError:
            print("Anna koordinaatit kokonaislukuina")
        except IndexError:
            print("Anna kaksi koordinaattia välilyönnillä erotettuna")

        else:
            print("Seuraava funktio")
            tarkista_koordinaatit(x, y, leveys, korkeus)
            return x, y

def avaa_ruutuja(kentta):
    """Avaa pelikentällä olevia ruutuja merkitsemällä ne x:llä.
    Avattavia ruutuja kysytään käyttäjältä kunnes tämä haluaa lopettaa antamalla tyhjän syötteen.
    Kentän tila tulostetaan jokaisen avauksen jälkeen."""

    while True:
        try:
            # leveys = int(input("Anna kentän leveys: "))
            # korkeus = int(input("Anna kentän korkeus: "))
            dimensio = input("Anna kentän leveys ja korkeus muodossa (lxk): ").split("x", 1)

            leveys = int(dimensio[0])
            korkeus = int(dimensio[1])
            if leveys <= 0 or korkeus <= 0:
                print("Noin pienelle kentälle ei mahdu ainuttakaan pistettä!")
                continue

        except ValueError:
            print("Anna luku")

        else:
            kysy_koordinaatit(leveys, korkeus)
            print("Ennen kentän luontia")

            k = korkeus - 1
            l = leveys - 1
            merkki = ["o " * l]
            kentta = []
            for i in range(0,k):
                kentta.append(merkki)
            for rivi in kentta:
                for alkio in rivi:
                    print(alkio)
            break
    print("Ennen x:n laittoa")
    for x in range(l):
        for y in range(k):
            #kentta.insert(0, "x")
            kentta.insert(1, "x")
    for rivi in kentta:
        for alkio in rivi:
            print(alkio)

#################################Pääohjelma#################################

avaa_ruutuja(kentta=[])
