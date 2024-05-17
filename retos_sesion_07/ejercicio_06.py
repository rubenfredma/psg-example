# Agregar 5 ejemplos con otras funciones no vistas en la sesion
# Utilizar la documentacion Metodos de cadenas: 
#  https://docs.python.org/3/library/stdtypes.html#string-methods

# center()
print("center(), Retorna al centro de una cadena con longitud definida")
texto = "centro"
# 10 total de caracteres, usando '*' como caracter de relleno
x = texto.center(10,"*")
print(texto)
print(x)

print(".endswith(), Retorna verdadero si la cadena termina con el valor especificado")
frase = "Hola, bienvenido a python."
x = frase.endswith("python.")
print(frase)
print(x)

print(".rpartition(). Devuelve una tupla donde la cadena se divide en tres partes")
frase = "Me gusta comer las bananas para desayunar"
x = frase.rpartition("para")
print(frase)
print(x)

print(".splitlines(). Divide la cadena al encontrar saltos de linea y devuelve en una lista")
cadena = "Gracias por la musica\nBienvenido a la jungla."
x = cadena.splitlines()
print(cadena)
print(x)

print(".isidentifier(). Devuelve true, si la cadena es un identificador valido")
cadena = "Demo"
x = cadena.isidentifier()
print(cadena)
print(x)