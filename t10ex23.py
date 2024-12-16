def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un número: ")
        if a!=".":
            l.append(int(a))
    return l
def crear_punts(l):
    s="."
    for e in l:
        print("{} \n".format(s*e))
        s="."

a = llegir_llista()
crear_punts(a)