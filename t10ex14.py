def gran(num1, num2):
   if num1 > num2:
       return num1
   elif num2 > num1:
       return num2
   else:
       return "Els dos números són iguals"



print(gran(10, 20))  
print(gran(50, 30)) 
print(gran(5, 5))    
print(gran(-10, 0))  
print(gran(3, -5))   