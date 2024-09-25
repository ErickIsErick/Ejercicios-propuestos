class ListaConCursores:
    def __init__(self, tamaño):
        self.informacion = [None] * tamaño
        self.cursores = [-1] * tamaño
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
        self.informacion[indice] = elemento
        if self.primero == -1:
            self.primero = indice
        else:
            actual = self.primero
            while self.cursores[actual] != -1:
                actual = self.cursores[actual]
            self.cursores[actual] = indice
        self.cursores[indice] = -1

    def moverVentana(self, posicion):
        actual = self.primero
        for _ in range(posicion):
            if actual == -1:
                break
            actual = self.cursores[actual]
        self.ventana = actual

    def eliminarElemento(self, posicion):
        if self.primero == -1:
            print("lista está vacia.")
            return
        actual = self.primero
        anterior = -1
        for _ in range(posicion):
            if actual == -1:
                break
            anterior = actual
            actual = self.cursores[actual]
        if actual != -1:
            if anterior == -1:
                self.primero = self.cursores[actual]
            else:
                self.cursores[anterior] = self.cursores[actual]
            self.liberarIndice(actual)

    def mostrarLista(self):
        actual = self.primero
        while actual != -1:
            print(f"elemento: {self.informacion[actual]}")
            actual = self.cursores[actual]

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
                print(f"elemento {elemento} añadido")
            elif opcion == 2:
                posicion = int(input("introduce la posicion a mover la ventana: "))
                self.moverVentana(posicion)
                print(f"Ventana movida a la posicion {posicion}.")
            elif opcion == 3:
                posicion = int(input("introduce la posicion del elemento a eliminar: "))
                self.eliminarElemento(posicion)
                print(f"elemento en la posicion {posicion} eliminadi")
            elif opcion == 4:
                self.mostrarLista()
            elif opcion == 5:
                print("Saliendo... :>")
                break
            else:
                print("errorr ")


lista = ListaConCursores(10)
lista.insertarElemento(8)
lista.insertarElemento(4)
lista.insertarElemento(7)
lista.insertarElemento(5)
lista.moverVentana(2)
lista.menu()
