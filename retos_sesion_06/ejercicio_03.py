# Imprime una tabla de verdad para la siguiente afirmacion: 
# "Una puerta tiene dos interruptores que controlan dos luces, la puerta
# solo debe abrirse cuando las dos luces estan apagadas o las dos luces estan
# encendidas, caso contrario la puerta no se abre, 
# ¿Que operador logico se puede utilizar?"

print("  TABLE DE VERDAD DEL OPERADOR XNOR =========")
encendido = True
apagado = True
print ("encendido and encendido", " = ","La puerta se abre:",not((encendido or apagado) and not(encendido and apagado)))

encendido = False
apagado = False
print ("apagado and apagado", " = ","La puerta se abre:",not((encendido or apagado) and not(encendido and apagado)))

encendido = True
apagado = False
print ("encendido and apagado", " = ","La puerta se abre:",not((encendido or apagado) and not(encendido and apagado)))

encendido = False
apagado = True
print ("apagado and encendido", " = ","La puerta se abre:",not((encendido or apagado) and not(encendido and apagado)))
