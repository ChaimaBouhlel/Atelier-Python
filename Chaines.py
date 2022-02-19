#les chaines:
"""
chaine = "Chaima"
print(chaine.isalnum())
print(chaine.isdigit())
"""

"""
ch="abcdaefga"
print("Derniere position",ch.rfind("a"))
print("Premiere position",ch.find("a"))
print("Nbre d'occurences",ch.count("a"))
"""
""""
texte = "Ceci est un Texte. Merci"
print(texte.title())
print(texte.upper())
print(texte.lower())
print(texte.capitalize())
print(texte.swapcase())
print(texte.replace(texte,"X"))
print(texte)
"""
"""

texte = "      Ceci est un Texte. Merci       "

print(texte.lstrip(),"cc")
print(texte.rstrip())
print(texte.strip())
"""

"""
texte = "Ceci est un Texte. Merci"
textSplit = texte.split(" ")
print(textSplit)
espace=" "
textJoin =espace.join(textSplit)
print(textJoin)
"""

"""
#comment modifier des caracteres dans une chaine
texte = "Ceci est un Texte. Merci"
caracteres = list(texte)
caracteres[8] = "A"
caracteres[9] = "B"
texte = "".join(caracteres)
print(texte)
"""

#EX1: verifier si une chaine est palindrome
print("EX1: verifier si une chaine est palindrome")
texte = input("donner chaine \n")
texte = str(texte)

carac=list(texte)
carac2=list(texte)
carac.reverse()
if (carac2==carac):
    print("oui")
else:
    print("non")

"""
#Methode 2
origine = texte
for i in range(0,int(len(texte)/2),1):
    x= texte[len(texte)-i-1]
    carac=list(texte)
    carac[len(texte)-i-1]=carac[i]
    carac[i]=x
if (origine==texte):
    print("oui")
else:
    print("non")
"""
#EX2: afficher les positions d’une sous-chaine dans une autre chaine
print("afficher les positions d’une sous-chaine dans une autre chaine")
pos = []
chaine = input("donner chaine \n")
chaine = str (chaine)
sschaine = input("donner sousschaine \n")
sschaine = str (sschaine)
y=0
x = chaine.find(sschaine)
while (x!=-1):
    pos.append(x+y)
    chaine = chaine[x+1:]
    y = y + x + 1
    x = chaine.find(sschaine)
print(pos)

#EX3: lire une phrase et d'afficher ses différents mots ainsi que leurs longueurs respectifs
print(" lire une phrase et d'afficher ses différents mots ainsi que leurs longueurs respectifs")
ph = input("donner phrase\n")
ph = str (ph)
ls = ph.split()
new = [len(c) for c in ls]
for i in range(0,len(ls)):
    print(ls[i], new[i])