# 5.- Un usuario ingresa su nombre y gustos musicales por teclado
# separados por coma, verifica si el usuario ingresó un nombre válido
# usando truthiness, convertir los gustos musicales en una lista
# y verifica si tiene el gusto rock en su lista de gustos musicales

nombre = input("Digite su nombre: ")
gustos = input("Gustos musicales: ")

if nombre:
    nombre2 = nombre.split(" ")
    soloNombre = "".join(nombre2)
    if soloNombre.isalpha():
        print(f"Nombre: {nombre}")
    else:
        print("Nombre no valido")
else:
    print("Sin datos, digite su nombre")

if gustos:
    lista = gustos.split(",")
    print(f"Gustos musicales: {lista}")
    if 'rock' in lista:
        print("Tiene como gusto musical al rock")
    else:
        print("No le gusta el rock")
    
else:
    print("Sin datos, digite sus gustos musicales")
