def sumar_nums(inici, final):
   suma = 0
   for i in range(inici, final + 1):
       suma += i
   return suma


if __name__ == "__main__":
   inici = int(input("Introdueix el primer número: "))
   final = int(input("Introdueix el segon número: "))
  
   resultat = sumar_nums(inici, final)
   print(f"La suma de tots els números entre {inici} i {final}, ambdós inclosos, és: {resultat}")