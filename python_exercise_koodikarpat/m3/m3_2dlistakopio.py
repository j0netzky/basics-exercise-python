kadet = [["A", "8"], ["5", "7"], ["3", "10"]]
kopio = kadet[:]
kopio.append(["2", "9"])
print(kadet)
print(kopio)
kopio[0][0] = "3"
print(kadet)
print(kopio)
