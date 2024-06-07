# 4.- Una tienda ofrece descuentos a sus clientes, si el cliente 
# es mayor de edad y tiene una compra mayor a 1000, 
# se le aplica un descuento del 10%, 
# si es menor de edad y tiene una compra mayor a 500 
# se le aplica un descuento del 5%, 
# si no cumple ninguna condición se le aplica un descuento del 2%

cliente_edad = 17
compra = 100
compra_total = 0

if cliente_edad >=18 and compra > 1000:
    compra_total = compra - (compra*0.1)
elif cliente_edad < 18 and compra > 500:
    compra_total = compra - (compra*0.05)
else:
    compra_total = compra - (compra*0.02)

print(f"Compra total = {compra_total} Bs")