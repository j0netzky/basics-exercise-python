import math
hypotenuusa = 13.753

float(hypotenuusa)

def laske_sivun_pituus (hypotenuusa):
    return hypotenuusa / math.sqrt(2)

# kanta = hypotenuusa ?

# c^2 = a^2 + b^2
# c^2 = a^2 + a^2
# c^2 = 2 * a^2
# c = 2 // 2 * a
# a = c / (2//2)



pituus = laske_sivun_pituus (hypotenuusa)
print (round(pituus, 4))
