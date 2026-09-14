# Actividad 1

notas_estudiantes = [8.5,9,3,8,7,6.5,5,10,7.8,9.3]
print("-"*10 + "NOTAS" + "-"*10)

for nota in notas_estudiantes:
    print(nota, end=" ")

suma_notas = 0
print("\n")

print("-"*5 + "PROMEDIO" + "-"*5)
for nota in notas_estudiantes:
    suma_notas += nota

promedio = suma_notas / len(notas_estudiantes)
print(f" El promedio es {promedio:.2f}")

nota_max = notas_estudiantes[0]
nota_min = notas_estudiantes[0]
print("\n")

for nota in notas_estudiantes:
    if nota > nota_max:
        nota_max = nota

    if nota < nota_min:
        nota_min = nota

print("-"*5 + "NOTA MÁXIMA" + "-"*5)
print(f"Nota máxima: {nota_max}") 
print("\n")

print("-"*5 + "NOTA MÍNIMA" + "-"*5) 
print(f"Nota mínima: {nota_min}")

# Actividad 2

cant_productos = 5
lista_productos = []

while cant_productos != 0:
    productos = input("Ingrese 5 productos de a uno: ")
    cant_productos -= 1
    lista_productos.append(productos)


print("-"*30)
print("    Lista de Productos     ")
print("-"*30)
lista_ordenada = sorted(lista_productos)

for lista in (lista_ordenada):
    print(f"- {lista}")

while True:
    respuesta = input("Desea eliminar algún producto? (s/n): ")
    if respuesta == "s":
        borrar = input("Qué producto desea eliminar?: ")
        if borrar in lista_productos:
            lista_productos.remove(borrar)
            print(f"El producto ha sido eliminado.")
            lista_ordenada = sorted(lista_productos)
            print("="*30)
            print("     VISTA PREVIA     ")
            print("="*30)
            for productos in lista_ordenada:
                print(f"- {productos}")

        else:
            print("El producto no se encuentra en la lista.")

    else:
        break

print("="*30)
print("     LISTA FINAL     ")
print("="*30)
for productos in lista_ordenada:
    print(f"- {productos}")
print("="*30)

# Actividad 3

import random
numeros_azar = []
numeros_par = []
numeros_impar = []

for i in range(15):
    numeros = random.randint(0,100)
    numeros_azar.append(numeros)

print("="*30)
print("  Lista numérica azar   ")
print("="*30)

for lista in range(len(numeros_azar)):
    if lista == len(numeros_azar) -1:
        print(numeros_azar[lista])
    else:
        print(numeros_azar[lista], end=" - ")
print("\n")

for numero in numeros_azar:
    if numero % 2 == 0:
        numeros_par.append(numero)

    else:
        numeros_impar.append(numero)


print("="*30)
print("   Lista Pares     ")
print("Cantidad de números pares:", len(numeros_par))
print("="*30)
for lista in range(len(numeros_par)):
    if lista == len(numeros_par) -1:
        print(numeros_par[lista])
    else:
        print(numeros_par[lista], end=" - ")
print("\n")

print("="*30)
print("    Lista Impares   ")
print("Cantidad de números impares:", len(numeros_impar))
print("="*30)
for lista in range(len(numeros_impar)):
    if lista == len(numeros_impar) -1:
        print(numeros_impar[lista])
    else:
        print(numeros_impar[lista], end=" - ")

# Actividad 4

datos = [1,3,5,3,7,1,9,5,3]
sin_repeticion = []

print("="*30)
print("  Lista original   ")
print("="*30)
for lista in range(len(datos)):
    if lista == len(datos) -1:
        print(datos[lista])
    else:
        print(datos[lista], end=" - ")
print("\n")

for numeros in datos:
    if numeros not in sin_repeticion:
        sin_repeticion.append(numeros)
    
print("="*30)
print("  Lista sin repetidos   ")
print("="*30)
for lista in range(len(sin_repeticion)):
    if lista == len(sin_repeticion) -1:
        print(sin_repeticion[lista])
    else:
        print(sin_repeticion[lista], end=" - ")

# Actividad 5

lista_presentes = ["Juan","Mateo","Lucas","Pablo","Rocio","María","Ana","Lucia"]

print("="*30)
print("  Lista Actual   ")
print("="*30)
for lista in lista_presentes:
    print("-", lista)
print("\n")

