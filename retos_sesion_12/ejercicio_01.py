# 1.- Crear un script que pida un número entero y 
# verifique si es par o impar usando operador ternario

nro = int(input("Digite un numero: "))
resultado = "nro par" if  nro%2 == 0 else "nro impar"
print(f"El {nro} es {resultado}")
