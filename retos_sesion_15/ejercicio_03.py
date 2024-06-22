# Simular un cajero automático que solicite un monto a retirar, 
# si el monto es mayor al saldo lanzar una excepción personalizada 
# y si el monto es mayor a 1000 lanzar una excepción genérica

import random
saldo = random.randint(100,2000)

print("----------------------------")
print("----Cajero Automatico-------")
print("----------------------------")
try:
    monto = float(input("Digite el monto a retirar Bs: "))

    if monto > 1000:
        ress = monto/0
    elif monto > saldo:
        raise Exception(f"Su saldo = {saldo} Bs. Y no puede retirar {monto} Bs")

except Exception as e: # Captura cualquier excepción
    print("💀 Error:", e)
else:
    print ("🎉 Transaccion realizada")
