# Dos mochileros se encuentran en el Salar de Uyuni y se ponen a comparar 
# la cantidad de lugares que han visitado
# Cada uno quiere saber en que parte del mundo ha estado el otro 
# que el no haya visitado

mochilero_a = {"París", "Londres", "Nueva York", "Tokio","Peru", "Chile", "Colombia", "Bolivia"}
mochilero_b = {"Londres", "Roma", "Nueva York", "Sidney","Argentina","Brasil","Panama","Bolivia"}

diferencia1 = mochilero_a.difference(mochilero_b)
print("Paises que el mochilero_a a visitado y el mochilero_b no ha estado:")
print(diferencia1)
print("----------------")
diferencia2 = mochilero_b.difference(mochilero_a)
print("Paises que el mochilero_b a visitado y el mochilero_a no ha estado:")
print(diferencia2)

