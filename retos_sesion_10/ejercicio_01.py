# 1.- Anita y Pepito llevan saliendo juntos por 4 semanas, cada vez 
# que salen van a comer a una plaza de comidas. 
# Ambos quieren saber que tan compatibles son viendo cuantos platos de 
# comida tienen en común. A continuación tienes los platos de comida 
# que ambos han ido pidiendo a los largo de sus citas:
#   Anita: Sushi, Pizza, Tacos, Hamburguesa, Pasta, Alitas
#   Pepito: Pizza, Tacos, Ensalada, Pasta, Helado, Milanesa
# Si la cantidad platos de comida que tienen en comunes mayor
#  a 50% entonces ambos seguirán saliendo

Anita = {'Sushi', 'Pizza', 'Tacos', 'Hamburguesa', 'Pasta', 'Alitas'}
Pepito = {'Pizza', 'Tacos', 'Ensalada', 'Pasta', 'Helado', 'Milanesa'}
print(Anita, Pepito)

total_platos = len(Anita)
interseccion = Anita.intersection(Pepito)
platos_comun = len(interseccion)
porcentaje_platos_comun = (platos_comun*100)/total_platos

print(f"La cantidad de platos en comun es del {porcentaje_platos_comun}%")
print("Ambos seguiran saliendo ?. ", (porcentaje_platos_comun>50))
