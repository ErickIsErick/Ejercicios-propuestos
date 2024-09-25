class ListaCompacta:
    def __init__(self, tamaño):
        self.vector = [[None, -1] for _ in range(tamaño)]
        self.libres = list(range(tamaño))
        self.primero = -1
        self.ventana = -1

    def obtenerIndiceLibre(self):
        if self.libres:
            return self.libres.pop(0)
        else:
            return -1

    def liberarIndice(self, indice):
        self.libres.append(indice)

    def insertarElemento(self, elemento):
        indice = self.obtenerIndiceLibre()
        if indice == -1:
            print("no hay espacio")
            return
        if self.primero == -1:
            self.primero = indice
        else:
            actual = self.primero
            while self.vector[actual][1] != -1:
                actual = self.vector[actual][1]
            self.vector[actual][1] = indice
        self.vector[indice] = [elemento, -1]

    def moverVentana(self, posicion):
        actual = self.primero
        for _ in range(posicion):
            if actual == -1:
                break
            actual = self.vector[actual][1]
        self.ventana = actual

    def eliminarElemento(self, posicion):
        if self.primero == -1:
            print("lista vacia")
            return
        actual = self.primero
        anterior = -1
        for _ in range(posicion):
            if actual == -1:
                break
            anterior = actual
            actual = self.vector[actual][1]
        if actual != -1:
            if anterior == -1:
                self.primero = self.vector[actual][1]
            else:
                self.vector[anterior][1] = self.vector[actual][1]
            self.liberarIndice(actual)

    def mostrarLista(self):
        actual = self.primero
        while actual != -1:
            print(f"Elemento: {self.vector[actual][0]}")
            actual = self.vector[actual][1]

    def menu(self):
        while True:
            print("╔═════════════════════╗")
            print("║    MENU PRINCIPAL   ║")
            print("╠═════════════════════╣")
            print("║ 1. añadir elemento   ║")
            print("║ 2. mover ventana     ║")
            print("║ 3. eliminar elemento ║")
            print("║ 4. mostrar lista     ║")
            print("║ 5. salir             ║")
            print("╚═════════════════════╝")
            opcion = int(input("Elige una opcion: "))
            if opcion == 1:
                elemento = int(input("introduce el elemento: "))
                self.insertarElemento(elemento)
                print(f"elemento {elemento} añadido.")
            elif opcion == 2:
                posicion = int(input("introduce la posicion a mover la ventana: "))
                self.moverVentana(posicion)
                print(f"ventana movida a la posicion {posicion}.")
            elif opcion == 3:
                posicion = int(input("introduce la posicion del elemento a eliminar: "))
                self.eliminarElemento(posicion)
                print(f"elemento en la posicion {posicion} eliminado.")
            elif opcion == 4:
                self.mostrarLista()
            elif opcion == 5:
                print("Saliendo... :>")
                break
            else:
                print("error")


lista = ListaCompacta(10)
lista.insertarElemento(8)
lista.insertarElemento(4)
lista.insertarElemento(7)
lista.insertarElemento(5)
lista.moverVentana(2)
lista.menu()
