# range(10,0,-1)  # 10 9 8 7 6 5 4 3 2 1

# # se puede convertir un a rango en una lista
# list(range(5))

# print(list(range(1,10,2)))

# # MALA PRACTICA, uso de variables fuera del ciclo, puede funcionar
# for i in range(5):
#     print(i)
# print(i)

# # estructura de un For
# print ("Inicio")
# for i in range(5): # rango (0,5,1)
#     print(i)
# print ("Fin")

# # Ej. sumar los numeros del 1 al 10 de 2 en 2
# print ("Ejemplo 1")
# suma = 0
# for i in range(1, 11, 2): # 1, 3, 5, 7, 9
#     #print(i)
#     print(suma)
#     suma = suma + i   #suma += i
# print(suma)

# print ("Ejemplo 2")
# for i in range(0, 6):
#     print(" "*(5-i) + "*"*i*2+"*")

# # Ej.3 crear una serie de nros cuadrados del 1 al 10
# print ("Ejemplo 3")
# for i in range(1, 11):
#     print(i**2, end="_")

# # Crear una lista de nros pares del 1 al 10
# print ("Ejemplo 4")
# pares = []
# for i in range(0, 11, 2):
#     pares.append(i)
# print(pares)
# print(type(pares))

# #EJERCICIO-1 Imprimir los 10 primeros de la serie numeros cubicos
# print("Serie cubicos")
# for i in range(1,11):
#     print(i**3, end=" ")

# for fruta in ['🍎','🍌','🍇','🍉']:
#     print(fruta)

# # Ej5 imprimir los elementos de una lista fiestas
# print ("Ejemplo 5")
# fiesta = ['🎄','🎆','🎁','🎊','✨','🎭']
# for objeto in fiesta:
#     print(objeto)

# # Ejemplo 6, imprimir los elementos de una tupla de frutas separados por coma
# print ("Ejemplo 6")
# frutas =  ('🍅','🍇','🍈','🍉','🍏')
# for fruta in frutas:
#     print(fruta, end=", ")

# # Ejemplo 7, imprimir los elementos de un diccionario
# print ("Ejemplo 7")
# frutas = {'🍅':'Tomate','🍇':'Uva','🍈':'Melón','🍉':'Sandía','🍊':'Naranja'}
# # al iterar devuelve la clave del diccionario
# for clave in frutas:
#     print(clave, frutas[clave])

# # Ejemplo 8, imprimir los elementos del ciclo de vida de un pollo con flechas
# print ("Ejemplo 8")
# ciclo_vida = '🍙🐣🐥🐤🐔🍗'
# for etapa in ciclo_vida:
#     print(etapa, end="->")

# # Recorrer elementos
# #   Mediante in como pertenencia
# #   Mediante len() y range()
# #   Mediante enumerate()
# # Ejemplo 9, Listar los elementos de la siguiente serie ['🐶','🐱','🐰','🐭']

# print ("Ejemplo 9")
# animales = ['🐶','🐱','🐰','🐭']
# for animal in animales:
#     print(animal)

# # Mediante len() y range()
# # Ejemplo 10, Listar los elementos de la siguiente serie ['🐶','🐱','🐰','🐭']
# print ("Ejemplo 10")
# animales = ['🐶','🐱','🐰','🐭']
# # creando un rango con la longitud de la lista
# for i in range(len(animales)):
#     print(animales[i])

# # Ejemplo 11, Listar los elementos de la siguiente serie ['🐶','🐱','🐰','🐭']
# print ("Ejemplo 11")
# animales = ['🐶','🐱','🐰','🐭']
# for i, animal in enumerate(animales):
#     print(i, animal, animales[i])

# # Ejercicio 2, imprimir la cantidad de veces los elementos
# # de la cadena '⚽🏈⚾🎱' de acuerdo a su posición más 1
# balones = '⚽🏈⚾🎱'
# for i, pelota in enumerate(balones):
#     print(i, pelota*(i+1))

# ###  ciclo  while
# print ("Ejemplo 12")
# i = 0
# while i <= 5:
#     print(i)
#     i += 1

# # Ejemplo 13, sumar los números mientras no se ingrese por teclado el número 0
# print ("Ejemplo 13")
# suma = 0
# numero = int(input("Ingrese un número: "))
# while numero != 0:
#     suma += numero
#     numero = int(input("Ingrese un número: "))
# print(suma)

# # Ejercicio 3, Ingresa un número por teclado y genera un contador hasta 0,
# # si el número es negativo no hace nada
# numero = int(input("Ingrese un número: "))
# while numero >= 0:
#     print(numero)
#     numero-=1
# print("Terminado")

