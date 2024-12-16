def menu():
   op=0
   while op<1 and op>5:
       print("Menu calculadora")
       print("1. Suma enters" )
       print("2. Sumar")
       print("Restar")
       print("Dividir)")
       print("Multiplicar")
       print("Sortir")
       op = int(input("Introdueixi una poció"))
       return op
def sumar ():
   a = int(input("introdueixi el primer element: "))
   b = int(input("introdueixi el segon element"))
   c = a + b
   print("El resultat de sumar {} més {} és {}".format(a, b, c))
def restar ():
   a = int(input("Introdueixi el primer element"))
   b = int(input("Introdueixi el segon elemet"))
   c = a - b
   print("el resultat de restar {} més {} és {}".format(a, b, c,))
def multiplicar():
   a = int(input("Introdueixi el primer element"))
   b = int(input("Introdueixi el segon element"))
   c = a * b
   print("El resultat de multiplicar {} més {} és {}".format(a, b, c))
def dividir():
   a = int(input("Introdueixi el primer element"))
   b = int(input("Introdueixi el segon element"))
   c = a / b
   print("El resultat de dividir {} més {} és".format(a, b, c))
a = True
while a:
   op = menu()
   match op:
       case 1:
           sumar()
       case 2:
           restar()
       case 3:
           multiplicar()
       case 4:
           dividir()
       case 5:
           a = False
           print("Adéu, gracies per haver utilitzar el programa! \n")