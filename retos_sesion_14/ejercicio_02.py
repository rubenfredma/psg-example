# Calculadora flexible: Crea una calculadora que acepte diferentes 
# operaciones matemáticas como argumentos de palabras clave y 
# realice los cálculos correspondientes, las operaciones son suma, resta,
# multiplicación y división


def calcular(n1,n2,*args):
    resultado=""

    lista = list(args)
    for operacion in lista:
        if operacion == "suma":
            sum = n1+n2
            resultado += f"Suma = {sum}\n"
            #+= f"{str(clave).title()}: {str(valor).upper()}\n"
        elif operacion == "resta":
            res = n1-n2
            resultado += f"Resta = {res}\n"
        elif operacion == "multiplicacion":
            mul = n1*n2
            resultado += f"Producto = {mul}\n"
        elif operacion == "division":
            div = n1/n2
            resultado += f"Division = {div}\n"
        else:
            resultado += f"Operacion no permitida"

    return resultado


op = calcular(10,5,'resta','division','hola')
print(op)
