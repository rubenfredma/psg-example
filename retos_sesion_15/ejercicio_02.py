# Crear un programa para crear una canasta de frutas, solicitar frutas
# por teclado y almacenar en una lista, si se ingresa "salir" 
# termina la ejecución. Solo se permiten las siguientes frutas 
# caso contrario lanzar una excepción personalizada
#  🍅🍇🍈🍉🍊🍌🍍🍑

frutas = []
while True:
    try:
        fruta = input("Ingrese una fruta: ")
        if fruta == "salir":
            break
        
        if fruta not in '🍅🍇🍈🍉🍊🍌🍍🍑':
            raise Exception(f"No se puede agregar esta fruta {fruta}")
        frutas.append(fruta)
    except KeyboardInterrupt as e:
        print('🚫 Para salir escriba "salir"')
    except Exception as e:
        print("💀 Error:", e)
    else:
        print("🎉 Fruta agregada")
    finally:
        print("Canasta:", frutas)
        