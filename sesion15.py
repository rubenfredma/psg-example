# Sesion 15: Errores y excepciones Try-Except

# # Ejemplo 1, División por cero
# print ("Inicio Ejemplo 1")
# x = 1 / 0
# print (x)
# print ("Fin Ejemplo 1")

# print ("Inicio Ejemplo 1")
# try:
#     x = 1 / 0
#     print (x)
# except Exception as e:
#     print("💀 Error:", e, type(e))

# print ("Fin Ejemplo 1")

# # Ejercicio 1, Crear un programa que solicite dos números y realice la división
# # de ambos números Si hay un error mostrar un mensaje de error 
# #El programa se detiene si se ingresa "salir"

# while True:
#     try:
#         n1 = input("Digite un nro: ")
#         n2 = input("Digite el 2do numero: ")

#         if n1 == "salir" or n2 == "salir":
#             break
    
#         division = int(n1)/int(n2)
#         print(f"{n1}/{n2}={division}")

#     except Exception as e:
#         print("💀 Error:", e, type(e))

# # -----------
# while True:
#     try:
#         num1 = input("Ingrese el primer número: ")
#         if num1 == "salir":
#             break
#         num2 = input("Ingrese el segundo número: ")
#         if num2 == "salir":
#             break
#         num1 = float(num1)
#         num2 = float(num2)
#         print("Resultado:", num1 / num2)
#     except Exception as e:
#         print("💀 Error:", e)

# # NameError: Se produce cuando no se encuentra una variable
# if a == 10:
#     print(True)

# # KeyError: Se produce cuando se intenta acceder a una clave que no existe en un diccionario
# a = {"a":1}
# print(a["b"])

# # Ejemplo 2, División por cero
# print ("Inicio Ejemplo 2")
# divisor = 0
# try:
#     x = 1 / divisor
#     print (x)
# except ZeroDivisionError as e:
#     print("0️⃣ Error:", e, type(e))
# except Exception as e:   # parte  no se ejecutada y salta al final
#     print("💀 Error:", e, type(e))
# print ("Fin Ejemplo 2")

# # ahora va a dividir con una cadena
# print ("Inicio Ejemplo 2")
# divisor = "0"
# try:
#     x = 1 / divisor
#     print (x)
# except ZeroDivisionError as e:  # se salta
#     print("0️⃣ Error:", e, type(e))
# except Exception as e:
#     print("💀 Error:", e, type(e))
# print ("Fin Ejemplo 2")

# # Jerarquía de excepciones
# # Ejemplo 2, División por cero   invirtiendo las lineas de except
# print ("Inicio Ejemplo 2")
# divisor = 0
# try:
#     x = 1 / divisor
#     print (x)
# except Exception as e: # Captura cualquier excepción -GENERICO
#     print("💀 Error:", e, type(e))
# except ZeroDivisionError as e:   # esta parte se salta
#     print("0️⃣ Error:", e, type(e))
# print ("Fin Ejemplo 2")

# # Ejemplo 3, De la lista de calificaciones obtener el promedio
# calificaciones = [20,40,80,"A"]
# suma = 0
# try:
#     for i in range(len(calificaciones)+1):
#         suma += calificaciones[i] 
#     promedio = suma / len(calificaciones)
#     print("Promedio:", promedio)
# except ZeroDivisionError as e:
#     print("0️⃣ Error:", e, type(e))
# except TypeError as e:
#     print("🎭 Error:", e, type(e))
# except Exception as e:
#     print("💀 Error:", e, type(e))

# # Ejemplo 3, De la lista de calificaciones obtener el promedio
# # OTRO TIPO DE ERROR, INDEX demas
# calificaciones = [20,40,80]
# suma = 0
# try:
#     for i in range(len(calificaciones)+1):
#         suma += calificaciones[i]
#     promedio = suma / len(calificaciones)
#     print("Promedio:", promedio)
# except ZeroDivisionError as e:
#     print("0️⃣ Error:", e, type(e))
# except TypeError as e:
#     print("🎭 Error:", e, type(e))
# except Exception as e: # Captura cualquier excepción
#     print("💀 Error:", e, type(e))

# # mismo ejemplo correguido
# # Ejemplo 3, De la lista de calificaciones obtener el promedio
# calificaciones = [20,40,80]
# suma = 0
# try:
#     for i in range(len(calificaciones)):
#         suma += calificaciones[i] # suma = suma + calificaciones[i]
#     promedio = suma / len(calificaciones)
#     print("Promedio:", promedio)
# except ZeroDivisionError as e:
#     print("0️⃣ Error:", e, type(e))
# except TypeError as e:
#     print("🎭 Error:", e, type(e))
# except Exception as e:
#     print("💀 Error:", e, type(e))

