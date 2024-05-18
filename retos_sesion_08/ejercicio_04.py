# Las notas de un estudiante durante un semestre son: 
#  34, 61, 80, 20, 12, 69, 32, 60, 61, 51, 90, 23, 15
# Genera una tupla con los resultados y calcula el promedio para saber
# si aprobo o no el semestre, utiliza la funcion sum() y len()

notas = (34, 61, 80, 20, 12, 69, 32, 60, 61, 51, 90, 23, 15)
print(notas,type(notas)) 

suma = sum(notas)
n = len(notas)
media = suma/n

print("La nota tiene una media de:",media)
print("¿Aprobo el curso?", media >51)