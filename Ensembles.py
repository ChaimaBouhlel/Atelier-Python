stopwords = {"et", "le", "pour", "la", "de", "un", "ou", "des", "en"}
texte = input("donner chaine \n")
texte = str(texte)
conv = texte.split()
s1 = set(conv)
print("Les mots de la phrase qui ne sont pas des mots vides:")
print(s1-stopwords)