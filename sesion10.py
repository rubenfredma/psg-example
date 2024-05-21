
# conjunto = {'🍕','🍔','🍟','🌭'}
# print(conjunto) # {'🍔', '🌭', '🍕', '🍟'}

# print ("Conjunto de enteros")
# conjunto = {1, 2, 3, 4, 5}
# print(conjunto)
# print(type(conjunto))

# conjunto = {'🍕','🍔','🍟','🌭','🍕','🍟'}
# print(conjunto) # {'🍕', '🍟', '🌭', '🍔'}
# print(type(conjunto))

# print ("Conjunto mixto")
# conjunto = {True, 1, 3.14, '☕'}
# print(conjunto)
# print(type(conjunto))

# # CONJUNTO VACIO
# conjunto = set()
# print(conjunto)
# print(type(conjunto))

# print ("Conjunto vacío")
# conjunto = set()
# print(conjunto)
# print(type(conjunto))

# print ("Conjunto a partir de la cadena")
# cadena = 'Hola Mundo Hola Mundo'
# conjunto = set(cadena)
# print(conjunto)
# print(type(conjunto))

# print ("Conjunto a partir de una tupla")
# tupla = (1, 2, 3, 4, 5, 5)
# conjunto = set(tupla)
# print(conjunto)
# print(type(conjunto))

# print ("Conjunto a partir de una lista")
# lista = [True, False, 0, 1]
# conjunto = set(lista)
# print(conjunto)
# print(type(conjunto))

# lista = [True, False, 0, 1,1,1,0,0,1,0,1,0]
# conjunto = set(lista)
# print(conjunto)
# print(type(conjunto))

# print ("Conjunto por comprensión")
# conjunto = {x for x in '🍕🍔🍟🍕🍔🍟🍔🍟'}
# print(conjunto)
# print(type(conjunto))

# Los conjuntos no soportan indexacion ni slicing
conjunto = {1, 2, 3, 4, 5}
#print(conjunto[0]) # TypeError: 'set' object is not subscriptable

conjunto = {1, 2, 3, 4, 5}
#print(conjunto[0:3]) # TypeError: 'set' object is not subscriptabl

# los conjuntos no soportan la concatenacion '+'
conjunto1 = {1, 2, 3}
conjunto2 = {4, 5, 6}
#print(conjunto1 + conjunto2)

# no soportan la repeticion con '*'
conjunto = {1, 2, 3}
#print(conjunto * 3)

# print ("Método add()")
# conjunto = {'🍕','🍔','🍟','🌭'}
# print (conjunto)
# conjunto.add('🥗')
# print(conjunto)

# print ("Método update()")
# conjunto = {'🍕','🍔','🍟','🌭'}
# print (conjunto)
# conjunto.update(['🥤','🍦'])
# print(conjunto)
# conjunto.update('🍩🍪')
# print(conjunto)
# conjunto.update(('🍫','🍬'))
# print(conjunto)
# conjunto.update({'🍭','🍮'})
# print(conjunto)

# print ("Método remove()")
# conjunto = {'🍕','🍔','🍟','🌭'}
# print (conjunto)
# conjunto.remove('🍔')
# print(conjunto)
# #conjunto.remove('🍔')
# #print(conjunto)
# # Key Error: '🍔'
# si no existe el elemento a borrar => hay error

# # si hay error igual lo ejecuta
# print ("Método discard()")
# conjunto = {'🍕','🍔','🍟','🌭'}
# print (conjunto)
# conjunto.discard('🍔')
# print(conjunto)
# conjunto.discard('🍔')
# print(conjunto)

# # elimina aleatoriamente un elemento del conjunto y lo retorna
# print ("Método pop()")
# conjunto = {'🍕','🍔','🍟','🌭', '🥤','🍦'}
# print (conjunto)
# print(conjunto.pop())
# print(conjunto)
# print(conjunto.pop())
# print(conjunto)
# retorno = conjunto.pop()
# print(retorno)
# print(conjunto)

# # elimina todos los elementos del conjunto
# print ("Método clear()")
# conjunto = {'🍕','🍔','🍟','🌭'}
# print (conjunto)
# conjunto.clear()
# print(conjunto)

# print ("Método union()")
# conjunto1 = {'🍔','🍟', '🥤'}
# conjunto2 = {'🍕','🍨','🥤'}
# print (conjunto1, conjunto2)

