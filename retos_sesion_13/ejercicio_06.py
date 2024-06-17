# Crea un ciclo infinito que reciba un número por teclado y verifique
# si es un número primo, termina la ejecución si se ingresa el número 0

while True:
    nro = int(input("Ingrese un numero: "))
    if nro == 0:
        break
    else:
        primo=0
        for i in range(2,nro+1):
            if nro%i == 0:
                primo += 1

        if primo == 1:
            print(f"{nro} es numero primo")
        else:
            print(f"{nro} no es numero primo")

print ("Fin")


primo=0
for i in range(2,nro+1):
    if nro%i == 0:
        primo += 1

if primo == 1:
    print("primo")
else:
    print("no es primo")