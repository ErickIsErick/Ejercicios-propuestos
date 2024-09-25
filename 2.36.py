class Lista:
    def __init__(self):
        self.lista = []

    def adicLista(self, elem):
        self.lista.append(elem)

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
                elem = int(input("introduce un numero: "))
                self.adicLista(elem)
                print(f"elemento {elem} añadido a la lista")
            elif opcion == 2:
                print("elementos en la lista:", self.lista)
            elif opcion == 3:
                print("saliendo...  :>")
                break
            else:
                print("errorr")

lista = Lista()
lista.menu()
