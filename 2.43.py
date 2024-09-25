class Nodo:
    def __init__(self, posicion, elemento):
        self.posicion = posicion
        self.elemento = elemento
        self.siguiente = None

class Lista:
    def __init__(self):
        self.longitud = 0
        self.primero = None
        self.ventana = None

    def insertarElemento(self, posicion, elemento):
        nuevoNodo = Nodo(posicion, elemento)
        nuevoNodo.siguiente = self.primero
        self.primero = nuevoNodo
        self.longitud += 1

    def moverVentana(self, posicion):
        actual = self.primero
        while actual is not None and actual.posicion != posicion:
            actual = actual.siguiente
        self.ventana = actual

    def eliminarElemento(self, posicion):
        actual = self.primero
        anterior = None
        while actual is not None and actual.posicion != posicion:
            anterior = actual
            actual = actual.siguiente
        if actual is not None:
            if anterior is None:
                self.primero = actual.siguiente
            else:
                anterior.siguiente = actual.siguiente
            self.longitud -= 1

    def verPosVent(self):
        if self.ventana is not None:
            return self.ventana.posicion
        else:
            return "la ventana no esta apuntando a ningun nodo."

    def mostrarLista(self):
        actual = self.primero
        if actual is None:
            print("La lista esta vacia.")
        else:
            while actual is not None:
                print(f"posicion: {actual.posicion}, elemento: {actual.elemento}")
                actual = actual.siguiente

    def menu(self):
        while True:
            print("╔═════════════════════╗")
            print("║    MENU PRINCIPAL   ║")
            print("╠═════════════════════╣")
            print("║ 1. añadir elemento   ║")
            print("║ 2. mover ventana     ║")
            print("║ 3. eliminar elemento ║")
            print("║ 4. ver posicion de la ventana ║")
            print("║ 5. mostrar lista     ║")
            print("║ 6. salir             ║")
            print("╚═════════════════════╝")
            opcion = int(input("elige una opcion: "))
            if opcion == 1:
                posicion = int(input("introduce la posicion: "))
                elemento = int(input("introduce el elemento: "))
                self.insertarElemento(posicion, elemento)
                print(f"elemento {elemento} añadido en la posicion {posicion}.")
            elif opcion == 2:
                posicion = int(input("digita la posicion a mover la ventana: "))
                self.moverVentana(posicion)
                print(f"ventana movida a la posicion {posicion}.")
            elif opcion == 3:
                posicion = int(input("Introduce la posicion del elemento a eliminar: "))
                self.eliminarElemento(posicion)
                print(f"elemento en la posicion {posicion} eliminado.")
            elif opcion == 4:
                print(f"la posicion actual de la ventana es: {self.verPosVent()}")
            elif opcion == 5:
                self.mostrarLista()
            elif opcion == 6:
                print("Saliendo... :>")
                break
            else:
                print("errorr")


lista = Lista()
lista.insertarElemento(1, 6)
lista.insertarElemento(2, 5)
lista.insertarElemento(3, 7)
lista.insertarElemento(4, 9)
lista.moverVentana(3)
lista.menu()
