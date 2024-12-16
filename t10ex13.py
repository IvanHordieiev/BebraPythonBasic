def menu():
   op = 0
   while op < 1 or op > 6:
       print("Menu calculadora")
       print("1. Suma enters")
       print("2. Restar")
       print("3. Dividir")
       print("4. Multiplicar")
       print("5. Canviar base")
       print("6. Sortir")
       op = int(input("Introdueixi una opció: "))
   return op


def sumar():
   a = int(input("Introdueixi el primer element: "))
   b = int(input("Introdueixi el segon element: "))
   c = a + b
   print(f"El resultat de sumar {a} més {b} és {c}")


def restar():
   a = int(input("Introdueixi el primer element: "))
   b = int(input("Introdueixi el segon element: "))
   c = a - b
   print(f"El resultat de restar {a} més {b} és {c}")


def dividir():
   a = int(input("Introdueixi el primer element: "))
   b = int(input("Introdueixi el segon element: "))
   if b != 0:
       c = a / b
       print(f"El resultat de dividir {a} més {b} és {c}")
   else:
       print("No es pot dividir per zero")


def multiplicar():
   a = int(input("Introdueixi el primer element: "))
   b = int(input("Introdueixi el segon element: "))
   c = a * b
   print(f"El resultat de multiplicar {a} més {b} és {c}")


def canviar_base():
   num = int(input("Introdueixi el número en base decimal: "))
   print(f"Base binària: {bin(num)[2:]}")
   print(f"Base octal: {oct(num)[2:]}")
   print(f"Base hexadecimal: {hex(num)[2:]}")


a = True
while a:
   op = menu()
   match op:
       case 1:
           sumar()
       case 2:
           restar()
       case 3:
           dividir()
       case 4:
           multiplicar()
       case 5:
           canviar_base()
       case 6:
           a = False
           print("Adéu, gracies per haver utilitzar el programa! \n")