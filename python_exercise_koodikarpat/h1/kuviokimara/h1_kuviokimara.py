PI = 3.1416

#1. Neliö
#2. Neliön ja puoliympyrän sektori
#3. Jäljelle jäävät kaksi 21.5 asteen sektoria
#4. Suorakulmainen kolmio - toinen 21.5 asteen sektoreista
#5. Neliö - puoliympyrän sektori
#6 puoliympyrän pinta-ala = sama kuin toisen puolen
#7 1/4 iso ympyrä = iso neliö + puoliympyrä

# Nelion pinta-ala

def laske_nelion_ala(x):
    nelion_ala = x ** 2
    return nelion_ala
#suorakulmaisen kolmion pinta-ala

def laske_kolmion_ala(x):

    kolmion_ala =  1 / 2 * (x ** 2)
    return kolmion_ala

#neliön halkaisija


    #halkaisija = ison ympyrän säde
def laske_halkaisija(x):

    halkaisija = ((2 ** 0.5) * x)
    return halkaisija


#vasemmanpuoleisimman sektorin pinta-ala

def laske_sektorin_ala(d):
    sektorin_ala =  (45/360) * PI * (d / 2) ** 2
    return sektorin_ala


def laske_ympyran_ala (d):
    a = PI * d ** 2
    return a

#ison neliön pinta-ala

def laske_suuren_nelion_ala(d):
    a = d ** 2
    return a

def laske_kuvion_ala(x):
    d = laske_halkaisija(x)
    ala = laske_suuren_nelion_ala(d) + (3 / 4) * laske_ympyran_ala (d) + laske_nelion_ala (x) + laske_kolmion_ala (d / 2) + laske_sektorin_ala (d)

    a = round(ala, 3)
    return a

#Koko kuvion pinta-ala

# 3/4 iso ympyrä + iso neliö + suorakulmainen kolmio + neliö + vasen sektori

#def laske_kuvion_ala(suuren_nelion_ala, ympyran_ala, nelion_ala, kolmion_ala, sektorin_ala):
#    return suuren_nelion_ala + 3 / 4 * ympyran_ala + nelion_ala + kolmion_ala + sektorin_ala
def main(x):

    a = round(laske_kuvion_ala(x), 3)
    print(a)

x = 3.467

main(x)
