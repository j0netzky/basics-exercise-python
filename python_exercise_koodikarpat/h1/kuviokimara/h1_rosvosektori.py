PI = 3.1416
sade = 13.742
sisakulma = 68

float (sade)
float (sisakulma)

def laske_sektorin_ala(sade, sisakulma):
    return (sisakulma / 360) * PI * (sade ** 2)

ala = laske_sektorin_ala(sade, sisakulma)
print(round(ala, 4))
