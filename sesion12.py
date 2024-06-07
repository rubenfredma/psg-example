# Estructuras de control: sentencias condicionales

# print ("Inicio")
# #condicion = True
# condicion = False
# if condicion:
#     # Bloque de código
#     print ("Cumple condición")
# print ("Fin")

# print ("Inicio")
# numero = 3
# if numero % 2 == 0:   # Si el módulo de 2 es 0
#     print ("El número es par")
# print ("Fin")

# print ("Inicio")
# condicion = False
# if condicion:
#     # Bloque de código
#     print ("Cumple condición")
# else:
#     # Bloque de código
#     print ("No cumple condición")
# print ("Fin")

# print ("Inicio")
# numero = 3
# if numero % 2 == 0:    # Si el módulo de 2 es 0
#     print ("El número es par")
# else:
#     print ("El número es impar")
# print ("Fin")

# print ("Inicio Anidado")
# condicion_1 = True
# condicion_2 = False
# if condicion_1:
#     print ("Cumple condición 1")
#     if condicion_2:
#         print ("Cumple condición 2")
#     else:
#         print ("No cumple condición 2")
# else:
#     print ("No cumple condición 1")
# print ("Fin")

# print ("Inicio Par, Impar o Cero")
# numero = 2
# if numero > 0 or numero < 0:
#     if numero % 2 == 0: # Si el módulo de 2 es 0
#         print ("El número es par")
#     else:
#         print ("El número es impar")
# else:
#     print ("El número es cero")
# print ("Fin")

# print ("Inicio ELIF")
# condicion_1 = True
# condicion_2 = True
# if condicion_1:
#     print ("Cumple condición 1")
# elif condicion_2:
#     print ("Cumple condición 2")
# else:
#     print ("No cumple condición 1 ni 2")
# print ("Fin")

# print ("Inicio Positivo, Negativo o Cero")
# numero = -1
# if numero > 0:
#     print ("El número es positivo")
# elif numero < 0:
#     print ("El número es negativo")
# else:
#     print ("El número es cero")

# print ("Inicio Ternario")
# condicion = False
# resultado = "Cumple" if condicion else "No cumple"
# print (resultado)
# print ("Fin")

# print ("Inicio Ternario Par o impar")
# numero = 2
# resultado = "El nro es par" if numero%2 == 0 else "El nro es impar"
# print (resultado)
# print ("Fin")

# print ("Truthiness Enteros")
# dividendo = int(input("Dividendo: "))
# divisor = int(input("Divisor: "))
# print (dividendo,divisor)
# if divisor:         #divisor != 0
#     print (dividendo / divisor)
# else:
#     print ("No se puede dividir entre cero")
# print ("Fin")

# print ("Truthiness Flotantes")
# dividendo = float(input("Dividendo: "))
# divisor = float(input("Divisor: "))
# print (dividendo,divisor)

# if divisor: #divisor != 0.0
#     print (dividendo / divisor)
# else:
#     print ("No se puede dividir entre cero")
# print("FIN")

# print ("Truthiness Cadenas")
# cadena = input("Cadena: ")
# print (cadena)
# if cadena:    # len(cadena) != 0 or cadena != "" 
#     print ("La cadena no está vacía")
# else:
#     print ("La cadena está vacía")
# print ("Fin")

# print ("Truthiness Tuplas")
# tupla = tuple(input("Tupla: "))
# print (tupla)
# if tupla:             # len(tupla) != 0 or tupla != ()
#     print ("La tupla no está vacía")
# else:
#     print ("La tupla está vacía")
# print ("Fin")

# print ("Truthiness Listas")
# lista = list(input("Lista: "))
# print (lista)
# if lista: # len(lista) != 0 or lista != []
#     print ("La lista no está vacía")
# else:
#     print ("La lista está vacía")
# print ("Fin")

# print ("Truthiness Conjuntos")
# conjunto = set(input("Conjunto: "))
# print (conjunto)
# if conjunto:     # len(conjunto) != 0 or conjunto != set()
#     print ("El conjunto no está vacío")
# else:
#     print ("El conjunto está vacío")
# print ("Fin")

