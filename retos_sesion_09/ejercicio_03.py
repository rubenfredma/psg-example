# Crear una lista de personas con 10 nombres de personas
personas = ["Ana","Mario","Vania","Isabel","Ivan","Jhon","Veronica","Maria","Lola","Juan"]
print(personas, type(personas))

# Obtener una sub lista de 2 a 7
grupo = personas[2:7]
print(grupo)

#   Buscar si existe el nombre "Jhon" en la lista original
print("Jhon esta en la lista original ?:","Jhon" in personas)

#   Ordenar la sub lista alfabéticamente
grupo.sort()
print(grupo)

#   Ordenar la lista original alfabéticamente de forma descendente
personas.sort(reverse=True)
print (personas)