def es_de_traspas(any):
   if (any % 4 == 0 and any % 100 != 0) or (any % 400 == 0):
       return True
   else:
       return False


anys = [2000, 2001, 2004, 1900, 2020, 2100, 2400]
for any in anys:
   if es_de_traspas(any):
       print(f"L'any {any} és de traspàs.")
   else:
       print(f"L'any {any} no és de traspàs.")


