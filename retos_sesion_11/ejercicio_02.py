# 2.- Crea un diccionario para almacenar información de comidas de animales
#  por ejemplo:

comidas = {"carne" : {"animales": ["león", "tigre"]}, "frutas" : {"animales": ["mono", "elefante"]}}
print(comidas)

# Añade al diccionario de comidas 4 alimentos más usando update(clave=valor)

comidas.update({'plantas':{"animales":["oveja", "vaca"]}})
comidas.update({'insectos':{"animales":["oso hormiguero", "murcielago"]}})
comidas.update({'semillas':{"animales":["ardilla", "loro","canario","gallina"]}})
comidas.update({'peces':{"animales":["delfin", "pelicano","gaviota"]}})
print(comidas)

# Existe en el diccionario de comidas la comida 'carne'?
print(f"La comida carne existe en el diccionario ?: {'carne' in comidas}")

# Elimina la comida 'frutas' del diccionario de comidas
del comidas['frutas']
print(comidas)
