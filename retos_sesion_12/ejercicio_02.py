# 2.- Tienes una página web y un usuario quiere acceder a ella, 
# verifica si el usuario inició sesión para acceder a la página, 
# caso contrario muestra un mensaje de error

sesion = '12345'
clave = input("Digite la clave para acceder a la pagina: ")

if clave == sesion:
    print("Sesion correcta, acceso a la pagina")
else:
    print("Error digite un valor correcto, para iniciar sesion")


