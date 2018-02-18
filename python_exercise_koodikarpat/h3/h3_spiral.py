from turtle import *

def piirra_spiraali(vari, kaarien_lkm, sade, kasvu, viivan_paksuus=1):

    color(vari)
    pensize(viivan_paksuus)

    for r in range(kaarien_lkm):
        circle(sade, 90)
        sade = sade+kasvu

piirra_spiraali("black", 20, 10, 3)
piirra_spiraali("red", 10, 20, 4, 3)
piirra_spiraali("blue", 10, -20, -4, 3)
done()
