def esvocal(x):
    return x.lower() in "aeiou"
a = "a"
while(a!="."):
    a = input("Escriu la vocal")
    if esvocal(a):
        print("La lletra introduïda {} és vocal".format(a))
    else:
        print("La lletra introduïda {} no és una vocal".format(a))