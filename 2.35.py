class Lista:
    def __init__(self):
        self.lista = []

    def estaLista(self, elem):
        return elem in self.lista

    def menu(self):
        while True:
            print("╔═════════════════════╗")
            print("║    MENU PRINCIPAL   ║")
            print("╠═════════════════════╣")
            print("║ 1. añadir elemento   ║")
            print("║ 2. buscar elemento   ║")
            print("║ 3. salir             ║")
            print("╚═════════════════════╝")
            opcion = int(input("elige una opcion: "))
            if opcion == 1:
                elem = int(input("introduce un numero: "))
                self.lista.append(elem)
                print(f"elemento {elem} añadido a la lista")
            elif opcion == 2:
                elem = int(input("introduce el numero a buscar: "))
                if self.estaLista(elem):
                    print(f"el numero {elem} esta en la lista ")
                else:
                    print(f"el numero {elem} NO esta en la lista ")
            elif opcion == 3:
                print("saliendo...  :>")
                break
            else:
                print("errorr")


lista = Lista()
lista.menu()
