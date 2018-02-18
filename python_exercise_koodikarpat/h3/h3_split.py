def pyyda_maalit():
    """Pyytää käyttäjältä ottelun lopputuloksen ja palauttaa syötetyn tuloksen kokonaislukuina."""
    while True:
        try:
            luku = input("Anna ottelun lopputulos: ").split("-", 1)
            maali1 = int(luku[0])
            maali2 = int(luku[1])
        except (ValueError, IndexError):
            print("Anna tulos muodossa <maalit 1>-<maalit 2>!")
        else:
            return maali1, maali2

maali1, maali2 = pyyda_maalit()
print("Joukkueiden välinen maaliero on {}".format((maali1 - maali2)))
