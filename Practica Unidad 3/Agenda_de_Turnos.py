print("=== AGENDA DE TURNOS ===")

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

nombre_operador = ""

while True:

    nombre_operador = input("Ingrese nombre de operador: ")

    if not nombre_operador.isalpha():
        print(">> (!)Error: Solo letras.")

    else:
        nombre_operador = str(nombre_operador)
        break

print(f">> Bienvenido {nombre_operador}.")

while True:

    print("   ==== MENÚ ====")
    print("1- Reservar turno.")
    print("2- Cancelar turno.")
    print("3- Ver agenda del día.")
    print("4- Ver resumen general.")
    print("5- Cerrar sistema.")

    opcion = input(">> Qué acción desea realizar?: ")

    if not opcion.isdigit():
        print(">> (!)Error: No es número.")

    else:
        opcion = int(opcion)

        if opcion == 1:

            while True:
                print()
                print("=== DÍAS DE TURNO ===")
                print("1- Lunes.")
                print("2- Martes.")
                print("3- Menú anterior.")
                
                dia = input(">> Escoja día para reservar turno: ")

                if not dia.isdigit():
                    print(">> (!)Error: No es número.")

                else:
                    dia = int(dia)

                    if dia == 1:

                        while True:

                            paciente_reservar = input("Ingrese nombre del paciente: ")

                            if not paciente_reservar.isalpha():
                                print(">> (!)Error: Solo letras.")

                            else:
                                paciente_reservar = str(paciente_reservar)

                                if paciente_reservar == lunes1 or paciente_reservar == lunes2 or paciente_reservar == lunes3 or paciente_reservar == lunes4:
                                    print(">> El paciente ya tiene turno este día.")
                                    break
                                if lunes1 == "":
                                    lunes1 = paciente_reservar
                                    print(">> Reservado en el primer turno del día lunes.")
                                    break
                                

                                elif lunes2 == "":
                                    lunes2 = paciente_reservar
                                    print(">> Reservado en el segundo turno del día lunes.")
                                    break

                                elif lunes3 == "":
                                    lunes3 = paciente_reservar
                                    print(">> Reservado en el tercer turno del día lunes.")
                                    break

                                elif lunes4 == "":
                                    lunes4 = paciente_reservar
                                    print(">> Reservado en el cuarto turno del día lunes.")
                                    break

                    if dia == 2:
                        while True:
                        
                            paciente_reservar = input("Ingrese nombre del paciente: ")
                        
                            if not paciente_reservar.isalpha():
                                print(">> (!)Error: Solo letras.")
                        
                            else:
                                paciente_reservar = str(paciente_reservar)

                                if paciente_reservar == martes1 or paciente_reservar == martes2 or paciente_reservar == martes3:
                                    print(">> El paciente ya tiene turno este día.")
                                    break

                                if martes1 == "":
                                    martes1 = paciente_reservar
                                    print(">> Reservado el primer turno del día martes.")
                                    break
                                elif martes2 == "":
                                    martes2 = paciente_reservar
                                    print(">> Reservado el segundo turno del día martes.")
                                    break
                                elif martes3 == "":
                                    martes3 = paciente_reservar
                                    print(">> Reservado el tercer turno del día martes.")
                                    break

                    elif dia == 3:
                        break

                    if dia > 3 or dia < 1:
                        print(">> (!)Error: Opción fuera de rango.")

        elif opcion == 2:

            while True:
                print()
                print("=== DÍAS DE TURNO ===")
                print("1- Lunes.")
                print("2- Martes.")
                print("3- Menú anterior.")
                
                dia = input(">> Escoja día para eliminar turno: ")

                if not dia.isdigit():
                    print(">> (!)Error: No es número.")
                else:
                    dia = int(dia)

                    if dia == 1:

                        while True:

                            paciente_eliminar = input("Ingrese nombre del paciente: ")

                            if not paciente_eliminar.isalpha():
                                print(">> (!)Error. Solo letras.")
                            else:
                                paciente_eliminar = str(paciente_eliminar)

                                if paciente_eliminar == lunes1:
                                    lunes1 = ""
                                    print(">> Paciente eliminado del primer turno de el día lunes.")
                                    break
                                elif paciente_eliminar == lunes2:
                                    lunes2 = ""
                                    print(">> Paciente eliminado del segundo turno de el día lunes.")
                                    break
                                elif paciente_eliminar == lunes3:
                                    lunes3 = ""
                                    print(">> Paciente eliminado del tercer turno de el día lunes.")
                                    break
                                elif paciente_eliminar == lunes4:
                                    lunes4 = ""
                                    print(">> Paciente eliminado del cuarto turno de el día lunes.")
                                    break
                                else:
                                    print(">> (!)El paciente no se encuentra registrado.")
                                    break
                    elif dia == 2:

                        while True:

                            paciente_eliminar = input("Ingrese nombre del paciente: ")

                            if not paciente_eliminar.isalpha():
                                print(">> (!)Error: Solo letras.")
                            else:
                                paciente_eliminar = str(paciente_eliminar)

                                if paciente_eliminar == martes1:
                                    martes1 = ""
                                    print(">> Paciente eliminado del primer turno de el día martes.")
                                    break
                                elif paciente_eliminar == martes2:
                                    martes2 = ""
                                    print(">> Paciente eliminado del segundo turno de el día martes.")
                                    break
                                elif paciente_eliminar == martes3:
                                    martes3 = ""
                                    print(">> Paciente eliminado del tercer turno de el día martes.")
                                else:
                                    print(">> (!)El paciente no se encuentra registrado.")
                                    break   
                    elif dia == 3:
                        break

                    else:
                        print(">> (!)Error: Rango inválido.")    

        elif opcion == 3:

            while True:
                print()
                print("=== AGENDA DE DÍA ===")
                print("1- Lunes.")
                print("2- Martes.")
                print("3- Menú anterior.")

                dia_agenda = input("Elija el día para ver su agenda: ")

                if not dia_agenda.isdigit():
                    print(">> (!)Error: No es número.")
                else:
                    dia_agenda = int(dia_agenda)

                    if dia_agenda == 1:

                        if lunes1 == "":
                            lunes1 = "(Libre)"
                        elif lunes2 == "":
                            lunes2 = "(Libre)"
                        elif lunes3 == "":
                            lunes3 = "(Libre)"
                        elif lunes4 == "":
                            lunes4 = "(Libre)"

                        print("=== AGENDA LUNES ===")
                        print(f"Turno 1: {lunes1}")
                        print(f"Turno 2: {lunes2}")
                        print(f"Turno 3: {lunes3}")
                        print(f"Turno 4: {lunes4}")

                    if dia_agenda == 2:

                        if martes1 == "":
                            martes1 = "(Libre)"
                        elif martes2 == "":
                            martes2 = "(Libre)"
                        elif martes3 == "":
                            martes3 = "(Libre)"

                        print("=== AGENDA MARTES ===")
                        print(f"Turno 1: {martes1}")
                        print(f"Turno 2: {martes2}")
                        print(f"Turno 3: {martes3}")

                    if dia_agenda == 3:
                        break
        
        elif opcion == 4:

            lunes_ocupados = 0
            lunes_libres = 0
            martes_ocupados = 0
            martes_libres = 0

            if lunes1 == "" or lunes1 == "(Libre)":
                lunes_libres += 1
            else:
                lunes_ocupados += 1

            if lunes2 == "" or lunes2 == "(Libre)":
                lunes_libres += 1
            else:
                lunes_ocupados += 1

            if lunes3 == "" or lunes3 == "(Libre)":
                lunes_libres += 1
            else:
                lunes_ocupados += 1

            if lunes4 == "" or lunes4 == "(Libre)":
                lunes_libres += 1

            if martes1 == "" or martes1 == "(Libre)":
                martes_libres += 1
            else:
                martes_ocupados += 1

            if martes2 == "" or martes2 == "(Libre)":
                martes_libres += 1
            else:
                martes_ocupados += 1

            if martes3 == "" or martes3 == "(Libre)":
                martes_libres += 1
            else:
                martes_ocupados += 1

            print("=== LUNES ===")
            print(f"Turnos libres: {lunes_libres}")
            print(f"Turnos ocupados: {lunes_ocupados}")
            print("--------------------------------")
            print("=== MARTES ===")
            print(f"Turnos libres: {martes_libres}")
            print(f"Turnos ocupados: {martes_ocupados}")

            if lunes_ocupados > martes_ocupados:
                print(">> Lunes es el día con más turnos ocupados.")
            elif lunes_ocupados < martes_ocupados:
                print(">> Martes es el día con más turnos ocupados.")
            else:
                print(">> Empate de días ocupados.")

        elif opcion == 5:
            print("=== HASTA LUEGO ===")
            break

        else:
            print(">> (!)Error: Rango inválido.")