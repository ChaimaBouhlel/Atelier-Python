"""#ecriture de la fonction
def externe(a):
    #fonction imbriquée
    def interne(b):
        return 2 * b
    #On est dans externe ici
    return 3 * interne(a)


#appel
x = 10
print( externe(x))
#print(interne(x)) #provoque une erreur: Une fonction imbriquée n'est pas visible à l'exterieur

"""
import collections

"""def f():
    x=2
    def f1():
        nonlocal x
        x=x+1
    f1()
    print(x)
f()
"""
"""#Ex1:
def parler_enthousiasme(message, nbre = 1, bool=False):
    if (bool):
        print(message.upper()+nbre*"!")
    else:
        print(message+"!"*nbre)
parler_enthousiasme("hello", 3)"""

"""#Ex2
def affiche_employee(nom, sal=3000):
    print("Le nom est:", nom)
    print("Le salaire est:", sal)
affiche_employee("Mohamed")"""

"""#EX3
def Ouvrage(titre, *aut, **infos):
    print("Titre du livre:",titre)
    print("Auteurs:")
    for i in aut:
        print(i)
    for i in infos:
        print(i+":",infos[i])
Ouvrage("L'etranger","Albert Camus",nbrePages=230)"""

"""def somme(*a):
    s=0
    for el in a:
        s+=el
    return s
print(somme(1))
print(somme(20,20))
print(somme(10,20,3))
"""
#print(list(map(lambda x:x%2==0,[7,8,6,9])))


#EX4
def trier(ls):
    ls.sort(key=lambda x: x["note"], reverse=False)
    print(ls)
trier([{"nom":"Sam", "note":18},{"nom":"Joey", "note":13},{"nom":"Marco", "note":15}])


"""
def f():
    yield "un"
    yield "deux"
    yield "trois"
for i in f():
    print(i)"""

