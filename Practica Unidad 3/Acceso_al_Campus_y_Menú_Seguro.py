print()
print("       ACESSO AL CAMPUS       ")
print("==============================")

usuario_correto = "alumno"
clave_correcta = "python123"
intentos = 3
acceso_usuario = False
acceso_clave = False

while acceso_usuario == False:
    intentos -= 1
    usuario = input("Ingrese el usuario: ")
    print()

    if usuario != usuario_correto:
        print(f"(!)Usuario Incorrecto. Intentos: {intentos}/3.")

        if intentos == 0:
            print("===> CUENTA BLOQUEADA - ACCESO DENEGADO <===")
            print("     ==================================     ")
            print("\n")
            break
    else:
        print(">> USUARIO CORRECTO.")
        print("   ================ ")
        intentos = 3
        acceso_usuario = True

if acceso_usuario == True:
    while acceso_clave == False:
        intentos -= 1
        clave = input("Ingrese la clave: ")
        print("\n")

        if clave != clave_correcta:
            print(f"(!)Clave incorrecta. Intentos {intentos}/3.")

            if intentos == 0:
                print("===> CUENTA BLOQUEADA - ACCESO DENEGADO <===")
                print("     ==================================     ")
                print()
                break
                
        else:
            print("===> CLAVE CORRECTA - ACCESO CONCEDIDO <===")
            acceso_clave = True

if acceso_clave == True:
    while True:
        print("            MENÚ DE OPCIONES.          ")
        print("           ==================          ")
        print("     1- Ver estado de inscripción.")
        print("     2- Cambiar clave.")
        print("     3- Mostrar mensaje motivacional.")
        print("     4- Salir.")

        eleccion = input("Ingrese una opción: ")
        print("\n")

        if not eleccion.isdigit():
            print("=>(!)Error, opción inválida.")
        else:
            eleccion = int(eleccion)

            if eleccion == 1:
                print(">> ESTADO: Inscripto.")
                print()

            elif eleccion == 2:
                while True:
                    clave = input("Nueva clave: ")
                    if len(clave) < 6:
                        print("Error: Mínimo 6 caracteres.")
                    else:
                        print(">> Clave actualizada correctamente.")
                        print()
                        break
            elif eleccion == 3:
                print("---------------------------------------------------------------------------------")
                print("No tienes que ser bueno para empezar, tienes que empezar para llegar a ser bueno.")
                print("---------------------------------------------------------------------------------")
                print()

            elif eleccion == 4:
                print("           ===> HASTA LUEGO <===")
                break

            else:
                print("=>(!)Error, opción fuera de rango")
