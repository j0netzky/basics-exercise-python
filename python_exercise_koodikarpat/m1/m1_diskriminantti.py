#Parametrinen diskrimination

def laske_diskriminantti(kerroin_1, kerroin_2, vakio):
    diskriminantti = kerroin_2 ** 2 - 4 * kerroin_1 * vakio
    print(kerroin_1, kerroin_2, vakio)
    return diskriminantti

print(laske_diskriminantti(5 - 8, 4 * 3, 13))