# print ("Truthiness Diccionarios")
# diccionario = {}
# clave = input("Clave: ")
# valor = input("Valor: ")
# if clave:
#   diccionario = {clave:valor}
# print (diccionario)
# if diccionario: # diccionario != {}
#     print ("El diccionario no está vacío")
# else:
#     print ("El diccionario está vacío")
# print ("Fin")

# print ("Truthiness None")
# valor = None
# print (valor, type(valor))
# if valor:      # valor != None
#     print ("El valor no es None")
# else:
#     print ("El valor es None")
# print ("Fin")

# entero = int(input("Entero: "))
# resultado = "Diferente de 0" if entero else "Igual a 0"
# print (resultado)

# flotante = float(input("Flotante: "))
# resultado = "Diferente de 0.0" if flotante else "Igual a 0.0"
# print (resultado)

# cadena = input("Cadena: ")
# resultado = "No está vacía" if cadena else "Está vacía"
# print (resultado)

# temp=int(input("Digite la temperatura: "))
# if temp > 30:
#     print("Encender")
# elif temp < 20:
#     print("Apagar")
# else:
#     print("ambiente normal")

# frutas = ["platano","sandia","sandia","pera"]
# if "manzana" in frutas:
#     print("hay manzanas")
#     cantidad = frutas.count('manzana')
#     print(f"Se tienen {cantidad} manzanas")
# else:
#     print("No hay manzanas")
#     frutas.append('manzana')
#     frutas.append('manzana')
#     print(frutas)

# cesta = ['🍎','🍌','🍒','🍉']
# print (cesta)
# if '🍎' in cesta:
#     print (f"Hay {cesta.count('🍎')} manzanas")
# else:
#     cesta.extend(['🍎','🍎'])
#     print (cesta)


# cesta = ['🍑','🍓','🍉']
# print (cesta)
# resultado = f"Hay {cesta.count('🍎')} manzanas" if '🍎' in cesta else cesta.extend(['🍎','🍎'])
# print (resultado)
# print (cesta)

## SI NO HAY => DA ERROR
# animal = {'especie':'🐶', 'nombre': 'Firulais', 'mamifero': True}
# print(animal)
# if animal["mamifero"]:
#   print(f"{animal['nombre']} es un mamifero")
# else:
#   print("el animal no es mamifero")

# animal = {'especie':'🐶', 'nombre': 'Firulais', 'mamifero': True}
# print (animal)
# if animal.get('mamifero'): # animal['mamifero']
#     print ("Es un mamífero")
# else:
#     print ("No es un mamífero")

# conjunto_1 = {'⚽','🏀','🍸'}
# conjunto_2 = {'🏈','🏉','🍳'}
# print (conjunto_1, conjunto_2)
# if conjunto_1.isdisjoint(conjunto_2): # <=>len(conjunto_1.intersection(conjunto_2)) == 0
#     conjunto_1.update(conjunto_2)
#     print (conjunto_1)
# else:
#     print ("Tienen elementos en común")
#     print (conjunto_1.intersection(conjunto_2))

# # solucion anidada
# correo = input("Correo: ")
# if "@" in correo and "." in correo and correo.count("@") == 1:
#     if correo.find("@") < correo.rfind(".") and correo.find("@") > 0 and correo.rfind(".") < len(correo) - 1:
#         if correo.rfind(".") - correo.find("@") > 1:
#             if correo.find(".") - correo.find("@") > 1:
#                 print ("El correo es válido")
#             else:
#                 print ("El correo no es válido")
#         else:
#             print ("El correo no es válido")
#     else:
#         print ("El correo no es válido")
# else:
#     print ("El correo no es válido")


# solucion con elif
correo = input("Correo: ")
if "@" not in correo or "." not in correo or correo.count("@") != 1:
    print("El correo no es válido")
elif correo.find("@") >= correo.rfind(".") or correo.find("@") == 0 or correo.rfind(".") == len(correo) - 1:
    print("El correo no es válido")
elif correo.rfind(".") - correo.find("@") <= 1:
    print("El correo no es válido")
elif correo.find(".") - correo.find("@") == 1:
    print("El correo no es válido")
else:
    print("El correo es válido")
