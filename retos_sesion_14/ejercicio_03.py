# Crear una función recursiva para obtener el N número de la serie de Fibonacci
#     0, 1, 1, 2, 3, 5, 8

def fibonacci(numero):
    if numero == 0 or numero == 1:
        return numero
    else:
        return fibonacci(numero-1) + fibonacci(numero-2)
         
resultado = fibonacci(6)
print (resultado)

