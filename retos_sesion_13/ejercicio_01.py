# Imprimir los 20 primeros números de la serie de Fibonacci
#   0, 1, 1, 2, 3, 5, 8,.....

i = 0
j = 1
print(i, end=", ")
print(j, end=", ")
for c in range(1,19):
    aux = i+j
    print(aux, end=", ")
    i = j
    j = aux
    



