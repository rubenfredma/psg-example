# Convertir a cuantos dias, horas, minutos y segundos
# corresponde la siguiente cantidad de segundos: 288325

# 1 dia = 86400 seg
# 1 hora = 3600 seg
# 1 min = 60 seg

segundos = 288325
dia = segundos//86400
segundos = segundos%86400

hora = segundos//3600
segundos = segundos%3600

min = segundos//60
segundos = segundos%60

print("En 288325 segundos hay:")
print(dia,"dias")
print(hora,"horas")
print(min,"minutos")
print(segundos,"segundos")
