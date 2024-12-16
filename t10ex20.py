
def invertir(s):
    return s[::-1]

def es_palindrom(s):
    if s == invertir(s):
        return True
    else:
        return False
    
s = input("Introdueixi una cadena: ")
a = invertir(s)
if es_palindrom(s):
    print("La frase/paraula {} és igual a {} i, per tant, és palíndrom".format(s, a))
else:
    print("La frase/paraula {} no és igual a {} i, per tant, no és palindrom".format(s, a))