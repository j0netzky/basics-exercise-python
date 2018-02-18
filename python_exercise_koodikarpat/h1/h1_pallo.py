PI = 3.1416

#V = 4 / 3 * PI * r^3 Matikkakaava menis näin
#A = 4 * PI * r^2 -||-

def laske_ala(sade): #Funktion määritys
    return 4 * PI * sade ** 2

def laske_tilavuus(sade): #Funktion määritys
    return (4 / 3) * PI * sade ** 3

#Säteen selville saamasiksei:
    #p = 2 * PI * r
    #r = p / (2 * pi)

def laske_sade(piiri): #Määritys
    return piiri / (PI * 2)

def laske_pallon_ominaisuudet(piiri): #funktion määritys
    sade = laske_sade(piiri)
    ala = laske_ala(sade)
    tilavuus = laske_tilavuus(sade)
    return ala, tilavuus

#Lasku
print("Tämä ohjelma laskee pallon tilavuuden ja pinta-alan, kun tiedetään pallon ympärysmitta")
piiri = 23
ala, tilavuus = laske_pallon_ominaisuudet(piiri)
print("Ympärysmitta:")
print(piiri)
print("Tilavuus:")
print(round(tilavuus, 4))
print("Pinta-ala:")
print(round(ala, 4))
