def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix una paraula: ")
        if a!=".":
            l.append(a)
    return l

def filtrar_paraules(l,n):
    return list(filter(lambda x:len(x)>n,l))

x = llegir_llista()
y = int(input("Introdueixi un número: "))
print("De la llista {} que tinguin més de {}-caràcters hi ha {}".format(x,y,filtrar_paraules(x,y)))