print("===============")
print("CAJA  DE KIOSCO")
print("===============")

while True:
    nombre = input("Ingrese el nombre del cliente: ")
    print()

    if not nombre.isalpha():
        print("Error. Nombre inválido.")

    else:
        break

while True:
    cant_productos = input(f"Ingrese la cantidad de productos de {nombre}: ")
    print()

    if not cant_productos.isdigit():
        print("Error. Cantidad inválida.")

    else:
        cant_productos = int(cant_productos)

        if cant_productos == 0:
            print("Error. No puede ser 0.")

        else:
            break

cont_productos = 0
total_sin_descuento = 0
ahorro = 0
resultado = ""

for i in range(1,cant_productos + 1):

    while True:
        precio_producto = input(f"Ingrese el precio del producto N°{i}: ")

        if not precio_producto.isdigit():
            print("Error. Precio inválido, pruebe un número entero positivo.")

        else:
            precio_producto = int(precio_producto)

            if precio_producto == 0:
                print("Error. El precio no puede ser 0.")

            else:
                cont_productos += 1
                break

    total_sin_descuento += precio_producto

    while True:

        decision = input("El producto tiene descuento? (S/N): ").lower()
        print("\n")

        if decision == "s" or decision == "n":

            if decision == "s":
                ahorro += precio_producto * 0.10
                break

            elif decision == "n":
                break

        else:
            print("Error. debe ingresar s/n.")

    resultado = resultado + "Producto N°" + str(i) + " - " + "Precio: $" + str(precio_producto) + " " + decision + "/Descuento." + "\n"

promedio =  total_sin_descuento / cant_productos
total_con_descuento = total_sin_descuento - ahorro


print("=========================================")
print("            RESULTADO FINAL              ")
print("=========================================")
print(f"Cliente: {nombre}.")
print(f"Cantidad de productos: {cant_productos}.")
print("=========================================")
print(resultado)
print("=========================================")
print(f"Total: ${total_sin_descuento}.")
print(f"Total con descuento: ${total_con_descuento}.")
print(f"Ahorro: ${ahorro}")
print(f"Promedio de productos: ${promedio}.")