# union = conjunto1.union(conjunto2)
# print(union)

# # contiene los elem que estan en ambos conjuntos
# print ("Método intersection()")
# conjunto1 = {'🍔','🍟', '🥤'}
# conjunto2 = {'🍕','🍨','🥤'}
# print (conjunto1, conjunto2)

# interseccion = conjunto1.intersection(conjunto2)
# print(interseccion)

# # Los que están en el 1er conjunto pero no en el 2do
# print ("Método difference(), importa el orden")
# conjunto1 = {'🍔','🍟', '🥤'}
# conjunto2 = {'🍕','🍨','🥤'}
# print ("1:",conjunto1, "2:",conjunto2)
# diferencia = conjunto1.difference(conjunto2)
# print("1 y 2:",diferencia)
# diferencia = conjunto2.difference(conjunto1)
# print("2 y 1:",diferencia)

# # Contiene los elementos que están en un conjunto
# #  o en el otro pero no en ambos  =>  complemento de la interseccion
# print ("Método symmetric_difference()")
# conjunto1 = {'🍔','🍟', '🥤'}
# conjunto2 = {'🍕','🍨','🥤'}
# print (conjunto1, conjunto2)
# diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
# print(diferencia_simetrica)

# # MÉTODOS DE ASIGNACIÓN CON OPERACIONES.- Permiten realizar operaciones
# #  con conjuntos y asignar el resultado al conjunto inicial
# print ("Método intersection_update()")
# conjunto1 = {'🍔','🍟', '🥤'}
# conjunto2 = {'🍕','🍨','🥤'}
# print (conjunto1, conjunto2)
# conjunto1.intersection_update(conjunto2)
# print(conjunto1)

# print ("Método difference_update()")
# conjunto1 = {'🍔','🍟', '🥤'}
# conjunto2 = {'🍕','🍨','🥤'}
# print ("1:",conjunto1, "2:",conjunto2)
# conjunto1.difference_update(conjunto2)
# print ("1:",conjunto1, "2:",conjunto2)

# print ("Método symmetric_difference_update()")
# conjunto1 = {'🍔','🍟', '🥤'}
# conjunto2 = {'🍕','🍨','🥤'}
# print (conjunto1, conjunto2)
# conjunto1.symmetric_difference_update(conjunto2)
# print(conjunto1)

# # MÉTODOS DE BÚSQUEDA [54:40]
# print ("Método issubset()")
# conjunto1 = {'🍔','🍟', '🥤'}
# conjunto2 = {'🍕','🍨','🥤'}
# conjunto3 = {'🍔','🍟'}
# print (conjunto1, conjunto2,conjunto3)
# # ¿El conjunto1 es subconjunto del conjunto2?  => F
# print(conjunto1.issubset(conjunto2))
# # ¿El conjunto3 es subconjunto del conjunto1?  => V
# # Todos loe elem de conjunto3 estan en el conjunto1
# print(conjunto3.issubset(conjunto1))

# # EL ORDEN IMPORTA
# # ¿El conjunto1 es subconjunto del conjunto3?  =>F
# print(conjunto1.issubset(conjunto3))


# print ("Método issuperset()")
# conjunto1 = {'🍔','🍟', '🥤'}
# conjunto2 = {'🍕','🍨','🥤'}
# conjunto3 = {'🍔','🍟'}
# print (conjunto1, conjunto2,conjunto3)
# # ¿El conjunto1 es superconjunto del conjunto2?
# print(conjunto1.issuperset(conjunto2)) # C1 contiene a C2?

# # ¿El conjunto1 es superconjunto del conjunto2?
# print(conjunto1.issuperset(conjunto3)) # C1 contiene a C3?

# print ("Método isdisjoint()")
# conjunto1 = {'🍔','🍟', '🥤'}
# conjunto2 = {'🍕','🍨'}
# conjunto3 = {'🍔','🍟'}
# print (conjunto1, conjunto2,conjunto3)

# # ¿El conjunto1 no tiene elementos en común con el conjunto2?
# print(conjunto1.isdisjoint(conjunto2))  # AMBOS SON DISTINTOS?

# # ¿El conjunto1 no tiene elementos en común con el conjunto3?
# print(conjunto1.isdisjoint(conjunto3))   # HAY 2 ELEM EN COMUN

