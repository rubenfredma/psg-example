# Simular un tres en raya con funciones donde reciba las jugadas 
# y devuelva el ganador hasta que alguien ingrese salir

import random
import os

def inicializar_juego():
    """Función que incializa los valores del juego"""
    juego_en_curso = True
    #jugadores = [[input("Jugador 111: "),"X"], [input("Jugador 222: "),"O"]]
    jugadores = [["Jugador X","X"], ["Jugador O","O"]]
    jugador_actual = random.randint(0, 1)
    tablero = [["-","-","-"],["-","-","-"],["-","-","-"]]
    
    #print(jugadores)

    return juego_en_curso, jugadores, jugador_actual, tablero

def actualizar_tablero(jugador, coordenada_fila, coordenada_columna, tablero_actual):
    if str(coordenada_fila) not in '123' or str(coordenada_columna) not in '123':
        print("datos incorrectos")
        
    """Actualiza el tablero con la acción del jugador actual"""
    tablero_actual[coordenada_fila - 1][coordenada_columna - 1] = jugador[1]
    return tablero_actual

def tablero_completo(tablero_actual):
    """Comprueba si el tablero está completo, devuelve True o False"""
    for linea in tablero_actual:
        for celda in linea:
            if celda == '-':
                return False
    return True

def comprobar_ganador(jugador, tablero_actual):
    """Comprueba si ha ganado el jugador actual, devuelve True o False"""
    #Comprobar por filas
    for i in range(3):
        ganador = True
        for x in range(3):
            if tablero_actual[i][x] != jugador[1]:
                ganador = False
                break
        if ganador:
            return ganador
    #Comprobar por columnas
    for i in range(3):
        ganador = True
        for x in range(3):
            if tablero_actual[x][i] != jugador[1]:
                ganador = False
                break
        if ganador:
            return ganador
    #Comprobar por diagonales
    ganador = True
    for i in range(3):
        if tablero_actual[i][i] != jugador[1]:
            ganador = False
            break
    if ganador:
        return ganador
    ganador = True
    for i in range(3):
        if tablero_actual[i][3 - 1 - i] != jugador[1]:
            ganador = False
            break
    if ganador:
        return ganador
    
    return False

print(f"Juegan: Jugador X  y Jugador 0")
juego_en_curso, jugadores, jugador_actual, tablero = inicializar_juego()

while juego_en_curso:
    if tablero_completo(tablero):
        juego_en_curso = False
        #os.system("cls")
        
        print("Fin del juego, no hay ganador")
        break

    #os.system("cls")
    #Nuevo turno
    print("Turno de: " + jugadores[jugador_actual][0])
    
    #Dibujar tablero
    print("0 1 2 3")
    coordenadas_vertical = 1
    for linea in tablero:
        print(coordenadas_vertical, linea[0], linea[1], linea[2])
        coordenadas_vertical += 1
    
    #Selección de casilla
    #coordenada_fila, coordenada_columna = list(map(int, input("Elige coordenadas nn, n entre 1 y 3: ")))
    datos = input("Elige coordenadas entre 1 y 3 [n,n]: ")
    if ',' in datos:   
        entradas = datos.split(",")
        coordenada_fila = int(entradas[0])
        coordenada_columna = int(entradas[1])
    elif datos == "salir":
        print("Termino el juego")
        break
    else:
        print("Falla en la entrada de datos, termino el juego")
        break

    #Actuaizar tablero
    tablero = actualizar_tablero(jugadores[jugador_actual], coordenada_fila, coordenada_columna, tablero)
    
    #Comprobamos si ha ganado
    if comprobar_ganador(jugadores[jugador_actual], tablero):
        juego_en_curso = False
    
        #Dibujar tablero
        os.system("cls")
        print("0 1 2 3")
        coordenadas_vertical = 1
        for linea in tablero:
            print(coordenadas_vertical, linea[0], linea[1], linea[2])
            coordenadas_vertical += 1
        print("Ganador: ",jugadores[jugador_actual][0])

    #Cambio de jugador
    jugador_actual = 1 if jugador_actual == 0 else 0



