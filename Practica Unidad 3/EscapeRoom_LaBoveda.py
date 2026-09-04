print("=== Historia ===")
print("Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo limitados.")
print("Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.")
nombre_agente = ""
while True:
    print()
    nombre_agente = input("Ingrese nombre de Agente: ")
    print()

    if not nombre_agente.isalpha():
        print(">>(!)Error: Solo letras.")

    else:
        nombre_agente = str(nombre_agente)

        if len(nombre_agente) <= 3:
            print(">>(!)Error: Mínimo 4 letras.")
        else:
            break

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

intentos_forzar = 0
estado_alarma = ""
print(f"Bienvenido agente {nombre_agente}.")
print("----------------------------------")
print("=== COMIENZA EL JUEGO ===")

while True:
    if alarma:
        estado_alarma = "Activada"
    else:
        estado_alarma = "Desactivada"
    print("=== ESTADÍSTICAS ===")
    print(f">> Tiempo restante: {tiempo}")
    print(f">> Energía restante: {energia}")
    print(f">> Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f">> Estado de la alarma: {estado_alarma}")
    print("\n")
    print("=== MENÚ DE OPCIONES ===")
    print("1- FORZAR CERRADURA.")
    print("2- HACKEAR PANEL.")
    print("3- DESCANSAR.")

    opcion = input("Qué movimiento desea hacer?: ")
    print("\n")

    if not opcion.isdigit():
        print(">>(!)Error: Solo número.")
    else:
        opcion = int(opcion)

        if opcion == 1:
            intentos_forzar += 1
            energia -= 20
            tiempo -= 2
            if intentos_forzar == 3:
                print("¡CERRADURA TRABADA, LA ALARMA HA SIDO ACTIVADA!")
                alarma = True
            else:
                cerraduras_abiertas += 1
                print(">> HAS ABIERTO UNA CERRADURA. SIGUE ASÍ.")
            if energia <= 40 and alarma == False:
                print("¡¡¡¡RIESGO DE ALARMA!!!!")

                while True:
                    numero = input(">>¡Escoja un número entre 1 y 3 para ver si se activa!: ")

                    if not numero.isdigit():
                        print(">>(!)Error: Debe ser número.")
                    else:
                        numero = int(numero)

                        if numero == 3:
                            print("¡¡¡MALA SUERTE, ACTIVASTE LA ALARMA!!!!")
                            alarma = True
                            break
                        elif numero == 1 or numero == 2:
                            print(">> SALVADO, CONTINUA..")
                            break
                        else:
                            print(">>(!)Error: Número fuera de rango.")

        elif opcion == 2:
            energia -= 10
            tiempo -= 3
            intentos_forzar = 0

            for i in range(4):
                print("Hackeando... letra  conseguida.")
                codigo_parcial += "A" 

            if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print(">> ¡Has completado el código!")
                print(">> !Abriste una cerradura!")
                codigo_parcial = ""
            else:
                print(">> ¡Has sumado letras al codigo, ya casi puedes abrir una cerradura!")

        elif opcion == 3:
            energia += 15
            tiempo -= 1
            intentos_forzar = 0

            if energia > 100:
                energia = 100

            if alarma == True:
                print(">> Descansas con alarma activada. Pierdes 10 de energía.")
                energia -= 10

        else:
            print(">>(!)Error: Fuera de rango.")

    if energia <= 0 or tiempo <= 0:
        print("\n")
        print("=== HAS PERDIDO ===")
        print("Te has quedado sin recursos.")
        break

    if alarma == True and tiempo <= 3:
        print("=== HAS PERDIDO ===")
        print("Energía muy baja y alarma activada.")
        print("La bóveda se ha bloqueado de forma permanente!")
        break

    if cerraduras_abiertas == 3:
        print("=== HAS GANADO ===")
        print("Has abierto todas las cerraduras.")
        break
if alarma:
    estado_alarma = "Activada"
else:
    estado_alarma = "Desactivada"
print("======================")
print(" ESTADISTICAS FINALES ")
print("======================")

print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
print(f"Alarma: {estado_alarma}")
print(f"Energía {energia}")
print(f"Tiempo: {tiempo}")