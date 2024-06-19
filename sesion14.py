# # Funciones: bloques de codigo
# def nombre_funcion():
#     print ("Bloque de código")
# nombre_funcion()

# # error, llama a alggo que no esta definido
# nombre_funcion()
# def nombre_funcion():
#     print ("Bloque de código")

# def nombre_funcion():
#     print ("Bloque de código")
# nombre_funcion()
# nombre_funcion()
# nombre_funcion()
# nombre_funcion()

# 	# Funcion sinargumento y sin retorno
# def funcion():
#     print ("Bloque de código")
# funcion()

# # Ejemplo 1, Crear una función para imprimir una lista de 10 números pares
# # y llamarla dos veces
# print ("Ejemplo 1")
# print ("1. Definir función")
# def imprimir_pares():
#     pares = [i for i in range(0, 21, 2)]
#     print (pares)
# print ("2. Llamar función")
# imprimir_pares()
# imprimir_pares()

# # Ejercicio 1, crear una función que imprima un mensaje de bienvenida del
# # siguiente conjunto de forma aleatoria

# def mensaje():
#     mensajes = {"Bienvenido al Python Study Group 🐍","¡Hola y bienvenido al Python Study Group! ✨","Hola, aprendamos Python juntos 🐍"}
#     print(mensajes.pop())
# mensaje()
# mensaje()

# # Funciones sin argumentos y con un retorno
# def funcion():
#     return "Bloque de código"
# resultado = funcion()
# print (resultado)

# # Ejemplo 2, Crear una función que devuelva un saludo en diferentes idiomas
# print ("Ejemplo 2")
# print ("1. Definir función")
# def saludo():
#     saludos = {"Hola", "Hello", "Bonjour", "Ciao"}
#     return saludos.pop()

# print ("2. Llamar función")
# resultado = saludo()
# print (resultado)

# # Ejercicio 2, Devolver una fruta aleatoria del siguiente conjunto
# def almacen():
#     frutas = {'🍅','🍌','🍎','🍇','🍉'}
#     return frutas.pop()

# fruta = almacen()
# print(fruta)

# def devolver_fruta():
#     frutas = {'🍅','🍌','🍎','🍇','🍉'}
#     return frutas.pop()

# fruta = devolver_fruta()
# print (fruta)

# # Funciones sin argumento y con multiples retornos, Devuelve una tupla en Python
# def funcion():
#     return "Bloque", "de", "código"

# resultado = funcion()
# print (resultado)
# print(type(resultado))

# def funcion():
#     return "Bloque", "de", "código"

# x,y,z = funcion()
# print(x)
# print(y)
# print(z)

# # Ejemplo 3, Crear una función que devuelva un saludo en dos idiomas
# print ("Ejemplo 3")
# print ("1. Definir función")
# def saludo():
#     saludos_es = {"Hola", "Holi", "Buenos días"}
#     saludos_en = {"Hello", "Hi", "Good morning"}
#     return saludos_es.pop(), saludos_en.pop()

# print ("2. Llamar función")
# resultado = saludo()
# print (resultado)

# # Ejercicio 3, Devolver una fruta y un color aleatorio de los siguientes conjuntos
# def devuelve_fruta_color():
#     frutas = {'🍏​','🍌','🍎','🍇','🍉'}
#     colores = {'🔴','💧​','💡','⛺','🔵'}
#     return frutas.pop(), colores.pop()

# fruta,color =  devuelve_fruta_color()
# print(f"FRUTA: {fruta}")
# print(f"COLOR: {color}")

# def devolver_fruta_color():
#     frutas = {'🍅','🍌','🍎','🍇','🍉'}
#     colores = {'🔴','🟠','🟡','🟢','🔵'}
#     return frutas.pop(), colores.pop()

# fruta, color = devolver_fruta_color()
# print (fruta, color)

# # Funciones con un argumento y sin retorno
# def funcion(parametro):
#     print (parametro)

