class TablaHash:                                          
    def __init__(self, tamaño):
        self.tabla = [None] * tamaño                    #este codigo es una "mejora" del anterior 
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
        self.tabla[indice] = elemento
        if self.primero == -1:
            self.primero = indice
        else:
            actual = self.primero
            while self.tabla[actual] is not None:
                actual = (actual + 1) % len(self.tabla)
            self.tabla[actual] = indice

    def moverVentana(self, posicion):
        if 0 <= posicion < len(self.tabla):
            self.ventana = posicion
        else:
            print("fuera de rango ")

    def eliminarElemento(self, posicion):
        if 0 <= posicion < len(self.tabla) and self.tabla[posicion] is not None:
            self.tabla[posicion] = None
            self.liberarIndice(posicion)
        else:
            print("posicion fuera de rango or elemento no existe")

    def mostrarLista(self):
        for i, elemento in enumerate(self.tabla):
            if elemento is not None:
                print(f"posicion: {i}, elemento: {elemento}")

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
            opcion = int(input("elige una opcion: "))
            if opcion == 1:
                elemento = int(input("introduce el elemento: "))
                self.insertarElemento(elemento)
                print(f"elemento {elemento} añadido")
            elif opcion == 2:
                posicion = int(input("introduce la posicion a mover la ventana: "))
                self.moverVentana(posicion)
                print(f"ventana movida a la posición {posicion}")
            elif opcion == 3:
                posicion = int(input("introduce la posicion del elemento a eliminar: "))
                self.eliminarElemento(posicion)
                print(f"elemento eliminado en la posicion {posicion}  ")
            elif opcion == 4:
                self.mostrarLista()
            elif opcion == 5:
                print("Saliendo... :>")
                break
            else:
                print("errorr ")


#mejoro la eficiencia porque tiene mejor gestion de espacio, la tabla hash la hace mas sencilla y directa


tabla = TablaHash(10)
tabla.insertarElemento(8)
tabla.insertarElemento(4)
tabla.insertarElemento(7)
tabla.insertarElemento(5)
tabla.moverVentana(2)
tabla.menu()
