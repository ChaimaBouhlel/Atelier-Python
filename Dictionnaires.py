#Ex1
#échange les clés et les valeurs d'un dictionnaire
print("Ex1: échanger les clés et les valeurs d'un dictionnaire")
myKeys = []
myValues = []
dic = {"car":"voiture", "carpet":"tapis", "market":"marché", "Night":"nuit"}
dic2={}
for i in dic:
    dic2[dic[i]]=i
print(dic2)

#Ex2: une phrase entrée par l'utilisateur,
#sauvegarder dans un dictionnaire les différents mots de la phrase avec leurs nombres d'occurrence.
print("Ex2: sauvegarder dans un dictionnaire les différents mots de la phrase avec leurs nombres d'occurrence.")
phrase = input("Donner une phrase:")
phrase = str(phrase)
ls = phrase.split()
s = set(ls)
dic={}
for i in ls:
    ph = phrase
    dic[i] = 0
    x = ph.find(i)
    while (x!=-1):
        ph = ph[x + 1:]
        dic[i] += 1
        x = ph.find(i)
print(dic)

#EX3:entrer les informations relatives à un nombre d'étudiants (nom, prénom et note) et
# créer une structure qui à partir d'un nom et prénom donnés, permet de déterminer la note.
print("EX3")
n = input("Donner le nbre d'étudiants")
n = int(n)
dic = {}
for i in range(1,n+1):
    nom= input("nom")
    prenom = input("prenom")
    note = input("note")
    nom = str(nom)
    prenom = str(prenom)
    note = int (note)
    tup=(nom,prenom)
    dic[tup]=note
print("Donner les coordonnées pour determiner la note")
nom= input("nom")
prenom = input("prenom")
nom = str(nom)
prenom = str(prenom)
tup=(nom,prenom)
print("Votre note est:",dic[tup])