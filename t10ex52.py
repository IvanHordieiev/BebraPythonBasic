def index_paraula(llista, paraula):
   inici, final = 0, len(llista) - 1
   while inici <= final:
       mig = (inici + final) // 2
       if llista[mig] == paraula:
           return mig
       elif llista[mig] < paraula:
           inici = mig + 1
       else:
           final = mig - 1
   return -1


llista_ordenada = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
paraula_a_cercar = "e"
resultat = index_paraula(llista_ordenada, paraula_a_cercar)
print(f"L'índex de la paraula '{paraula_a_cercar}' és: {resultat}")


paraula_a_cercar = "z"
resultat = index_paraula(llista_ordenada, paraula_a_cercar)
print(f"L'índex de la paraula '{paraula_a_cercar}' és: {resultat}")