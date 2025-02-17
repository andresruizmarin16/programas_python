import random
print("¡Bienvenido al Piedras, Papel o Tijeras!\n Introduce la posición que aparece en pantalla para tu elección")
n_victorias = 0
n_derrotas = 0
n_empate = 0
while True:
    eleccion_jugador = int(input("Introduce tu eleccion: \n1.Piedra\n2.Papel\n3.Tijera "))
    eleccion_ia = random.randint(1,3)

    if eleccion_jugador == eleccion_ia:
        n_empate +=1
        print("¡Empate!")
    elif eleccion_jugador == 1 and eleccion_ia == 2:
        n_derrotas +=1
        print("¡Derrota!")
    elif eleccion_jugador == 2 and eleccion_ia == 3:
        n_derrotas +=1
        print("¡Derrota!")
    elif eleccion_jugador == 3 and eleccion_ia == 1:
        n_derrotas +=1
        print("¡Derrota!")
    elif eleccion_jugador == 2 and eleccion_ia == 1:
        n_victorias +=1
        print("Victoria!")
    elif eleccion_jugador == 3 and eleccion_ia == 2:
        n_victorias +=1
        print("Victoria!")
    elif eleccion_jugador == 1 and eleccion_ia == 3:
        n_victorias +=1
        print("¡Victoria!")
    else:
        print("Has introducido mal tu elección")
    decision_jugador = input("¿Quiere seguir jugando(s/n)?").lower()
    if decision_jugador == "n":
        break
    else:
        continue

print("Victorias:",n_victorias)
print("Derrota:",n_derrotas)
print("Empates:",n_empate)