import collections
from math import *

"""
print("bonjour", end=" ")
print("chaima")
x = 20.555
name = "max"
print("{} a {:.2f} ans".format(name, x))
print("la valeur de pi est {:*<10.2f}".format(pi))
pourcentage=((4500+2575)/14800)*100
print("le pourcentage est {:<10.0f} %".format(pourcentage))
print("le pourcentage est {:<10.1f} %".format(pourcentage))
print("le pourcentage est {:<10.2f} %".format(pourcentage))
print("le pourcentage est {:<10.3f} %".format(pourcentage))
"""
# saisie
"""
n=input("donner le nombre ")
n=float(n)
print("{:.0f} {:.0f} {:.0f}".format(n,n**2,n**3))
"""

# exercice if
"""
a=input("donner a:")
a=int(a)
b=input("donner b:")
b=int(b)
oper=input("donner l'operateur")
if (oper=="+"):
    print("a + b = ",a+b)
elif (oper=="-"):
    print("a - b = ",a-b)
elif (oper=="*"):
    print("a * b = ",a*b)
elif(oper=="/"):
    if (b==0):
        print("division sur 0 impossible")
    else:
        print("a / b = ",a/b)
"""
# exercice while
"""
i=0
while i<6 :
    i += 1
    if (i==3) :
        continue
    print(i)
"""

# exercices
"""

mot=input("saisir un mot")
nb=0
for i in mot:
    if i=="o" or i=="u" or i=="i" or i=="e" or i=="y" or i=="a":
        nb+=1
print("le nombre de voyelles est ",nb)
"""
"""
somme=0
for i in range(1,11):
    c=input("donner entier")
    c=int(c)
    if (c<0):
        print("entier negatif")
        break
    else:
        somme+=c
else :
    print("La somme de ces 10 entiers: ",somme)
"""

# les listes
"""
liste = list(range(0, 11, 2))
print(liste)
print(liste[len(liste) - 1])
print(liste[0:3: 1])
l = liste.copy()
print(l)
l = [1, 2, 3, 4, 5, 6]
print(len(l))
del(l[2])
print(len(l))
print(l)
liste.clear()
print(liste)
l.insert(2,3)
l2 = [7, 8, 9]
print(l+l2)
print(l[-2])
print(l[-2:])
print(l[2:])
print(l[2:4])
"""
"""
l1 = [1, 2, 3, 4, 5, 6]
l2 = [7, 8, 9]
print(l1.extend(l2))
print(l1)
l1.reverse()
print(l1)
"""
"""
L = ["sami", 1, 9.5, False]
L.sort(key=str)
print(L)

print(L.index("sami",0,4))
"""
"""
L=[[1, 2], [3, 4]]
print(L[0][1])

l=[1,2,0,5,6,6,6,7,4,9,4,2,5,3,1,23,5,4]
a=[x for x in l if x>5]
print(a)
"""

"""
l = ['a', 'b']
print(type(l))
l.append('c')
print(l)
m=['A', 'B','C']
print(l+m)
m=l
print(l,m)
l.append('d')
m=l.copy()
l.append('e')
print(l,m)
"""
"""

l = [1, 2, 0, 5, 6, 6, 6, 7, 4, 9, 4, 2, 5, 3, 1, 23, 5, 4]
pair = [x for x in l if (x % 2 == 0)]
impair = [x for x in l if (x % 2 == 1)]
print(pair, impair)
"""

"""
lettres = ['a', 'b', 'c', 'd', 'e']
nouv = [x for x in lettres if x not in ['o', 'u', 'i', 'e', 'y', 'a']]
print(nouv)
"""
"""
mois = ["Janvier", "Fevrier", "Mars"]
jours = [1, 20, 4]
date = []
for c in mois:
    for x in jours:
        date.append([c,x])
print(date)
appf =[]
app =[]
L = [[1,2,3], [4,5,6], [7,8,9]]
for c in L:
    app = [x for x in c if True]
    appf =appf + app
print(appf)
"""
"""
mois = ["Janvier", "Fevrier", "Mars"]
jours = [31, 28, 31]
zipped = zip(mois, jours)
print (list(zipped))
"""
"""
M= [[1,2,3], [4,5,6], [7,8,9]]
for i in M:
    print(i)

T = []
for j in range(0,len(M[1])):
    T.append([])
    for i in M:
            T[j].append(i[j])


for x in T:
    print(x)
"""

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

#verifier si une chaine est palindrome
"""
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

#Les ensembles
"""
set1 = {'Mahdi', 'Raslen', 'Basboussa'}
set2 = {1, 2, 3, 4}
set3 = {2, 5, 7}
print(set3 | set2)
print(set3 & set2)
print(set3 - set2)
print(set3 ^ set2)
"""
"""
s1 = { 1, 2, 3}
s2 = { 1, 2, 3, 5, 6}
print(s1<s2)
print(s1.issubset(s2))
print(s2.issuperset(s1))
"""
"""stopwords = {"et", "le", "pour", "la", "de", "un", "ou", "des", "en"}
texte = input("donner chaine \n")
texte = str(texte)
print(texte)
conv = texte.split()
print(conv)
s1 = set(conv)
print(s1)
print(s1-stopwords)"""

#les dictionnaires


"""dic = {"key1":"oui"}
print("key1" in dic)
for i in dic:
    print (dic[i])
for i in dic.values():
    print(i)"""
"""
dic = {"prenom":"mahdi", 'age':20}
dic["nom"]="Chaari"
print(dic)
print(dic.values())
print(dic.keys())
"""

"""

"""
"""dic = {"prenom":"mahdi", 'age':20}
dic["nom"]="Chaari"
dic["a"]="b"
dic["c"]="b"

print(dic)
od = collections.OrderedDict(sorted(dic.items(), key=str))
print(od)"""

