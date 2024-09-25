class Nodo:
    def __init__(self, data=None):
        self.data = data
        self.sig = None

class ListaEncadenada:
    def __init__(self):
        self.head = None

    def adicLista(self, elem):
        nuevo = Nodo(elem)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.sig:
                actual = actual.sig
            actual.sig = nuevo

    def impLista(self):
        if not self.head:
            print("la lista esta vacia.")
        else:
            actual = self.head
            while actual: 
                print(actual.data, end=" -> ")
                actual = actual.sig
            print("None")

    def eliminarLista(self, pos):
        if self.head is None:
            print("la lista esta vacia")
            return
        actual = self.head
        if pos == 0:
            self.head = actual.sig
            print("elemento eliminado en la posicion 0")
            return
        for i in range(pos - 1):
            if actual is None:
                print("posicion fuera de rango.")
                return
            actual = actual.sig
        if actual.sig is None:
            print("Posicion fuera de rango.")
            return
        actual.sig = actual.sig.sig
        print(f"Elemento eliminado en la posicion {pos}.")    

    def menu(self):
        while True:
            print("╔═════════════════════╗")
            print("║    MENU PRINCIPAL   ║")
            print("╠═════════════════════╣")
            print("║ 1. añadir elemento   ║")
            print("║ 2. eliminar elemento ║")
            print("║ 3. mostrar lista     ║")
            print("║ 4. salir             ║")
            print("╚═════════════════════╝")
            opcion = int(input("elige una opcion: "))
            if opcion == 1:
                elem = int(input("introduce un numero: "))
                self.adicLista(elem)
                print(f"Elemento {elem} añadido a la lista.")
            elif opcion == 2:
                pos = int(input("Introduce la posicion a eliminar: "))
                self.eliminarLista(pos)
            elif opcion == 3:
                self.impLista()
            elif opcion == 4:
                print("saliendo...  :>")
                break
            else:
                print("errorr ")


lista = ListaEncadenada()
lista.menu()
