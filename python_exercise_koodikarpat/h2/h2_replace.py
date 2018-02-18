def vaihda_merkit(merkkijono):
    merkkijono = merkkijono.replace("1", "3")
    merkkijono = merkkijono.replace("2", "1")
    merkkijono = merkkijono.replace("3", "2")
    return merkkijono


merkkijono = str(input("Syötä merkkijono: "))
merkkijono = vaihda_merkit(merkkijono)
print(merkkijono)
