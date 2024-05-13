# Comparar los numeros 123 y 890, comprobar si tienen
# la misma paridad, ambos pares o ambos impares

num1 = 123
num2 = 890
print("Ambos nros son pares o impares:")
print(((num1 % 2)==0 and (num2 % 2)==0) or ((num1 % 2)==1 and (num2 % 2)==1))