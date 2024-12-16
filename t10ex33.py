"""
Ara modificarem l'exercici i el que farem és comparar els caràcters centrals entre ells
"""
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
def retorna_conjunt(l):
    # Prec: Donada un llista de paraules
    # Post: Retorna un conjunt de caràcters el centre (si senar, centres si parell) de cada paraula
    m=[]
    for e in l:
        senar = len(e)%2==1
        if senar:
            m.append(e[len(e)//2])
        else:
            m.append(e[len(e)//2])
            m.append(e[len(e)//2+1])
    s=set(m)
    return s

def llistes_comparades(l,s):
    # Prec: Donada una llista de paraules i un conjunt de lletres centrals
    # Post: Mostraré llistes de paraules que tenen els elements centrals iguals
    for e in s:
        laux=[]
        for x in l:
            senar = len(x)%2==1
            if senar:
                if x[len(x)//2] == e:
                    laux.append(x)
            else:
                if x[len(x)//2] == e or x[len(x)//2+1] == e:
                    laux.append(x)
        print("Totes les paraules de la llista {} que tenen el centre {} igual són: {}".format(l,e,laux))


#Programa principal
l = llegir_llista()
s = retorna_conjunt(l)
llistes_comparades(l,s)


"""
Definir una funció nums_que_comencen_per() que donat una llista de noms, 
ens digui quants comencen per la lletra a.

Aquesta variant mira els caràcters centrals si són iguals que el donat (si és parell mira els dos del centre)


def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un nom: ")
        if a!=".":
            l.append(a)
    return l

def noms_que_comencen_per(l,c):
    m=[]
    for e in l:
        senar = len(e)%2==1
        if senar:
            aux= len(e)//2
            if e[aux]==c.upper() or e[aux]==c.lower():
                m.append(e)
        else:
            aux = len(e)//2 -1
            if e[aux]==c.upper() or e[aux]==c.lower() or e[aux+1]==c.upper() or e[aux+1]==c.lower():
                m.append(e)
    print("Els elements de la llista {} que comencen per {} són: {}".format(l,c,m))


#Programa principal
l = llegir_llista()
c = input("Introdueix un caràcter: ")
noms_que_comencen_per(l,c)
"""