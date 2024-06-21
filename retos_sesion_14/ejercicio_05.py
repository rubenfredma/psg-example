# Crear una función que reciba una cadena y devuelva la cadena invertida

def cadena_inv(cadena):
    resultado = cadena[::-1]
    return resultado

texto = "hola mundo"
print(texto)
print(cadena_inv(texto))