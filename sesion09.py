# print ("Lista de enteros")
# mi_lista = [1,2,3,4,5]
# print (mi_lista)

# print ("Lista de cadenas")
# mi_lista = ["hola", "mundo", "python"]
# print (mi_lista)
# print(type(mi_lista))

# print ("Lista mixta")
# mi_lista = [1, "hola", 3.14, "mundo", 5]
# print (mi_lista)

# print ("Lista vacía")
# mi_lista = []
# print (mi_lista)
# print(type(mi_lista))

# print ("Lista a partir de una cadena")
# mi_lista = list("hola mundo")
# print (mi_lista)

# print ("Lista a partir de una tupla")
# mi_tupla = (1,2,3,4,5)
# print (mi_tupla)
# mi_lista = list(mi_tupla)
# print (mi_lista)

# print ("Lista por comprensión")
# mi_lista = [x for x in range(10)]
# print (mi_lista)

# print ("Indexación positivo de una lista")
# lista = [1, "hola", 3.14, (1,2)]
# print (lista[0], type(lista[0])) 
# print (lista[1], type(lista[1])) 
# print (lista[2], type(lista[2])) 
# print (lista[3], type(lista[3])) 

# print ("Indexación negativo de una lista")
# lista = [1, "hola", 3.14, (1,2)]
# print (lista[-1], type(lista[-1]))
# print (lista[-2], type(lista[-2]))
# print (lista[-3], type(lista[-3]))
# print (lista[-4], type(lista[-4]))

# print ("Modificación de una lista")
# lista = [1, "hola", 3.14, (1,2)]
# print (lista)
# lista[0] = 2
# lista[1] = "mundo"
# print (lista)

# print ("Slicing de una lista")
# lista = ["P", "y", "t", "h", "o", "n", "L", "a", "P", "a", "z"]
# print (lista)
# sub_lista = lista[2:7]
# print(sub_lista)
# print(type(sub_lista))

# print ("Slicing con paso positivo")
# lista = ["P", "y", "t", "h", "o", "n", "L", "a", "P", "a", "z"]
# print (lista)
# sub_lista = lista[0:9:3]
# print (sub_lista)

# print ("Slicing con paso negativo")
# lista = ["P", "y", "t", "h", "o", "n", "L", "a", "P", "a", "z"]
# print (lista)
# sub_lista = lista[8:2:-4]
# print (sub_lista)

# print ("Slicing negativo con paso negativo")
# lista = ["P", "y", "t", "h", "o", "n", "L", "a", "P", "a", "z"]
# print (lista)
# sub_lista = lista[-1:-8:-2]
# print (sub_lista)

# print ("Slicing negativo con paso positivo")
# lista = ["P", "y", "t", "h", "o", "n", "L", "a", "P", "a", "z"]
# print (lista)
# sub_lista = lista[-8:-1:2]
# print (sub_lista)

# print ("Concatenación de listas")
# lista1 = [1,2,3]
# lista2 = ["a","b","c"]
# concatenar = lista1 + lista2
# print (lista1, lista2)
# print (concatenar)
# print (type(concatenar))

# print ("Repetición de listas")
# lista = [True, False]
# repetir = lista * 3
# print (lista)
# print (repetir)
# print (type(repetir))

# print ("Método index(valor)")
# lista = [1,True,3.14,"hola",5]
# valor = "hola"
# print (valor, lista.index(valor))
# valor = 3.14
# print (valor, lista.index(valor))

# print ("Método count(valor)")
# lista = [1,True,3.14,"hola",5, True, True, 3.140]
# valor = True
# print (valor, lista.count(valor))
# valor = 3.14
# print (valor, lista.count(valor))

# print ("Método insert(i, valor)")
# lista = [1,2,3,4,5]
# print (lista)
# lista.insert(2, "OwO")
# print (lista)

# print ("Método append(valor)")
# lista = [1,2,3,4,5]
# print (lista)
# lista.append("(OwO=)")
# print (lista)

# lista.append("(OwO=)")
# print (lista)
# lista.append("(OwO=)")
# print (lista)

# print ("Método extend(iterable)")
# lista = [1,2,3]
# print (lista)

# # convierte cada caracter en un elemnt de la lista
# lista.extend(":3")
# print (lista)

# # enviando otra lista
# lista.extend(["(¬_¬ )", "(O_O=)"])
# print (lista)

# # extendiendo con tuplas
# lista.extend(("😅", "😎"))
# print(lista)

# print ("Método remove(valor)")
# lista = [1,2,"UwU",4,5, "UwU"]
# print (lista)
# # elimina la 1ra vez que encuentra
# lista.remove("UwU")
# print (lista)
# # elimina la 2da vez q encuentra
# lista.remove("UwU")
# print (lista)

# print ("Método pop(index)")
# lista = ["OwO",3,"UwU",5]
# print (lista)
# lista.pop(1)
# print (lista)
# print ("Método pop()")
# lista.pop()
# print (lista)