# # MÉTODOS DE COPIA

# print ("Asignación por referencia")
# conjunto = {'🍕','🍔','🍟','🌭'}
# print (conjunto)
# copia = conjunto
# copia.add('🥗')
# print(conjunto)
# print(copia)
# # ambos son iguales => apuntan a la misma direccion de memoria

# # Para crear una copia de un conjunto
# print ("Método copy()")
# conjunto = {'🍕','🍔','🍟','🌭'}
# print (conjunto)
# copia = conjunto.copy()  # esta en otra dir de memoria
# copia.add('🥗')
# print(conjunto)
# print(copia)

# # FUNCIONES CON CONJUNTOS
# print ("Función len()")
# conjunto = {'🍕','🍔','🍟','🌭'}
# print (conjunto)
# print(len(conjunto))

# print ("Función max()")
# conjunto = {1, 2, 3, 4, 5}
# print (conjunto)
# print (max(conjunto))

# conjunto = {'🍕','🍔','🍟','🌭'}
# print (conjunto)
# print(max(conjunto))

# print ("Función min()")
# conjunto = {1, 2, 3, 4, 5}
# print (conjunto)
# print (min(conjunto))
# conjunto = {'🍨','🍔','🍟','🍕'}
# print (conjunto)
# print(min(conjunto))

# print ("Función sum(), SOLO NROS")
# conjunto = {1, 2, 3, 4, 5}
# print (conjunto)
# print (sum(conjunto))

# OPERADORES CON CONJUNTOS
# Los conjuntos soportan operadores que permiten realizar operaciones

# print ("Operador |=")
# conjunto1 = {'🍔','🍟', '🥤'}
# conjunto2 = {'🍕','🍨'}
# print (conjunto1, conjunto2)

# # lo del conjunto2 pasarlo al conjunto1
## conj1 UNION conj2 y pasarlo al conj1
# conjunto1 |= conjunto2
# print(conjunto1)

# # solo el pipe | significa union
# conjunto3 = conjunto1 | conjunto2
# print(conjunto3)

# # OPERADORES DE COMPARACION
# print ("Operador ==")
# conjunto1 = {'🍔','🍟', '🥤'}
# conjunto2 = {'🍔','🍟', '🥤'}
# conjunto3 = {'🍕','🍨'}
# print (conjunto1, conjunto2, conjunto3)
# print(conjunto1 == conjunto2)
# print(conjunto1 == conjunto3)

# print ("Operador !=")
# conjunto1 = {'🍔','🍟', '🥤'}
# conjunto2 = {'🍔','🍟', '🥤'}
# conjunto3 = {'🍕','🍨'}
# print (conjunto1, conjunto2, conjunto3)
# print(conjunto1 != conjunto2)
# print(conjunto1 != conjunto3)

# print ("Operador < , es subconjunto y no igual?")
# conjunto1 = {'🍔','🍟'}
# conjunto2 = {'🍔','🍟', '🥤'}
# conjunto3 = {'🍕','🍨'}
# print (conjunto1, conjunto2, conjunto3)
# print(conjunto1 < conjunto2)  # conj1 cabe en el conj2
# print(conjunto1 < conjunto3)

# conjunto1 = {'🍔','🍟'}
# conjunto2 = {'🍔','🍟'}
# print(conjunto1 < conjunto2)  # es False

# print ("Operador >, es superconj y no igual a otro")
# conjunto1 = {'🍔','🍟','🥤','🍕'}
# conjunto2 = {'🍔','🍟', '🥤'}
# conjunto3 = {'🍕','🍨'}
# print (conjunto1, conjunto2, conjunto3)
# print(conjunto1 > conjunto2)  # conj1  contiene al conj2
# print(conjunto1 > conjunto3)

# print ("Operador <=")
# conjunto1 = {'🍔','🍟'}
# conjunto2 = {'🍔','🍟'}
# conjunto3 = {'🍕','🍨'}
# print (conjunto1, conjunto2, conjunto3)
# print(conjunto1 <= conjunto2)
# print(conjunto1 <= conjunto3)

# print ("Operador >=")
# conjunto1 = {'🍔','🍟'}
# conjunto2 = {'🍔','🍟'}
# conjunto3 = {'🍕','🍨'}
# print (conjunto1, conjunto2, conjunto3)
# print(conjunto1 >= conjunto2)
# print(conjunto1 >= conjunto3)

