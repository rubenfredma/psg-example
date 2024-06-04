# 3.- Crea un diccionario con las siguientes tuplas de animales

tupla = (('perro', '🐶') , ('gato','🐱') , ('aves',['🐦','🦅']))
print(tupla)
diccionario = dict(tupla)
print(diccionario)

# Del diccionario obtén y elimina el valor de la clave 'aves'
aves = diccionario.pop('aves')
print(aves, type(aves))
print(diccionario)

# Modifica el valor de la clave 'gato' por '🐈'
diccionario['gato']='🐈'
print(diccionario)

# Cambia la clave perro por perros y su valor por ['🐶','🐕']
mi_lista = [diccionario['perro']]
mi_lista.append('🐕')
diccionario['perros'] = mi_lista
del diccionario['perro']
print(diccionario)