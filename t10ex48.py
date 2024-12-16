def hi_ha_duplicats(llista):
   elements_vistos = set()
   for element in llista:
       if element in elements_vistos:
           return True
       elements_vistos.add(element)
   return False


llista_prova1 = [1, 2, 3, 4, 5]
llista_prova2 = [1, 2, 3, 2, 5]
llista_prova3 = ["a", "b", "c", "d", "e"]
llista_prova4 = ["a", "b", "c", "a", "e"]


print(hi_ha_duplicats(llista_prova1))  
print(hi_ha_duplicats(llista_prova2))  
print(hi_ha_duplicats(llista_prova3))  
print(hi_ha_duplicats(llista_prova4))  


