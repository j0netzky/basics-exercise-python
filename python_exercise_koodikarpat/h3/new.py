l = 7 - 3
k = 6 - 2
merkki = ["o " * l]
kentta = []
# for i in range(0,l):
#     kentta.append(merkki)
# for rivi in kentta:
#     for alkio in rivi:
#         print(alkio, end="")
#     print("\n")

for i in range(0,k):
    kentta.append(merkki)
    print(kentta) #päällimmäinen lista
for rivi in kentta:
    print(rivi) #listan sisällä oleva lista
    for alkio in rivi:
        print(alkio) #listan sisällä olevan listan arvo
