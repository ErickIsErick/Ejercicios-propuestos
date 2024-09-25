class Lista:
    def __init__(self):
        self.lista = []
        self.ventana = -1  #posicion de la ventana

    def posVentanaLista(self):
        return self.ventana


    def menu(self):
        while True:  
            print("╔═════════════════════╗")
            print("║    MENU PRINCIPAL   ║")
            print("╠═════════════════════╣")
            print("║ 1. ver posicion de la ventana ║")
            print("║ 2. salir            ║")
            print("╚═════════════════════╝")
            opcion = int(input("elige una opcion: "))
            if opcion == 1:
                print(f"la posicion actual de la ventana es: {self.posVentanaLista()}")
            elif opcion == 2:
                print("saliendo...  :>")
                break
            else:
                print("errorr")


lista = Lista()
lista.menu()
