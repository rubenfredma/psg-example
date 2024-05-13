# Construir el operador XNOR en python

print("  OPERADOR XNOR  ---------")
a = True
b = False
print (not((a or b) and not(a and b)))
a = True
b = True
print (not((a or b) and not(a and b)))
