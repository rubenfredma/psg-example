# Dar las felicitaciones a los estudiantes que aprobaron el curso
# de la siguiente tupla de estudiantes
# estudiantes = [('Juan', 51), ('Pedro', 80), ('Maria', 90), ('Ana', 40), ('Luis', 30)]

estudiantes = [('Juan', 51), ('Pedro', 80), ('Maria', 90), ('Ana', 40), ('Luis', 30)]

for i in estudiantes:
    if i[1] > 50:
        print(f"{i[0]}, felicitaciones por aprobar el curso ")
    