# funcion("Bloque de código") #1 Argumento

# # Ejemplo 4, Crear una función que imprima el cuadrado de un número
# def cuadrado(x):
#   print(x**2)

# cuadrado(2)

# print ("Ejemplo 4")
# print ("1. Definir función")
# def cuadrado(numero):
#     print (numero**2)

# print ("2. Llamar función")
# cuadrado(5)
# cuadrado(10)

# # Ejercicio 4, Crear una función que imprima el mensaje de bienvenida de acuerdo
# # al un idioma enviado como argumento, si no existe imprimir un mensaje por defecto
# def mensaje_bienvenida(idioma):
#     mensajes = {"es":"Bienvenido al Python Study Group 🐍",
#                  "en": "Hello and welcome to the Python Study Group! ✨",}
#     print(mensajes.get(idioma,"Mensaje x defecto"))

# mensaje_bienvenida("es")
# mensaje_bienvenida("en")
# mensaje_bienvenida("it")

# def bienvenida(idioma):
#     mensajes = {
#         "es":"Bienvenido al Python Study Group 🐍",
#         "en": "Hello and welcome to the Python Study Group! ✨",
#     }
#     print (mensajes.get(idioma, "¡Hola!"))

# bienvenida("es")
# bienvenida("en")
# bienvenida("fr")

# # Funciones con multiples argumentos y sin retorno
# def funcion(param1, param2,paramN):
#     print (param1, param2,paramN)

# funcion("Bloque", "de", "código")

# # Ejemplo 5, Crear una función que reciba una cadena y un entero
# # y repita la cadena el número de veces
# print ("Ejemplo 5")
# print ("1. Definir función")
# def repetir(cadena, veces):
#     print (cadena*veces)

# print ("2. Llamar función")
# repetir("🍩🎉", 10)

# # Ejercicio 5, Crear una función que reciba una lista de animales, un entero
# # e imprima una lista con los animales repetidos el número de veces
# def repetir(lista, nro):
#     lista2=[]
#     for i in lista:
#       lista2.append(i*nro)
#     print(lista2)

# animales = ['🐶','🐦','🐭','🐧','🐵']
# repetir(animales,5)
# # ------------
# def repetir_animales(animales,veces):
#     lista = [animal*veces for animal in animales]
#     print (lista)

# animales = ['🐶','🐱','🐭','🐹','🐰']
# repetir_animales(animales,3)

# # Funciones con multiples argumentos y con un retorno
# def funcion(param1, param2, paramN):
#     return param2

# resultado = funcion("Bloque", "de", "código")
# print (resultado)

# # Ejemplo 6, Crear una función que reciba dos números y devuelva una lista
# # con la suma, resta, multiplicación y división de los números
# print ("Ejemplo 6")
# print ("1. Definir función")
# def operaciones(numero1, numero2):
#     suma = numero1 + numero2
#     resta = numero1 - numero2
#     multiplicacion = numero1 * numero2
#     division = numero1 / numero2
#     return [suma, resta, multiplicacion, division]

# print ("2. Llamar función")
# resultado = operaciones(10, 5)
# print (resultado)

# # Ejercicio 6, Crear una función que reciba dos enteros y una cadena
# # devolver el resultado de la operación de los números según la cadena puede ser
# # suma, resta, multiplicación o división
# def calculo(n1,n2,operacion):
#   resultado=0
#   if operacion == "suma":
#     resultado = n1+n2
#   elif operacion == "resta":
#     resultado = n1-n2
#   elif operacion == "multiplicacion":
#     resultado = n1*n2
#   elif operacion == "division":
#     resultado = n1/n2
#   else:
#     resultado="Operacion no permitida"
#   return resultado

