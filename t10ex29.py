def bintodec(b):
    aux = b[::-1]
    d=0
    for i,e in enumerate(b):
        d+=int(e)*(2**i)
    return d

#programa principal
a = input("Introduexi un número en binari (només pot tenir 0's i 1's): ")
print("El número {}-binari és {}-decimal".format(a,bintodec(a)))