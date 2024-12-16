def verificar_edad(edad):
   if edad > 18:
       return "Es mayor de edad."
   elif edad < 18:
       return "No es mayor de edad."
   else:
       return "Tiene exactamente 18 años."


def prueba_verificar_edad():
   edades = [16, 18, 21] 
   for edad in edades:
       resultado = verificar_edad(edad)
       print(f"Edad: {edad} - Resultado: {resultado}")


prueba_verificar_edad()