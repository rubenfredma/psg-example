# 5.- Eres NOE y tienes que guardar dos animales de cada especie en un 
# arca, crea un diccionario con las especies

arca = {"perro" : 2, "gato" : 2, "tigre" : 2, "mono" : 2, "unicornio" : 0, "jirafa" : 1}
print(arca)

# Añade al arca 2 especies más usando update()
arca.update({'oso':2})
arca.update({'llama':2})
print(arca)

# Toma lista de los animales en el arca iterando el diccionario
iterador = iter(arca.items())
print("------  Listado de animales del arca---------")
siguiente = next(iterador)
print(siguiente[0])
siguiente = next(iterador)
print(siguiente[0])
siguiente = next(iterador)
print(siguiente[0])
siguiente = next(iterador)
print(siguiente[0])
siguiente = next(iterador)
print(siguiente[0])
siguiente = next(iterador)
print(siguiente[0])
siguiente = next(iterador)
print(siguiente[0])
siguiente = next(iterador)
print(siguiente[0])

print()
# Existe en el arca la especie 'dragon'?
print(f"Existe en el arca la especie 'dragon'?: {'dragon' in arca}")

# Elimina la especie 'unicornio' del arca
arca.pop('unicornio')
print(arca)

# Modifica el valor de la especie 'jirafa' por 2
arca.update(jirafa=2)
print(arca)

# Vacía el arca después del diluvio
arca.clear()
print(arca)