# op = calculo(10,5,"sua")
# print(op)
# #----------------
# def operacion(numero1, numero2, operacion):
#     if operacion == "suma":
#         return numero1 + numero2
#     elif operacion == "resta":
#         return numero1 - numero2
#     elif operacion == "multiplicacion":
#         return numero1 * numero2
#     elif operacion == "division":
#         return numero1 / numero2
#     else:
#         return "Operación no válida"

# resultado = operacion(10, 5, "suma")
# print (resultado)

# # Funciones con multiples argumentos y con multiples retornos
# def funcion(param1, param2,paramN):
#     return paramN, param2,param1  # retornando como tupla

# resultado = funcion("Bloque", "de", "código")
# print (resultado)

# # Ejemplo 7, Crear una función que reciba dos números y devuelva la suma, resta,
# # multiplicación y división de los dos números

# print ("Ejemplo 7")
# print ("1. Definir función")
# def operaciones(numero1,numero2):
#     suma = numero1 + numero2
#     resta = numero1 - numero2
#     multiplicacion = numero1 * numero2
#     division = numero1 / numero2
#     return suma, resta, multiplicacion, division

# print ("2. Llamar función")
# # desempaquetando la salida de la funcion
# suma,resta,multiplicacion,division = operaciones(10,5)
# print(suma,resta,multiplicacion,division)

# # Ejercicio 7, Crear una juego de piedra papel o tijera, donde reciba dos jugadas por teclado
# # y devuelva las jugadas y el resultado, si ingresa salir terminar el juego

# def obtener_jugada(jugador):
#     while True:
#         jugada = input(f"Jugador {jugador}, ingresa tu jugada (piedra, papel, tijera) o 'salir' para termnar: ").lower()
#         if jugada in ["piedra","papel","tijera","salir"]:
#             return jugada
#         else:
#             print("Entrada no valida. Intentalo de nuevo")

# def determinar_ganador(jugada1, jugada2):
#     if jugada1 == jugada2:
#         return "Empate"
#     elif (jugada1 == "piedra" and jugada2 == "tijera") or \
#          (jugada1 == "papel" and jugada2 == "piedra") or \
#          (jugada1 == "tijera" and jugada2 == "papel"):
#          return "Jugador 1 gana"
#     else:
#         return "Jugador 2 gana"

# def jugar():
#     while True:
#         jugada1 = obtener_jugada(1)
#         if jugada1 == "salir":
#             print("Juego terminado")
#             break
#         jugada2 = obtener_jugada(2)
#         if jugada2 == "salir":
#             print("Juego terminado")
#             break

#         print(f"Jugador 1 jugo: {jugada1}")
#         print(f"Jugador 2 jugo: {jugada2}")

#         resultado = determinar_ganador(jugada1, jugada2)
#         print(resultado)

# # inicia el juego
# jugar()
# # -----------------
# def jugar_piedra_papel_tijera(jugada1, jugada2):
#     if jugada1 == jugada2:
#         resultado = "Empate"
#     elif jugada1 == "piedra" and jugada2 == "tijera":
#         resultado = "Jugador 1 gana"
#     elif jugada1 == "papel" and jugada2 == "piedra":
#         resultado = "Jugador 1 gana"
#     elif jugada1 == "tijera" and jugada2 == "papel":
#         resultado = "Jugador 1 gana"
#     else:
#         resultado = "Jugador 2 gana"
#     return jugada1, jugada2, resultado

# while True:
#     jugador1 = input("Jugador 1: ")
#     if jugador1 == "salir":
#         break
#     jugador2 = input("Jugador 2: ")
#     if jugador2 == "salir":
#         break
#     resultado = jugar_piedra_papel_tijera(jugador1, jugador2)
#     print (resultado)

# # Variables globales y locales
# variable_global = "Variable global"
# def funcion():
#     variable_local = "Variable local"
#     print ("✨",variable_global)
#     print ("✨",variable_local)

# funcion()
# print ("🎈",variable_global)
# #print ("🎈",variable_local)  #ERRROR

# # prioridad
# variable = "Variable global"
# print ('0.',variable)

