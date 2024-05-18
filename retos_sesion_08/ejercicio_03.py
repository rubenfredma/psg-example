# Ingresa una cadena por teclado y almacena el valor en una tupla.
# - Concatena la tupla ('¡',)  + tupla almacenada + la tupla('!',)
# - Imprime el resultado concatenado
# - Repite la tupla final tres veces e imprime el nuevo resultado

tupla = (input("Digite una cadena: "),)
concatenado = ('¡',) + tupla + ('!',)
print(concatenado,type(concatenado))
repetido = concatenado * 3

print(repetido)