# # Ejemplo 4, De la lista de calificaciones obtener el promedio
# print ("Inicio Ejemplo 4")
# calificaciones = [20,40,80]
# suma = 0
# try:
#     for i in range(len(calificaciones)):
#         suma += calificaciones[i]
#     promedio = suma / len(calificaciones)
#     print("Promedio:", promedio)
# except Exception as e:
#     print("💀 Error:", e, type(e))
# else:
#     print ("🎉 Sin errores")
# print ("Fin Ejemplo 4")

# # Ejercicio 2, Crear un programa que solicite dos números y mediante una función
# # devuelva la división de ambos
# # Si hay un error mostrar un mensaje de error. El programa se detiene si se ingresa "salir"
# # Añadir un bloque else que muestre el resultado de la función

# def division(num1, num2):
#     return num1 / num2

# while True:
#     try:
#         num1 = input("Ingrese el primer número: ")
#         if num1 == "salir":
#             break
#         num2 = input("Ingrese el segundo número: ")
#         if num2 == "salir":
#             break
#         num1 = float(num1)
#         num2 = float(num2)
#         resultado = division(num1, num2)
#     except Exception as e:
#         print("💀 Error:", e)
#     else:
#         print("🎉 Resultado: ",resultado)

# # Ejemplo 5, Simula una conexión a internet que haga ping y cerrar la conexión
# print ("Inicio Ejemplo 5")
# try:
#     print("🔗 Ping...")
# except Exception as e:
#     print("💀 Error:", e)
# else:
#     print("🎉 Ping Exitoso")
# finally:
#     print("🔌 Cerrando conexión")

# # Ejemplo 6, Simula una conexión a internet que haga ping y cerrar la conexión
# print ("Inicio Ejemplo 6")
# try:
#     print("🔗 Ping...")
#     raise Exception("Error de conexión") #Excepción genérica
# except Exception as e: # Captura cualquier excepción
#     print("💀 Error:", e)
# else:
#     print("🎉 Ping Exitoso")
# finally:
#     print("🔌 Cerrando conexión")

# # Ejercicio 3, Escriba un programa que solicite un número por teclado 
# # y se almacene en una lista
# #  Si es 0 se genera una excepción
# #  Si la ejecución es correcta muestra "🎉Agregado"
# #  Termina la ejecución sólo con la palabra "salir" 
# #     utilizar la excepción KeyboardInterrupt(anula el ctrl+C)
# #  Finalmente imprima siempre la suma de los números y la lista
# numeros = []
# while True:
#     try:
#         num = input("Ingrese un número: ")
#         if num == "salir":
#             break
#         num = float(num)
#         if num == 0:
#             raise Exception("No se puede agregar el número 0")
#         numeros.append(num)
#     except KeyboardInterrupt as e:
#         print('🚫 Para salir escriba "salir"')
#     except Exception as e:
#         print("💀 Error:", e)
#     else:
#         print("🎉 Número agregado")
#     finally:
#         print("Suma:", sum(numeros))

# # Ejemplo 7, Crea una función que no hace nada, todavia se esta completando la funcion
# print("Inicio Ejemplo 7")
# def funcion():
#     pass

# funcion()
# print("Fin Ejemplo 7")

# #----------
# a=2
# if a==2:
#     print("a es igual a 2")
# else:
#     # para esta parte no esta claro q poner, con pass ya no hay error
#     pass

# # Excepciones personalizadas
# class MiError(Exception):
#     pass

# raise MiError("Mensaje de error")

# # Ejemplo 8, Tienes un frutero, saca las frutas mientras no sea un gusano y genera una excepción
# print("Inicio Ejemplo 8")
# class GusanoError(Exception):
#     pass
 
# frutero = ['🍎', '🍌', '🍐', '🐛', '🍇']
# for fruta in frutero:
#     try:
#         if fruta == '🐛':
#             raise GusanoError("😱 Ewww!")
#         print(fruta)
#     except GusanoError as e:
#         print("🐛 Error:", e)
#     except Exception as e:
#         print("💀 Error:", e)
# print("Fin Ejemplo 8")

# Ejercicio 4, Crear un programa que solicite palabras por teclado y almacene en una lista
# Si se inserta caracteres no alfabéticos se genera una excepción personalizada y no se almacena
# Si se ingresa "salir" se termina la ejecución
# Mostrar el mensaje "🎉 Palabra agregada" si no hay errores
# Finalmente imprimir la lista de palabras
class NoAlfabeticoError(Exception):
    pass

palabras = []
while True:
    try:
        palabra = input("Ingrese una palabra: ")
        if palabra == "salir":
            break
        if not palabra.isalpha():
            raise NoAlfabeticoError("Solo se permiten letras")
        palabras.append(palabra)
    except NoAlfabeticoError as e:
        print("🚫 Error:", e)
    except Exception as e:
        print("💀 Error:", e)
    else:
        print("🎉 Palabra agregada")
    finally:
        print("Lista:", palabras)

