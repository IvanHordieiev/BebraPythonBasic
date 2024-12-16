def elimina_duplicats(llista):
   return list(set(llista))


llista_prova = [1, 2, 2, 3, 4, 4, 4, 5, 6, 1, 7, 8, 9, 9, 10]
llista_sense_duplicats = elimina_duplicats(llista_prova)
print("Llista original:", llista_prova)
print("Llista sense duplicats:", llista_sense_duplicats)