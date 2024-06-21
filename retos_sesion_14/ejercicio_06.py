# Crear una función que reciba una lista de números 
# y devuelva solo los números pares

def lista_pares(lista):
    lista_aux = []
    for i in lista:
        if i%2 == 0:
            lista_aux.append(i)
        
    return lista_aux

numeros = [1,2,3,4,5,6,7,8,9]
resultado = lista_pares(numeros)
print (resultado)

