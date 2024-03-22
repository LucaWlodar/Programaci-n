# print("Hola usuarios")
# j1 = input("Jugador 1 porfavor ingrese su nombre\n")
# fig1 = str(input("Ingrese la figura a usar(X-O)"))
# while (fig1=="X" or "O"):
#     j2 = input("Jugador 2 porfavor ingrese su nombre\n")
#     break
def imprimir_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-" * 5)

def verificar_ganador(tablero, jugador):
    # Verificar filas y columnas
    for i in range(3):
        if all(tablero[i][j] == jugador for j in range(3)) or all(tablero[j][i] == jugador for j in range(3)):
            return True

    # Verificar diagonales
    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2 - i] == jugador for i in range(3)):
        return True

    return False

def juego():
    tablero = [[" "]*3 for _ in range(3)]
    nombres = [input("Nombre del jugador 1: "), input("Nombre del jugador 2: ")]
    fichas = [input(f"{nombres[0]}, ¿quieres jugar con 'X' o 'O'? ").upper(), '']
    
    while fichas[0] not in ('X', 'O'):
        fichas[0] = input("Por favor, selecciona 'X' o 'O' para el jugador 1: ").upper()

    fichas[1] = 'X' if fichas[0] == 'O' else 'O'
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
            elif all(cell != " " for row in tablero for cell in row):
                imprimir_tablero(tablero)
                print("¡El juego ha terminado en empate!")
                break
            turno += 1
        else:
            print("Esa posición ya está ocupada. Intente nuevamente.")

juego()