# # obteniendo los valores eliminados
# print ("Método pop(index)")
# lista = ["OwO",3,"UwU",5]
# print (lista)
# var1 = lista.pop(1)
# print (lista)
# print(var1)

# print ("Método pop()")
# var2 = lista.pop()
# print (lista)
# print(var2)

# #  deja la lista vacia
# print ("Método clear()")
# lista = ["ewe","OwO","UwU"]
# print (lista)
# lista.clear()
# print (lista)

# print ("Método sort(), oredna de manor a mayor")
# lista = [3,1,5,2,4]
# print (lista)
# lista.sort()
# print (lista)

# print ("Método sort(), ordena de mayor a menor")
# lista = [3,1,5,2,4]
# print (lista)
# lista.sort(reverse=True)
# print (lista)

# print ("Método reverse(), invierte el orden de la lista")
# lista = [3,1,5,2,4]
# print (lista)
# lista.reverse()
# print (lista)

# # se hace una referencia a la lista con  copia = lista
##  NO HACE UNA COPIA DEL ORIGINAL
# print ("Asignación de lista")
# lista = [1,2,3,4,5]
# print (lista)
# copia = lista
# copia[0] = 6
# print (copia)
# print (lista)

# print ("Método copia con slicing")
# lista = [1,2,3,4,5]
# print (lista)
# # crea otro objeto con los mismos datos
# # apunta a otra posicion de memoria
# copia = lista[:]
# copia[0] = 6
# print (copia)
# print (lista)

# print ("Método copy()")
# lista = [3,1,5,2,4]
# print (lista)
# # copia en otro espacio de memoria
# copia = lista.copy()
# print (copia)
# print (copia == lista)

# # copia es la lista?? FALSE => apuntan a segment dist de memoria
# # pueden contener los mismos elementos, pero pueden trabajar indepen
# print(copia is lista)   # [1:23]

# print ("Método copia con slicing")
# lista = [1,2,3,4,5]
# print (lista)
# copia = lista.copy()
# copia[0] = 6
# print (copia)
# print(lista)

# print ("Función len()")
# lista = [1,True,3.14,"🐍",5]
# print (lista)
# print (len(lista))       

# print ("Función max()")
# lista = [1,2,3,4,5]
# print (lista)
# print (max(lista))
# lista = ["a","b","c","d","e"]
# print (lista)
# print (max(lista))

# print ("Función min()")
# lista = [1,2,3,4,5]
# print (lista)
# print (min(lista))
# lista = ["a","b","c","d","e"]
# print (lista)
# print (min(lista))
         
# print ("Función sum()")  # solo nros
# lista = [1,2,3,4,5]
# print (lista)
# print (sum(lista))

# print ("Comparación de listas")
# lista = [1,2,3,4,5]
# print (lista)
# print (3 in lista)
# print (6 in lista)
# print (3 not in lista) #3 no esta en la lista? = False
# print (6 not in lista)
# print ([1,2,3] in lista) #  la sublista esta en la lista? = False

# lista = [1,2,3,4,5,[1,2,3]]
# print ([1,2,3] in lista)

# # si son el mismo objeto en memoria
# print ("Comparación de listas")
# lista1 = [1,2,3,4,5]  # en memoria-1
# lista2 = [1,2,3,4,5]  # en memoria-2
# lista3 = [1,2]        # en memoria-3
# print (lista1, lista2, lista3)

# # es false, porque estan en dif espacios de memoria
# print (lista1 is lista2)
# print (lista1 is not lista2)  # True
# print(lista3 is lista1)

# #  '=='  compara a nivel de valores
# lista1 = [1,2,3,4,5]  # en memoria-1
# lista2 = [1,2,3,4,5]  # en memoria-2
# print (lista1 is lista2)
# print(lista1 == lista2)

# # Operadores de comparacion, compara elemento a elemento
# print ("Menor y Menor Igual que")
# print ([1,2,3] <= [1,2,4])
# print ([1,2,3] <= [1,2,2,2])
# print ([1,2,3] <= [2])
# print ([1,2,3] < [1,2,3])
# print ([1,2,3] <= [1,2,3])

# print ("Mayor y Mayor Igual que")
# print ([1,2,3] >= [1,2,4])
# print ([1,2,3] >= [1,2,2,2])
# print ([1,2,3] >= [2])
# print ([1,2,3] > [1,2,3])
# print ([1,2,3] >= [1,2,3])

# print ("Igual y Desigual que")
# print ([1,2,3] == [1,2,3])
# print ([1,2,3] == [1,2,4])
# print ([1,2,3] != [1,2,3])
# print ([1,2,3] != [1,2,4])

print ("Listas anidadas")
lista = [1,2,3,[4,5,6]]
print (lista)
print (type(lista))
valor_lista = lista[3]
print (valor_lista)
print (type(valor_lista))
valor = valor_lista[1]
print (valor)
print (type(valor))

