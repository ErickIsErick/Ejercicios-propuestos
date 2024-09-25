class Lista:
    def __init__(self):
        self.lista = []
        self.ventana = 0 

    def antLista(self):
        if self.ventana > 0:
            self.ventana -= 1
            print(f"la ventana ahora esta en la posicion {self.ventana}")
        else:
            print("la ventana ya esta en la primera posicion.")

    def menu(self):
        while True:
            print("╔═════════════════════╗")
            print("║    MENU PRINCIPAL   ║")
            print("╠═════════════════════╣")
            print("║ 1. avanzar ventana   ║")
            print("║ 2. retroceder ventana║")
            print("║ 3. salir             ║")
            print("╚═════════════════════╝")
            opcion = int(input("elige una opcion: "))
            if opcion == 1:
                self.ventana += 1
                print(f"la ventana ahora está en la posicion {self.ventana}")
            elif opcion == 2:
                self.antLista()
            elif opcion == 3:
                print("saliendo... :>")
                break
            else:
                print("errorr")


lista = Lista()
lista.menu()
