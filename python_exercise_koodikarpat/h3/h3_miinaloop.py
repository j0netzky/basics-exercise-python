def tarkista_koordinaatit(x, y, leveys, korkeus):
    """Tarkistaa ovatko annetut x, y -koordinaatit annettujen rajojen sisällä. Palauttaa True, jos koordinaatit ovat rajojen sisällä;
    muuten palautetaan False."""

    if x <= leveys - 1 and y <= korkeus - 1:
        return True
        print("Koordinaatit ovat kentällä")
    elif x < 0 and y < 0:
        return False
        print("Koordinaatit eivät ole kentällä!")

def kysy_koordinaatit(leveys, korkeus):
        """Pyytää käyttäjältä koordinaatteja kunnes käyttäjä antaa kaksi kokonaislukua, joista molemmat ovat annetun kentän rajojen sisäpuolella,
        tai tyhjän syötteen. Palauttaa saadut koordinaatit. Jos käyttäjä antaa tyhjän syötteen, palautetaan kaksi None-arvoa."""
        x = int(input("Anna x-koordinaatti: "))
        y = int(input("Anna y-koordinaatti: "))

        while True:
            try:
                tarkistus = tarkista_koordinaatit(x, y, leveys, korkeus)

                if x == "" or y == "":
                    return None
            except ValueError:
                pass
            else:
                return x, y
#Paaohjelma
leveys = int(input("Anna kentän leveys: "))
korkeus = int(input("Anna kentän korkeus: "))

if leveys <= 0 or korkeus <= 0:
    print("Noin pienelle kentälle ei mahdu ainuttakaan koordinaattia!")
kysy_koordinaatit(leveys, korkeus)
