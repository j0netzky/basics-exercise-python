def nopeus():
    nopeus = (matka / 1000) / (aika / 3600)
    print("{matka:.2f} metriä {aika:.2f} sekunnissa kulkeneen auton nopeus on {nopeus:.2f} km/h.".format(matka=matka, aika=aika, nopeus=nopeus))


matka = float(input("Anna auton kulkema matka(m): "))
aika = float(input("Anna matkaan kulunut aika(s): "))

nopeus()
