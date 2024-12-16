def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un número: ")
        if a!=".":
            l.append(int(a))
    return l

def esta_ordenada(l):
    ld=l.sort(reverse=True)
    la=l.sort(reverse=False)
    if l.sort(reverse=True)==ld:
        print("La llista està ordenada de forma descendent")
    elif l.sort(reverse=False)==la:
        print("La llista està ordenada de forma ascendent")
    else:
        print("La llista no està ordenada")


#Programa principal
l=llegir_llista()
esta_ordenada(l)