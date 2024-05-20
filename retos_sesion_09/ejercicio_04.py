# Tienes una tienda de abarrotes y tienes dos listas una 
# con los productos que tienes y otra con los precios

productos = ["Azuccar","Cafe", "Pan","Papel higienico"]
precios = [3, 2, 0.50, 10]
print(productos)
print(precios)

print("------------------")
#   1 Agregar 5 productos nuevos al final de las listas 
productos.append("Leche")
precios.append(6)
productos.append("Aceite")
precios.append(10)
productos.append("Huevo")
precios.append(1)
productos.append("Fideos")
precios.append(5)
productos.append("Pepsi cola")
precios.append(11)

print(productos)
print(precios)

#   2 Eliminar el producto con el nombre "Leche" de las listas
print("")
valor = "Leche"
posicion = productos.index(valor)
print("Eliminando el producto:", valor)
productos.pop(posicion)
precios.pop(posicion)
print(productos)
print(precios)

#   3 ¿Cuanto cuesta el producto "Pan" y "Huevo"?
print("")
index_pan = productos.index("Pan")
index_huevo = productos.index("Huevo")
precio_pan = precios[index_pan]
precio_huevo = precios[index_huevo]

print(f"El pan cuesta {precio_pan} bs")
print(f"El huevo cuesta {precio_huevo} bs.")


#   4 ¿Cual es el producto más caro y más barato?
print("")
mayor = max(precios)
menor = min(precios)
index_max = precios.index(mayor)
index_min = precios.index(menor)
producto_caro = productos[index_max]
producto_barato = productos[index_min]
print(f"El producto mas caro es: {producto_caro}")
print(f"El producto mas barato es: {producto_barato}")

#   5 ¿Cuántos productos tienes en total?
print(f"Total de productos: {len(productos)}")

#   6 ¿Cuanto cuesta el total de los productos?
print(f"El total productos cuesta: {sum(precios)} bs.")

#   7 Ordena los productos alfabéticamente y precios si es posible
print("")
productos.sort()
print(productos)

#   8 Eliminar todos los productos de las listas
productos.clear()
precios.clear()
print(productos)
print(precios)
