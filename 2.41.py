class ListaCompacta:
    def __init__(self):
        self.lista = []

    def adicLista(self, elem):
        if not self.lista or self.lista[-1][0] != elem:
            self.lista.append([elem, 1])
        else:
            self.lista[-1][1] += 1

    def impLista(self):
        if not self.lista:
            print("la lista esta vaciaa")
        else:
            for elem, count in self.lista:
                print(f"{elem} aparece {count} veces")

    def menu(self):
        while True:
            print("╔═════════════════════╗")
            print("║    MENU PRINCIPAL   ║")
            print("╠═════════════════════╣")
            print("║ 1. añadir elemento   ║")
            print("║ 2. mostrar lista     ║")
            print("║ 3. salir             ║")
            print("╚═════════════════════╝")
            opcion = int(input("elige una opcion: "))
            if opcion == 1:
                elem = int(input("Introduce un numero: "))
                self.adicLista(elem)
                print(f"elemento {elem} añadido a la lista ")
            elif opcion == 2:
                self.impLista()
            elif opcion == 3:
                print("saliendo...")
                break
            else:
                print("errorr ")



lista = ListaCompacta()
lista.menu()
