def kysy_salasana ():
    while True:

        syote = input("Anna salasana: ")
        if len(syote) < 8:
            print("Salasanan pituus on vähintään 8 merkkiä.")
            continue
        else:
            return syote

print(kysy_salasana())
