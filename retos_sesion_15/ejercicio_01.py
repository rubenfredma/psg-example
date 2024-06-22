# Crear una calculadora que solicite dos números y realice las operaciones
# básicas de suma, resta, multiplicación y división con manejo de excepciones, 
# para salir del programa se debe ingresar "salir"


def operaciones(numero1, numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2
    return (suma, resta, multiplicacion, division)

while True:
    try:
        num1 = input("Ingrese el primer número: ")
        if num1 == "salir":
            break
        num2 = input("Ingrese el segundo número: ")
        if num2 == "salir":
            break
        num1 = int(num1)
        num2 = int(num2)
        #resultado = division(num1, num2)
        #sum,res,mul,div = operaciones(num1, num2)
        sum = num1 + num2
        res = num1 - num2
        mul = num1 * num2
        div = num1 / num2

    except KeyboardInterrupt as e:
        print('🚫 Para salir escriba "salir"')
    except ZeroDivisionError as e:
        print("0️⃣ Error:", e, type(e))
    except Exception as e:
        print("💀 Error:", e)
    else:
        print(f"{num1}+{num2} = {sum}")
        print(f"{num1}-{num2} = {res}")
        print(f"{num1}x{num2} = {mul}")
        print(f"{num1}/{num2} = {div}")