opcion = ""
while opcion != 3:
    print("Menú de opciones.")
    print("-"*30)
    print("1) Eliminar.")
    print("2) Agregar.")
    print("3) Terminar.")
    opcion = int(input("Elija la opción(1,2,3): "))

    if opcion == 1:
        eliminar = input("Ingrese el nombre del alumno que desea eliminar: ").title()
        if eliminar in lista_presentes:
            lista_presentes.remove(eliminar)
            print("="*30)
            print("  Lista Actual   ")
            print("="*30)
            for lista in lista_presentes:
                print("-", lista)
            print("Alumno eliminado exitosamente.")
        else:
            print("Error. Este alumno no está en la lista.")

    elif opcion == 2:
        agregar = input("Ingrese el nombre del alumno que desea agregar: ").title()
        if agregar not in lista_presentes:
            lista_presentes.append(agregar)
            print("="*30)
            print("  Lista Actual   ")
            print("="*30)
            for lista in lista_presentes:
                print("-", lista)
            print("Alumno agregado exitosamente.")
            continue

        else:
            print("Este nombre ya se encuentra en la lista.")

    else:
        break
print("="*30)
print("  Lista Final   ")
print("="*30)
for lista in lista_presentes:
    print("-", lista)
# Actividad 6

import random
numerosazar = []

for i in range(10):
    numeros = random.randint(0,100)
    numerosazar.append(numeros)


print("="*30)
print("   Lista de Números    ")
print("="*30)
for lista in numerosazar:
    print(lista, end=". ")
print("\n")
    
lista_alreves = numerosazar[-1:] + numerosazar[:-1]

print("="*30)
print("   Lista al Revés    ")
print("="*30)
for lista in lista_alreves:
    print(lista, end=". ")
print("\n")

# Actividad 7

temperaturas = [
    [12, 22],
    [10, 25],
    [14, 28],
    [15, 20],
    [8,  19],
    [11, 26], 
    [13, 24]
]

semana = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]

print("="*30)
print("  Temperaturas de la semana  ")
print("="*30)
for lista in range(len(temperaturas)):
    print(f"{semana[lista]}: Mín {temperaturas[lista][0]}°C | Máx {temperaturas[lista][1]}°C")

suma_maximas = 0
suma_minimas = 0

for temp in temperaturas:
    suma_maximas += temp[1]
    suma_minimas += temp[0]

promedio_max = suma_maximas / len(temperaturas)
promedio_min = suma_minimas / len(temperaturas)

print("="*50)
print(f"Promedio de temperatura mínima: {promedio_min: .1f}°C.")
print(f"Promedio de temperatura máxima: {promedio_max: .1f}°C")
print("="*50)

max_amplitud = 0
dia_mayor_amplitud = ""

for i in range(len(temperaturas)):
    amplitud_hoy = temperaturas[i][1] - temperaturas[i][0]

    if amplitud_hoy > max_amplitud:
        max_amplitud = amplitud_hoy
        dia_mayor_amplitud = semana[i]

print(f"La mayor amplitud térmica fué el día {dia_mayor_amplitud} con {max_amplitud}°C de diferencia.")
print("="*50)

# Actividad 8

n_matriz = [
    [8, 7, 6],
    [6, 9, 7],
    [9, 10, 8],
    [4, 6, 5],
    [2, 8, 8]
]

estudiantes = ["Estudiante 1","Estudiante 2","Estudiante 3","Estudiante 4","Estudiante 5"]
materias = ["Matemática","Lengua","Historia"]

print("="*40)
print("   Planilla de notas   ")
print("="*40)
for i in range(len(n_matriz)):
    print(f"{estudiantes[i]} | Matemática: {n_matriz[i][0]} | Lengua: {n_matriz[i][1]} | Historia: {n_matriz[i][2]}")
    print(f"-"*55)
print("\n")

print("Promedio por Estudiante:")
print("-"*50)
for i in range(len(n_matriz)):
    suma_notas_alumno = 0
    
    for nota in n_matriz[i]:
        suma_notas_alumno += nota
        
    promedio_alumno = suma_notas_alumno / 3
    print(f"- {estudiantes[i]}: {promedio_alumno:.2f}")
print("\n")

print("Promedio por Materia:")
print("-"*40)
for j in range(3):
    suma_materia = 0
    
    for i in range(len(n_matriz)):
        suma_materia += n_matriz[i][j]
        
    promedio_materia = suma_materia / len(n_matriz)
    print(f"- {materias[j]}: {promedio_materia:.2f}")
print("\n")

# Actividad 9

tablero = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

jugadores = ["X","O"]
turno = 0

print("-"*13)
print("| Ta,Te,Ti! |")
print("-"*13)

for jugada in range(9):
    print("\nTablero Actual:")

    for i in range(3):
        for j in range(3):
            print(tablero[i][j], end=" ")#
        print()

        jugador_actual = jugadores[turno]

    print(f"Turno del jugador: '{jugador_actual}'")

    fila = int(input("Ingrese la fila (0-2): "))
    columna = int(input("Ingrese la columna (0-2): "))

    if fila >= 0 and fila <= 2 and columna >= 0 and columna <=2: 
        if tablero[fila][columna] == "-":
            tablero[fila][columna] = jugador_actual

            turno = (turno + 1) % 2

        else:
            print("Casilla ocupada.")

    else:
        print("Casilla inválida.")

