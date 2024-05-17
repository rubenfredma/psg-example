# Escribe un programa que reciba una cadena y retorna verdadero o falso
# si es palindrome la frase o palabra, ejemplo "Anita lava la tina"  es verdad

frase = "Anita lava la Tina"
frase_sin_espacios = frase.strip()
frase_solo_letras = frase_sin_espacios.replace(" ","")
frase_minusculas = frase_solo_letras.lower()

cadena = frase_minusculas
cadena_inv = frase_minusculas[::-1]

#print(cadena, cadena_inv)
print(frase," ¿Es palindrome? :",(cadena == cadena_inv))