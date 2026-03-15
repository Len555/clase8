# SISTEMA BASICO DE INVENTARIO Y PEDIDOS
# Uso de arreglos (listas) y funciones


# Listas que almacenan la información
inventario = []
pedidos = []


# FUNCION: Registrar nuevo producto

def registrar_producto():
    print("\n--- Registrar Producto ---")

    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad disponible: "))
    precio = float(input("Precio del producto: "))

    producto = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    }

    inventario.append(producto)

    print("Producto registrado correctamente.")


# FUNCION: Mostrar inventario

def mostrar_inventario():

    print("\n--- Inventario Actual ---")

    if len(inventario) == 0:
        print("No hay productos registrados.")
        return

    for i, producto in enumerate(inventario):
        print(f"{i+1}. {producto['nombre']} | Cantidad: {producto['cantidad']} | Precio: ${producto['precio']}")


# FUNCION: Editar producto

def editar_producto():

    mostrar_inventario()

    if len(inventario) == 0:
        return

    indice = int(input("Seleccione el numero del producto a editar: ")) - 1

    if 0 <= indice < len(inventario):

        nombre = input("Nuevo nombre: ")
        cantidad = int(input("Nueva cantidad: "))
        precio = float(input("Nuevo precio: "))

        inventario[indice]["nombre"] = nombre
        inventario[indice]["cantidad"] = cantidad
        inventario[indice]["precio"] = precio

        print("Producto actualizado correctamente.")

    else:
        print("Producto no valido.")


# FUNCION: Eliminar producto

def eliminar_producto():

    mostrar_inventario()

    if len(inventario) == 0:
        return

    indice = int(input("Seleccione el numero del producto a eliminar: ")) - 1

    if 0 <= indice < len(inventario):

        inventario.pop(indice)
        print("Producto eliminado correctamente.")

    else:
        print("Producto no valido.")


# FUNCION: Registrar pedido

def registrar_pedido():

    print("\n--- Registrar Pedido ---")

    cliente = input("Nombre del cliente: ")
    producto = input("Producto solicitado: ")
    cantidad = int(input("Cantidad solicitada: "))

    pedido = {
        "cliente": cliente,
        "producto": producto,
        "cantidad": cantidad
    }

    pedidos.append(pedido)

    print("Pedido registrado correctamente.")


# FUNCION: Mostrar pedidos

def mostrar_pedidos():

    print("\n--- Lista de Pedidos ---")

    if len(pedidos) == 0:
        print("No hay pedidos registrados.")
        return

    for i, pedido in enumerate(pedidos):
        print(f"{i+1}. Cliente: {pedido['cliente']} | Producto: {pedido['producto']} | Cantidad: {pedido['cantidad']}")



# MENU PRINCIPAL

def menu():

    while True:

        print("\n  SISTEMA DE INVENTARIO ")
        print("1. Registrar producto")
        print("2. Mostrar inventario")
        print("3. Editar producto")
        print("4. Eliminar producto")
        print("5. Registrar pedido")
        print("6. Mostrar pedidos")
        print("7. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            registrar_producto()

        elif opcion == "2":
            mostrar_inventario()

        elif opcion == "3":
            editar_producto()

        elif opcion == "4":
            eliminar_producto()

        elif opcion == "5":
            registrar_pedido()

        elif opcion == "6":
            mostrar_pedidos()

        elif opcion == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("Opcion no valida.")

# EJECUCION DEL PROGRAMA

menu()
