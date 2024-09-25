class Matriz:
    def __init__(self, filas, columnas):
        self.matriz = [[0] * columnas for _ in range(filas)]
        self.filas = filas
        self.columnas = columnas

    def asigneMatriz(self, fila, columna, valor):
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            self.matriz[fila][columna] = valor

    def infoMatriz(self, fila, columna):
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            return self.matriz[fila][columna]
        return None

    def impMatriz(self):
        for fila in self.matriz:
            print(" ".join(map(str, fila)))

    def menu(self):
        while True:
            print("╔═════════════════════╗")
            print("║    MENU PRINCIPAL   ║")
            print("╠═════════════════════╣")
            print("║ 1. asignar valor     ║")
            print("║ 2. mostrar matriz    ║")
            print("║ 3. salir             ║")
            print("╚═════════════════════╝")
            opcion = int(input("Elige una opcion: "))
            if opcion == 1:
                fila = int(input("Introduce la fila: "))
                columna = int(input("Introduce la columna: "))
                valor = int(input("Introduce el valor: "))
                self.asigneMatriz(fila, columna, valor)
                print(f"valor {valor} asignado a [{fila}, {columna}].")
            elif opcion == 2:
                self.impMatriz()
            elif opcion == 3:
                print("saliendo...")
                break
            else:
                print("errorr ")

#
matriz = Matriz(3, 3)  #matriz de 3x3 siuui
matriz.menu()
