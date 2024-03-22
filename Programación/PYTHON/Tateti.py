def imprimir_tablero(tablero):
    for fila in tablero:
        print("|".join(fila)) 
        print("-" * 5)

def verificar_ganador(tablero, jugador):
    for i in range(3):
        if (tablero[i][0] == tablero[i][1] == tablero[i][2] == jugador or
            tablero[0][i] == tablero[1][i] == tablero[2][i] == jugador):
            return True

    if (tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador or
        tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador):
        return True

    return False

def juego():
    tablero = [[" "]*3 for _ in range(3)]

    nombres = [input("Nombre del jugador 1: "), input("Nombre del jugador 2: ")]
    fichas = [input(f"{nombres[0]}, ¿quieres jugar con 'X' o 'O'? ")]

    while fichas[0] != 'X' and fichas[0] != 'O':
        fichas[0] = input("Por favor, selecciona 'X' o 'O' para el jugador 1: ")

    fichas.append('X' if fichas[0] == 'O' else 'O')
    turno = 0

    while True:
        imprimir_tablero(tablero)
        jugador_actual = nombres[turno % 2]
        ficha_actual = fichas[turno % 2]
        print(f"Turno de {jugador_actual} ({ficha_actual})")

        fila = int(input("Ingrese el número de fila (0, 1, 2): "))
        columna = int(input("Ingrese el número de columna (0, 1, 2): "))

        if tablero[fila][columna] == " ":
            tablero[fila][columna] = ficha_actual
            if verificar_ganador(tablero, ficha_actual):
                imprimir_tablero(tablero)
                print(f"¡{jugador_actual} ha ganado!")
                break
            elif all(" " not in fila for fila in tablero):
                imprimir_tablero(tablero)
                print("¡El juego ha terminado en empate!")
                break
            turno += 1
        else:
            print("Esa posición ya está ocupada. Intente nuevamente.")

juego()
