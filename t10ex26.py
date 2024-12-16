def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix una paraula: ")
        if a!=".":
            l.append(a)
    return l
def paraula_de_cada_longitud(l):
    a = []
    c = []
    for e in l:
        a.append(len(e))
    b = set(a)
    for e in b:
        y = len(list(filter(lambda x:x==e,a)))
        c.append([e,y])
    return c

#Programa principal
a = llegir_llista()
print("La paraula més llarga de la llista {} és {}".format(a,paraula_de_cada_longitud(a)))

"""
Definir una funció paraula_mes_llarga() que donada una llista de paraules, 
retorni la que té més caràcters. 
Ex: paraula_mes_llarga([“Hola”, “Ramis”, “IES”, “Paraula”]), ens retorni Paraula.

def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix una paraula: ")
        if a!=".":
            l.append(a)
    return l
def paraula_mes_llarga(l):
    a = l[0]
    for e in l:
        if len(e) > len(a):
            a = e
    return a

#Programa principal
a = llegir_llista()
print("La paraula més llarga de la llista {} és {}".format(a,paraula_mes_llarga(a)))
"""