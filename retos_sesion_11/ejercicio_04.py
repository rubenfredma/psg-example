# 4.- Gestión de hábitats en peligro: Crea un diccionario que asocie 
# especies animales en peligro de extinción con información sobre sus 
# hábitats amenazados, lo que permite priorizar la protección de áreas 
# críticas para la supervivencia de estas especies

habitats = {"polo norte" : {"especies": {"oso polar", "morsa", "ballena"}}, "amazonas" : {"especies": {"tigre", "mono", "guacamayo"}}}

# Añade al diccionario de habitats 2 habitats más usando update()
habitats.update({"altiplano":{"especies":{"quirquincho","chinchilla","vicuña"}}})
habitats.update({"amazonas":{"especies":{"delfin rosado","jaguar","manati"}}})
print(habitats)

# Existe en el diccionario de habitats el habitat 'amazonas'?
existe = 'amazonas' in habitats
print(f"El habitats amazonas existe en el diccionario ?: {existe}")

# Añade al diccionario de amazonas la especie 'anaconda'
habitats["amazonas"]["especies"].add("anaconda")
print(habitats)
