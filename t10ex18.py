def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un número: ")
        if a!=".":
            l.append(int(a))
    return l

def sumar_llista(l):
    suma=0
    for e in l:
        suma += e
    return suma

def multiplicar_llista(l):
    multiplicacio=1
    if 0 in l or len(l)==0:
        return 0
    else:
        for e in l:
            multiplicacio *= e
    return multiplicacio

l=llegir_llista()
print("La suma dels elements de la llista {} és {}".format(l,sumar_llista(l)))
print("La multiplicació dels elements de la llista {} és {}".format(l,multiplicar_llista(l)))