elukoita = ["mursu", "apina", "aasi", "laama", "koala", "aropupu", "hirvi"]

for elain in elukoita:
    if elain.startswith("a"):
        elukoita.remove(elain)
print(", ".join(elukoita))