# # Ejemplo 14, De la siguiente lista de frutas imprimir los elementos
# # hasta que se encuentre un gusano 🐛 con for
# frutas = ['🍎','🍌','🍇','🍉','🍊','🐛','🍋','🍍']
# print ("Ejemplo 14")
# for fruta in frutas:
#     if fruta == '🐛':
#         break
#     print(fruta)
# print ("Fin")

# # con while
# frutas = ['🍎','🍌','🍇','🍉','🍊','🐛','🍋','🍍']
# print ("Ejemplo 14 con WHILE ........")
# cont = 0
# while(frutas[cont] != '🐛'):
#     print(frutas[cont])
#     cont+=1
# print ("Fin")

# # termina mostrando al gusano
# frutas = ['🍎','🍌','🍇','🍉','🍊','🐛','🍋','🍍']
# print ("Ejemplo 14")
# i = ""
# while i != '🐛':
#     i = frutas.pop(0)  # saca a la var i, tambien lo elimina de la lista
#     print(i)
# print ("Fin")

# # corte de ciclos infinitos
# num = int(input("Ingrese un numero: "))
# while num != 0:
#     print(num)
#     num -= 1     # para salir  ctrl + C
#     # condicion de salida
#     if num == -1000:
#       break;

# # Ejemplo 16, Crear un ciclo infinito que pida una cadena de texto
# # la ponga en mayúsculas y la imprima hasta que se ingrese la palabra salir
# print("Ejemplo 16")
# while True:
#     texto = input("Ingrese un texto: ")
#     if texto == 'salir':
#         break
#     print(texto.upper())
# print ("Fin")

# # Ejercicio 4, Crear un ciclo infinito que reciba un número por teclado
# # y verifique si es par o impar hasta que se ingrese el número 0
# while True:
#     nro = int(input("Ingrese un numero: "))
#     if nro == 0:
#         break
#     else:
#         if nro%2 == 0:
#             print(f"{nro} es par")
#         else:
#             print(f"{nro} es impar")
# print ("Fin")

# print ("Ejercicio 4")
# while True:
#     numero = int(input("Ingrese un número: "))
#     if numero == 0:
#         break
#     print ("Par" if numero % 2 == 0 else "Impar")

# ### Estructuras por comprension
# # Ejemplo 17, Crear una lista de los números pares del 2 al 10
# print ("Ejemplo 17")
# pares = [i for i in range(2, 11, 2)]
# print(pares)

# # creando un conjunto
# pares = {i for i in range(2, 11, 2)}
# print(pares)
# print(type(pares))

# # Ejemplo 18, Crear una lista de los números pares del 2 al 10 con condicional
# print ("Ejemplo 18")
# pares = [i for i in range(2, 11) if i % 2 == 0]
# print(pares)

# # lista de impares
# impares = [i for i in range(2, 11) if i % 2 == 1]
# print(impares)

# # Ejemplo 19, Crear un diccionario números 2 al 10
# # donde si es par vale "Par" y si es impar valga "Impar"
# print ("Ejemplo 19")
# pares = {i: "Par" if i % 2 == 0 else "Impar" for i in range(2, 11)}
# print(pares)

# # Ejercicio 5, Crear una tupla de los números impares del 1 al 10
# # usando una tupla por comprensión
# impares = tuple(i for i in range(1,11,2))
# print(impares)

# print ("Ejercicio 5")
# impares = tuple(i for i in range(1, 11) if i % 2 != 0)
# print(impares)

# # Ejemplo 20, Imprimir las tablas de multiplicar del 1 y 2
# print ("Ejemplo 20")
# for i in range(1, 3):
#     print(f"Tabla del {i}")
#     print("----------------")
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i*j}")

# # Ejemplo 21, Introducir un número por teclado y crear
# # una tabla de multiplicar de ese número del 1 al 10,
# # si se ingresa 0 termina el programa
# print ("Ejemplo 21")
# while True:
#     numero = int(input("Ingrese un número: "))
#     if numero == 0:
#         break
#     print(f"Tabla del {numero}")
#     for i in range(1, 11):
#         print(f"{numero} x {i} = {numero*i}")
# print ("Fin")

# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for fila in matriz:
#     for columna in fila:
#         print(columna, end=" ")
#     print()

# # Ejemplo 22, Introducir un número por teclado
# # y crear una matriz nxn con la letra X
# print ("Ejemplo 22")
# n = int(input("Ingrese un número: "))
# matriz = [['X' for i in range(n)] for j in range(n)]
# for fila in matriz:
#     for columna in fila:
#         print(columna, end=" ")
#     print()
# print (matriz)

# Ejercicio 6, Crear una matriz ingresando un número por teclado
# para el tamaño de la matriz y en cada posición colocar una tupla con (i, j)
n = int(input("Ingrese un número: "))
matriz = [[(j,i) for i in range(n)] for j in range(n)]
for fila in matriz:
    for columna in fila:
        print(columna, end=" ")
    print()

print(matriz)