# def funcion():
#     variable = "Variable local"  # mayor prioridad
#     print ('1.',variable)

# funcion()
# print ('2.',variable)

# # Ejemplo 8, De la siguiente lista de números obtener el mayor y menor número con una función
# numeros = [10, 5, 20, 15, 25, 30] #Global

# def mayor_menor(): #No recibe argumentos
#     mayor = max(numeros) #Local
#     menor = min(numeros) #Local
#     return mayor, menor #Devuelve dos valores

# resultado = mayor_menor()
# print (resultado)

# # Ejercicio 8, De la siguiente cadena global convertir en formato título
# # y contar las vocales aeiou con una función

# cadena = "python es un lenguaje de programación"
# def form_titulo(cadena):
#     return cadena.title()

# def contar_vocales(cadena):
#     cont=0
#     for i in cadena:
#         if i in 'aeiou':
#           cont +=1

#     return cont

# print(form_titulo(cadena))
# cantidad = contar_vocales(cadena)
# print(f"La cadena tiene {cantidad} vocales")

# #-----------
# def formato_vocales():
#     titulo = cadena.title()
#     vocales = sum([1 for letra in titulo if letra in "aeiouáéíóúAEIOUÁÉÍÓÚ"])
#     return titulo, vocales

# cadena = "python es un lenguaje de programación"
# resultado = formato_vocales()

# print (resultado)

# #------------
# def funcion(*args):
#     print (args)
#     print (type(args))

# funcion("Bloque", "de", "código")

# # Ejemplo 9 Crear una función que reciba un número y una cantidad de cadenas,
# # concatene las cadenas y la devuelva repetida N veces
# print ("Ejemplo 9")
# print ("1. Definir función")
# def concatenar(numero, *cadenas):
#     concatenado = ""
#     for cadena in cadenas:
#         concatenado += cadena
#     return concatenado*numero

# print ("2. Llamar función")
# resultado = concatenar(3, "🍎", "🍌", "🍍")
# print (resultado)

# # Ejercicio 9, Crear una función que reciba N objetos y genere una tupla
# # y una lista con los objetos usando *args
# def tupla_lista(*args):
#     tupla = tuple(args)
#     lista = list(args)
#     return tupla, lista

# lista, tupla = tupla_lista(1, 1.1, True, "🍎")

# print (lista)
# print (tupla)

# #  ---------------
# def generar_tupla_lista(*args):
#     return tuple(args), list(args)

# tupla, lista = generar_tupla_lista(1, 1.1, True, "⚽")
# print("Tupla",tupla)
# print("Lista:",lista)

# # KWARGS  uso como diccioanrio
# def funcion(**kwargs):
#     print (kwargs)
#     print (type(kwargs))

# funcion(nombre="Jhon", apellido="Doe", genero="M")

# # Ejemplo 10, Crear una función que reciba los datos de una persona y devuelva
# # un mensaje con los datos
# print ("Ejemplo 10")
# print ("1. Definir función")
# def datos_persona(**datos):
#     mensaje = ""
#     for clave, valor in datos.items():
#         mensaje += f"{str(clave).title()}: {str(valor).upper()}\n"
#     return mensaje
# print ("2. Llamar función")
# resultado = datos_persona(nombre="Jhon", apellido="Doe", edad=20, boliviano=True)
# print (resultado)

# # Ejercicio 10, Crea un simulador de lavar platos con una función que reciba los objetos
# # a lavar y el tiempo de lavado de cada objeto devuelva un mensaje con los objetos
# # lavados y el tiempo total de lavado
# def lavar(**objetos):
#     tiempo_total = 0
#     mensaje = ""
#     for objeto, tiempo in objetos.items():
#         tiempo_total += tiempo
#         mensaje += f"{objeto}: {tiempo} minutos\n"
#     mensaje += f"Tiempo total: {tiempo_total} minutos"
#     return mensaje

