# Crea una calculadora por consola que realice las operaciones de suma,
# resta, multiplicación y división, ingresa dos números 
# y la operación a realizar, verifica si la operación es válida 
# y muestra el resultado

num1 = input("Numero 1: ")
num2 = input("Numero 2: ")
operacion = input("Operacion: ")

if num1.isdigit() and num2.isdigit():
    #print("son numeros")
    if operacion in '+-*/':
        #print("operacion valida")
        if operacion=='+':
            resultado = int(num1)+int(num2)
        elif operacion == '-':
            resultado = int(num1)-int(num2)
        elif operacion == '*':
            resultado = int(num1)*int(num2)
        else:
            a = int(num1)
            b = int(num2)
            if b: 
                resultado = a/b
            else:
                resultado = "No se puede dividir entre cero"
        print("-----------------")
        print(f"Resultado: {resultado}")
    else:
        print("Operacion No valida")
else:
    print("ERROR, digite solo numeros")

