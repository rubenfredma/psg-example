# Crea un ciclo infinito que reciba una palabra por teclado 
# y verifique si es palíndrome, termina la ejecución 
# si se ingresa la palabra salir

while True:
    palabra = input("Ingrese una palabra: ")
    if palabra == 'salir':
        break
    
    palabra_junto=""
    for c in range(0,len(palabra)):
        if palabra[c] != " ":
            palabra_junto += palabra[c]
    palabra_inv = ""
    for c in range(len(palabra_junto)-1, -1, -1):
        palabra_inv += palabra_junto[c]

    if palabra_junto == palabra_inv:
        print(f"{palabra}, es palindrome")
    else:
        print(f"{palabra}, NO es palindrome")

print ("Fin")
