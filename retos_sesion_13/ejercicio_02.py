# Imprimir los 20 primeros números primos

cont = 1
nro = 2
while cont <= 20:
    
    primo=0
    for i in range(2,nro+1):
        if nro%i == 0:
            primo += 1

    if primo == 1:
        print(nro, end=", ")
        cont += 1
        
    nro = nro + 1
    


