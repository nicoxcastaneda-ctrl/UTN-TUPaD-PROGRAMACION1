print("--- BIENVENIDO A LA ARENA ---")

while True:

    nombre = input("Ingrese nombre del gladiador: ")

    if not nombre.isalpha():
        print("Error: Solo se permiten letras.")
        
    else:
        break

vida_jugador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado = 15
danio_enemigo = 12
turno_gladiador = True

print("=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:
    print("=================================================================================")
    print(f"{nombre} HP: {vida_jugador} VS Enemigo HP: {vida_enemigo} | Pociones: {pociones}")
    print("=================================================================================")

    print()
    print("Elige accion:")
    print("1. Ataque Pesado")
    print("2. Rafaga Veloz")
    print("3. Curar")

    while True:

        opcion = input("Opcion: ")
        
        if not opcion.isdigit():
            print("Error: Ingrese un numero valido.")
            
        else:
            opcion = int(opcion)

            if opcion < 1 or opcion > 3:
                print("Error: Opcion fuera de rango.")
                opcion = input("Opcion: ")
            else:
                break

    if opcion == 1:

        danio = ataque_pesado

        if vida_enemigo < 20:
            danio = ataque_pesado * 1.5
            print("¡GOLPE CRITICO!")

        vida_enemigo = vida_enemigo - danio

        print("¡Atacaste al enemigo por", danio, "puntos de daño!")

    elif opcion == 2:

        print(">> ¡Inicias una rafaga de golpes!")

        for i in range(3):
            vida_enemigo = vida_enemigo - 5
            print("> Golpe conectado por 5 de daño")

    elif opcion == 3:

        if pociones > 0:
            vida_jugador = vida_jugador + 30

            if vida_jugador > 100:
                vida_jugador = 100

            pociones = pociones - 1

            print("¡Te has curado 30 puntos de vida!")

        else:
            print("¡No quedan pociones!")

    if vida_enemigo <= 0:
        break

    vida_jugador = vida_jugador - danio_enemigo

    print("¡El enemigo te atacó por 12 puntos de daño!")

if vida_jugador > 0:
    print("¡VICTORIA!", nombre, "ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")