def laske_pituus(janat):            #janan pituus saadaan käyttämällä pythagoraan lausetta z^2 = (x1 - x0)^2 + (y1 - y0)^2
    janat = (((janat[3] - janat[1]) ** 2) + ((janat[2] -janat[0]) ** 2)) ** 0.5
    return janat



janat = [[1, 2, 3, 4], [1, 1, 10, 10], [0, 0, 2, 0]]
janat.sort(key=laske_pituus, reverse=True)
print(janat)
