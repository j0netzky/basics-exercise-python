def pyyda_syote(syote, virheilmoitus):
    """Kysyy käyttäjältä kokonaislukua käyttäen kysymyksenä parametrina annettua merkkijonoa. Virheellisen syötteen kohdalla käyttäjälle näytetään toisena parametrina annettu virheilmoitus. Käyttäjän antama kelvollinen syöte palautetaan kokonaislukuna. Hyväksyy vain luvut jotka ovat suurempia kuin 1."""

    while True:
        try:
            luku = int(input(syote))
            if luku <= 1:
                print(virheilmoitus)
                continue
        except ValueError:
            print(virheilmoitus)
        else:
            return luku

def tarkista_alkuluku(luku):
    """Tarkistaa onko parametrina annettu luku alkuluku. Palauttaa False jos luku ei ole alkuluku; jos luku on alkuluku palautetaan True"""
    for i in range(2, int(luku / 2 + 1)):
        if (luku % i) == 0:
            return False


    return True



luku = pyyda_syote("Anna kokonaisluku, joka on suurempi kuin 1: ", "Pieleen meni :'(")
luku = tarkista_alkuluku(luku)
if luku:
    print("Kyseessä on alkuluku.")
else:
    print("Kyseessä ei ole alkuluku.")
