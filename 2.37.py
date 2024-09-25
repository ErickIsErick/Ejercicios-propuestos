class Lista:
    def __init__(self):
        self.lista = []

    def impLista(self):
        if not self.lista:
            print("la lista esta vacia ")
        else:
            print("elementos en la lista:")
            for elem in self.lista:
                print(elem)

    def menu(self):
        while True:
            print("╔═════════════════════╗")
            print("║    MENU PRINCIPAL   ║")
            print("╠═════════════════════╣")
            print("║ 1. añadir elemento   ║")
            print("║ 2. imprimir lista    ║")
            print("║ 3. salir             ║")
            print("╚═════════════════════╝")
            opcion = int(input("elige una opcion: "))
            if opcion == 1:
                elem = int(input("Introduce un numero: "))
                self.lista.append(elem)
                print(f"elemento {elem} añadido a la lista.")
            elif opcion == 2:
                self.impLista()
            elif opcion == 3:
                print("saliendo... :>")
                break
            else:
                print("errorr")


lista = Lista()
lista.menu()
