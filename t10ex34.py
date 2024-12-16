"""
Definir una funció comptar_vocals() que donada una paraula, 
compti el número de vegades que apareix cada vocal. Ex: comptar_vocals(“Ratapinyada”) 
retorni1 HI ha 4 a’s, 0 e’s, 1 i’s, 0 o’s i 0 u’s.

"""
def comptar_vocals(p):
    ap = [0,0,0,0,0]
    for e in p:
        if e == "a" or e=="A":
            ap[0]+=1
        elif e=="e" or e=="E":
            ap[1]+=1
        elif e=="i" or e=="I":
            ap[2]+=1
        elif e=="o" or e=="O":
            ap[3]+=1
        elif e=="u" or e=="U":
            ap[4]+=1
        else:
            print("{} no és una vocal".format(e))
    print("La vocal a apareix {}-vegades \n la vocal e apareix {}-vegades \n la vocal i apareix {}-vegades \n la vocal o apareix {}-vegades \n la vocal u apareix {}-vegades".format(ap[0], ap[1], ap[2], ap[3], ap[4]))

x = input("Intro paraula: ")
comptar_vocals(x)
