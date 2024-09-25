class Almacen:
    def __init__(self):
        self.inventario = {}

    def agregar_producto(self, producto, cantidad):
        if producto in self.inventario:
            self.inventario[producto] += cantidad
        else:
            self.inventario[producto] = cantidad

    def eliminar_producto(self, producto, cantidad):
        if producto in self.inventario:
            self.inventario[producto] -= cantidad
            if self.inventario[producto] <= 0:
                del self.inventario[producto]

    def impAlmacen(self):
        for producto, cantidad in self.inventario.items():
            print(f"{producto}: {cantidad} unidades")

    def menu(self):
        while True:
            print("╔═════════════════════╗")
            print("║    MENU PRINCIPAL   ║")
            print("╠═════════════════════╣")
            print("║ 1. añadir producto   ║")
            print("║ 2. eliminar producto ║")
            print("║ 3. mostrar almacén   ║")
            print("║ 4. salir             ║")
            print("╚═════════════════════╝")
            opcion = int(input("Elige una opcion: "))
            if opcion == 1:
                producto = input("introduce el nombre del producto: ")
                cantidad = int(input("introduce la cantidad: "))
                self.agregar_producto(producto, cantidad)
                print(f"Producto {producto} añadido con {cantidad} unidades ")
            elif opcion == 2:
                producto = input("Introduce el nombre del producto: ")
                cantidad = int(input("Introduce la cantidad a eliminar: "))
                self.eliminar_producto(producto, cantidad)
                print(f"Producto {producto} reducido en {cantidad} unidades ")
            elif opcion == 3:
                self.impAlmacen()
            elif opcion == 4:
                print("saliendo...")
                break
            else:
                print("errorr ")


almacen = Almacen()
almacen.menu()
