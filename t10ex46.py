def llegir_llista():
    # Prec: llista buida i llegeix del teclat paraules
    # Post: Retorna la llista llegida de paraules, la llista acaba en trobar un punt
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un nom: ")
        if a!=".":
            l.append(a)
    return l


def retorna_nova_llista(l):
    return l[1:-1]

#Programa principal
l=llegir_llista()
s=retorna_nova_llista(l)
print("{} es transforma en {}".format(l,s))