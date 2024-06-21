# Un estudiante desea saber cuál es su promedio de calificaciones en la
# materia de matemáticas, cree una función que reciba las calificaciones
# como lista y devuelva el promedio las calificaciones son 20,40,60,51,13

def media_notas(lista):
    media = sum(lista) / len(lista)
    return media

notas = [20,40,60,51,13]
promedio = media_notas(notas)
print(f"Promedio de calificaciones = {promedio}")