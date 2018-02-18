def laske_pituus(janat):            #janan pituus saadaan käyttämällä pythagoraan lausetta z^2 = (x1 - x0)^2 + (y1 - y0)^2
    janat = (((janat[3] - janat[1]) ** 2) + ((janat[2] -janat[0]) ** 2)) ** 0.5
    return janat



pituus = laske_pituus([1, 1, 2, 1])
print(pituus)
