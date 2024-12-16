def num_majuscules(s):
    num=0
    j=[]
    for e in s:
        #if e in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if e.isupper():
            num += 1
            j.append(e)
    return num,"".join(j)

#Programa principal
a = input("Introduexi una paraula amb Majúscules i minúscules: ")
x,y=num_majuscules(a)
print("El número de majúscules que té la paraula {} és de {} i són {}".format(a,x,y))