def pyyda_syote(syote, virheilmoitus):
    """Kysyy käyttäjältä kokonaislukua käyttäen kysymyksenä parametrina annettua merkkijonoa. Virheellisen syötteen kohdalla käyttäjälle näytetään toisena parametrina annettu virheilmoitus. Käyttäjän antama kelvollinen syöte palautetaan kokonaislukuna."""

    while True:
        try:
            luku = int(input(syote))
        except ValueError:
            print(virheilmoitus)
        else:
            return luku

luku = pyyda_syote("Anna kokonaisluku: ", "Et antanut kokonaislukua")
print("Annoit kokonaisluvun {}! Nohevaa toimintaa!".format(luku))
hemulit = pyyda_syote("Montako hemulia mahtuu muumitaloon? ", "Tämä ei ollut kelvollinen hemulien lukumäärä!")
print("Muumitaloon mahtuu {} hemulia".format(hemulit))
