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

#Exercices Listes
#Ex1
print("Exercice: crée une liste de nombres pairs et une autre de nombres impairs")
l = [1, 2, 0, 5, 6, 6, 6, 7, 4, 9, 4, 2, 5, 3, 1, 23, 5, 4]
print(l)
pair = [x for x in l if (x % 2 == 0)]
impair = [x for x in l if (x % 2 == 1)]
print(pair, impair)

#Ex2
print("supprimer toutes les voyelles d’une liste de caractères")
lettres = ['a', 'b', 'c', 'd', 'e']
print(lettres)
nouv = [x for x in lettres if x not in ['o', 'u', 'i', 'e', 'y', 'a']]
print(nouv)

"""mois = ["Janvier", "Fevrier", "Mars"]
jours = [1, 20, 4]
date = []
for c in mois:
    for x in jours:
        date.append([c,x])
print(date)
"""
#Ex4
print("aplatir une liste et la rendre une liste à une seule dimension")
appf =[]
app =[]
L = [[1,2,3], [4,5,6], [7,8,9]]
print(L)
for c in L:
    app = [x for x in c if True]
    appf =appf + app
print(appf)


#Ex3
print("afficher tous les couples générés à partir de deux listes")
mois = ["Janvier", "Fevrier", "Mars","Avril"]
jours = [31, 28, 31, 30]
zipped = zip(mois, jours)
print (list(zipped))

#Ex4
print("transposer une matrice nxm")
M = [[1,2,3], [4,5,6], [7,8,9]]
for i in M:
    print(i)
T = []
for j in range(0,len(M[1])):
    T.append([])
    for i in M:
            T[j].append(i[j])
print("Transposée:")
for x in T:
    print(x)
