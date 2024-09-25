class Lista:
    def __init__(self):
        self.lista = []

    def eliminarLista(self, pos):
        if 0 <= pos < len(self.lista):
            eliminado = self.lista.pop(pos)
            print(f"elemento {eliminado} eliminado de la lista")
        else:
            print("Posicion invalida")

    def menu(self):
        while True:
            print("╔═════════════════════╗")
            print("║    MENU PRINCIPAL   ║")
            print("╠═════════════════════╣")
            print("║ 1. añadir elemento   ║")
            print("║ 2. eliminar por posicion ║")
            print("║ 3. mostrar lista     ║")
            print("║ 4. salir             ║")
            print("╚═════════════════════╝")
            opcion = int(input("elige una opcion: "))
            if opcion == 1:
                elem = int(input("Introduce un numero: "))
                self.lista.append(elem)
                print(f"Elemento {elem} añadido a la lista")
            elif opcion == 2:
                pos = int(input("introduce la posicion a eliminar: "))
                self.eliminarLista(pos)
            elif opcion == 3:
                print("Elementos en la lista:", self.lista)
            elif opcion == 4:
                print("saliendo...  :>")
                break
            else:
                print("errorr")


lista = Lista()
lista.menu()
