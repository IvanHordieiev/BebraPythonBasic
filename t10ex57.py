def elements_parells(llista):
   parells = []
   for i in range(0, len(llista), 2):
       parells.append(llista[i])
   return parells


llista_prova = ["saad", "taula", "silla", "ordenador", "mesa", "raton"]
resultat = elements_parells(llista_prova)
print("Els elements en posicions parells són:", resultat)