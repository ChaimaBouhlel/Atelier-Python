noms = ["Rasslen", "Mahdi", "Chaima", "Ahmed"]
prenoms = [ "Ansi", "Chaari", "Bouhlel", "Cherif"]
ages = [20, 20, 21, 21]
zipped = zip(noms, prenoms, ages)
lzip = list (zipped)
for x in lzip:
    print("le nom est:", str(x[0]).capitalize(), "le prenom est:", str(x[1]). capitalize(), "l'age est: ", x[2])