if tablero[0][0] == tablero[0][1] == tablero[0][2] != "-":
    print("ganó:", tablero[0][0])

elif tablero[1][0] == tablero[1][1] == tablero[1][2] != "-":
    print("Ganó:", tablero[1][0])

elif tablero[2][0] == tablero[2][1] == tablero[2][2] != "-":
    print("Ganó:", tablero[2][0])

elif tablero[0][0] == tablero[1][0] == tablero[2][0] != "-":
    print("Ganó:", tablero[0][0])

elif tablero[0][1]== tablero[1][1] == tablero[2][1] != "-":
    print("Ganó:", tablero[0][1])

elif tablero[0][2] == tablero[1][2] == tablero[2][2] != "-":
    print("Ganó:", tablero[0][2])

elif tablero[0][0] == tablero[1][1] == tablero[2][2] != "-":
    print("Ganó:", tablero[0][0])

elif tablero[0][2] == tablero[1][1] == tablero[2][0] != "-":
    print("Ganó:", tablero[0][2])

else:

    print("Empate.")

# Actividad 10

ventas = [
    [10, 15, 20, 12, 18, 25, 30],
    [5,  8,  12, 10, 7,  14, 20],
    [25, 30, 28, 35, 40, 50, 45],
    [12, 14, 11, 15, 10, 18, 22]
]

nombres_productos = ["Producto 1", "Producto 2", "Producto 3", "Producto 4"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

max_ventas_producto = 0
producto_mas_vendido = ""

print("="*40)
print("  Total Vendido por Producto")
print("="*40)

for i in range(4):
    total_producto = 0
    for j in range(7):
        total_producto += ventas[i][j]
    
    print(f"- {nombres_productos[i]}: {total_producto} unidades.")
    
    if total_producto > max_ventas_producto:
        max_ventas_producto = total_producto
        producto_mas_vendido = nombres_productos[i]

print("-"*40)
print("  Total Vendido por Día  ")
print("="*40)

max_ventas_dia = 0
dia_mas_vendido = ""

for j in range(7):
    total_dia = 0

    for i in range(4):
        total_dia += ventas[i][j]
    
    print(f"- {dias_semana[j]}: {total_dia} unidades.")
    if total_dia > max_ventas_dia:
        max_ventas_dia = total_dia
        dia_mas_vendido = dias_semana[j]

print("-"*40)

print("  Conclusiones de la Semana")
print("="*40)
print(f"El día con mayores ventas totales fue el {dia_mas_vendido} ({max_ventas_dia} unidades).")
print(f"El producto más vendido de la semana fue el {producto_mas_vendido} ({max_ventas_producto} unidades).")
print("="*40)


#Actividad 11

estudiantes = ["Juan","Maria","Nicolas","Diego","Gabriel","Facundo","Valeria","Rocio","ignacio","Benja"]

nombre = input("Ingrese nombre para buscar: ")

if not nombre.isalpha():
    print(">>Error: Solo letras.")
else:
    nombre = nombre.capitalize()

if nombre in estudiantes:
    posicion = estudiantes.index(nombre)
    print("El nombre si está en la lista.")
    print(f"Se encuentra en la posicion: {posicion +1}")
else:
    print("El nombre no se encuentra en la lista.")


#Actividad 12
cont = 0
numeros = []
print("Ingrese 8 numeros enyertos positivos.")
while cont < 8:
    num = input(">")

    if not num.isdigit():
        print(">>Error: Solo números.")
    else:
        num = int(num)
        numeros.append(num)
        cont += 1
        
        print("=== LISTA ORIGINAL ===")
        print(numeros)
        
        lista_alreves = reversed(numeros)
        lista_ordenada = sorted(numeros)
        
        
        print("=== LISTA ORDENADA ===")
        print(lista_ordenada)
        print("=== LISTA ALREVES ===")
        print(lista_alreves)


#Actividad 13

puntajes = [450,1200,875,990,300,1500,640]
mas_alto = puntajes[0]
mas_bajo = puntajes[0]
for i in range(len(puntajes)):

    if puntajes[i] > mas_alto:
        mas_alto = puntajes[i]
    elif puntajes[i] < mas_bajo:
        mas_bajo = puntajes[i]

ranking = sorted(puntajes)
print(f"El puntaje más najo es {mas_bajo}")
print(f"El puntaje más alto es {mas_alto}")
print("=== RANKING ===")
for j in puntajes:
    print("-",j)

posicion =  ranking.index(990)

print(f"El puntaje 990 está en la posición {posicion}.")

