# El dueño de un restaurante de comida Mexicana ha decidido comprar
# un restaurante de comida Italiana y abrir un nuevo restaurante 
# de comida fusion. La apertura esta a la vuelta de la esquina 
# y aun no hay podido actualizar el Menu, Ayuda a actualizar su menu
# de platos disponibles
# menu_mexicano: "Tacos", "Enchiladas", "Guacamole", "Tamales"
# menu_italiano: "Pizza", "Pasta", "Lasagna", "Tiramisú"

menu_mexicano = {"Tacos", "Enchiladas", "Guacamole", "Tamales"}
menu_italiano = {"Pizza", "Pasta", "Lasagna", "Tiramisú" }
#print(menu_mexicano, menu_italiano)

menu_fusion = menu_mexicano.union(menu_italiano)
print(f"Menu fusion: {menu_fusion}")