# # OPERADORES PARA OPERACIONES CON CONJUNTOS:  |  &  -  ^
# print ("Operador |")
# conjunto1 = {'🍔','🍟', '🥤'}
# conjunto2 = {'🍕','🍨','🥤'}
# print (conjunto1, conjunto2)
# union = conjunto1 | conjunto2
# print(union)

# print ("Operador &")
# conjunto1 = {'🍔','🍟', '🥤'}
# conjunto2 = {'🍕','🍨','🥤'}
# print (conjunto1, conjunto2)
# interseccion = conjunto1 & conjunto2
# print(interseccion)

# print ("Operador - ,  retorna la diferencia")
# conjunto1 = {'🍔','🍟', '🥤'}
# conjunto2 = {'🍕','🍨','🥤'}
# print ("1:",conjunto1, "2:",conjunto2)
# diferencia = conjunto1 - conjunto2
# print("1 - 2:",diferencia)
# diferencia = conjunto2 - conjunto1
# print("2 - 1:",diferencia)

# print ("Operador ^ , return la dif simetrica")
# conjunto1 = {'🍔','🍟', '🥤'}
# conjunto2 = {'🍕','🍨','🥤'}
# print (conjunto1, conjunto2)
# diferencia_simetrica = conjunto1 ^ conjunto2
# print(diferencia_simetrica)
# # los iguales  => descartarlo de la union

# OPERADORES PARA ASIGNACIÓN CON OPERACIONES
# |=   &=    -=    ^=
# opera con conjuntos y ASIGNA EL RESULTADO AL conjunto inicial
# print ("Operador |= Unión")
# conjunto1 = {'🍔','🍟', '🥤'}
# conjunto2 = {'🍕','🍨','🥤'}
# print (conjunto1, conjunto2)
# conjunto1 |= conjunto2
# print(conjunto1)

# print ("Operador &= Intersección")
# conjunto1 = {'🍔','🍟', '🥤'}
# conjunto2 = {'🍕','🍨','🥤'}
# print (conjunto1, conjunto2)
# conjunto1 &= conjunto2
# print(conjunto1)

# print ("Operador -= Diferencia")
# conjunto1 = {'🍔','🍟', '🥤'}
# conjunto2 = {'🍕','🍨','🥤'}
# print ("1:",conjunto1, "2:",conjunto2)
# conjunto1 -= conjunto2
# print("1 - 2:",conjunto1)
# conjunto1 = {'🍔','🍟', '🥤'}
# conjunto2 -= conjunto1
# print("2 - 1:", conjunto2)

# print ("Operador ^= Diferencia simétrica")
# conjunto1 = {'🍔','🍟', '🥤'}
# conjunto2 = {'🍕','🍨','🥤'}
# print (conjunto1, conjunto2)
# conjunto1 ^= conjunto2
# print(conjunto1)


# # CONJUNTOS INMUTABLES.- q no pueden ser modificados con frozenset()
# conjunto = frozenset({'🍔','🍕','🥗','🍟','🌭'})
# print(conjunto)
# print(type(conjunto))

# # No poseen adicion, eliminacion y asignacion
# conjunto = frozenset({1, 2, 3, 4, 5})
# print(conjunto)
# #print(conjunto.add(6)) # AttributeError: 'frozenset' object has no attribute 'add'
# #print(conjunto.remove(1)) # AttributeError: 'frozenset' object has no attribute 'remove'
# #print(conjunto |= {6}) # SyntaxError: invalid syntax

# # CONJUNTOS ANIDADOS.- conjuntos q contienen otros conjuntos
# # PERO tienen que ser inmutables para ser anidados
# print ("Conjunto de conjuntos")
# conjunto = {frozenset({'🍅','🍓','🍎'}), frozenset({'🍈','🍐','🍏'})}
# print(conjunto)
# print(type(conjunto))

# # conjunto de conjunto => ERRROR
# #conjunto = {{'🍅','🍓','🍎'}, {'🍈','🍐','🍏'}}

# print ("Conjunto de conjuntos")
# conjunto = {{'🍅','🍓','🍎'}, {'🍈','🍐','🍏'}} #TypeError: unhashable type: 'set'
# print(conjunto)
# print(type(conjunto))