# resultado = lavar(plato=5, vaso=3, tenedor=1, cuchara=0.5)
# print (resultado)

# # enviando directamente el objeto diccionario
# def lavar_platos(objetos):
#     tiempo_total = sum(objetos.values())
#     return f"Objetos lavados: {', '.join(objetos.keys())}. tiempo total: {tiempo_total}"

# objetos = {
#     "plato":5,
#     "vaso":3,
#     "tenedor":1,
#     "cuchara":0.5
# }
# resultado = lavar(plato=5, vaso=3, tenedor=1, cuchara=0.5)
# print (lavar_platos(objetos))

# # Documentacion de funciones
# # se puede doc una fun con comentario de varias lineas
# # Se accede con la funcion .__doc__
# print ("Acceso a la documentación")
# def funcion():
#     """
#     Documentación aquí
#     """
#     print ("Bloque de código")
# print (funcion.__doc__)
# print ("Fin de la ejecución")

# #------  funciones dentro de funciones
# # Ejemplo 11, Crear tres funciones una principal que reciba un número y dos funciones anidadas
# # que devuelvan el cuadrado y el cubo del número
# print ("Ejemplo 11")
# print ("1. Definir función Principal")
# def principal(numero):
#     cuadrado = cuadrado_numero(numero)
#     cubo = cubo_numero(numero)
#     return cuadrado, cubo
 
# print ("2. Definir función Cuadrado")
# def cuadrado_numero(numero):
#     return numero**2
 
# print ("3. Definir función Cubo")
# def cubo_numero(numero):
#     return numero**3
 
# print ("4. Llamar función Principal")
# numero = 5
# resultado = principal(numero)
# print (numero, resultado)

# # Ejercicio 11, Crear funciones de limpieza de una cadena para obtener las letras 
# # y convertir todo en mayúsculas crea funciones de limpieza y función una principal
# # cadena = "Python es un lenguaje de programación 🎈. Feliz Aprendizaje el 2024"
# def limpiar_letras(cadena):
#     """
#     Elimina los números de una cadena y espacios
#     """
#     return "".join([letra for letra in cadena if letra.isalpha()])
# def limpiar_mayusculas(cadena):
#     """
#     Convierte una cadena en mayúsculas
#     """
#     return cadena.upper()

# def limpiar(cadena):
#     cadena = limpiar_letras(cadena)
#     cadena = limpiar_mayusculas(cadena)
#     return cadena

# cadena = "Python es un lenguaje de programación 🎈. Feliz Aprendizaje el 2024"
# resultado = limpiar(cadena)
# print (cadena)
# print (resultado)

# # Ejemplo 12, Crear una función recursiva para obtener el 10cimo número par
# print ("Ejemplo 12")
# print ("1. Definir función")
# def numero_par(numero):
#     if numero == 0:
#         return 0
#     else:
#         return numero_par(numero-1) + 2
 
# print ("2. Llamar función")
# resultado = numero_par(10)
# print (resultado)

# # Ejercicio 12, Crear una función recursiva para obtener el factorial de un número
# # 5!=5∗4∗3∗2∗1=120
# def factorial(numero):
#     if numero == 0:
#         return 1
#     else:
#         return numero*factorial(numero-1)

# resultado = factorial(5)
# print (resultado)

# # Ejemplo 13, Crear una función anónima para obtener el cuadrado de un número
# print ("Ejemplo 13")
# cuadrado = lambda numero: numero**2
# resultado = cuadrado(5)
# print (resultado)
# resultado = cuadrado(10)
# print (resultado)

# Ejercicio 13, Crear una función anónima para obtener de una cadena las letras 
# solo los alfanuméricos y convertir en mayúsculas
cadena = "Python es un lenguaje de programación"
limpiar = lambda cadena: "".join([letra for letra in cadena if letra.isalnum()]).upper()
resultado = limpiar(cadena)
print (cadena)
print (resultado)


