class Linea:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estaciones = []

    def agregar_estacion(self, estacion):
        self.estaciones.append(estacion)

    def impLineas(self):
        print(f"inea {self.nombre}: {', '.join(self.estaciones)}")

class Metro:
    def __init__(self):
        self.lineas = []

    def agregar_linea(self, linea):
        self.lineas.append(linea)

    def impMetro(self):
        for linea in self.lineas:
            linea.impLineas()

    def menu(self):
        while True:
            print("╔═════════════════════╗")
            print("║    MENU PRINCIPAL   ║")
            print("╠═════════════════════╣")
            print("║ 1. añadir línea      ║")
            print("║ 2. añadir estación   ║")
            print("║ 3. mostrar metro     ║")
            print("║ 4. salir             ║")
            print("╚═════════════════════╝")
            opcion = int(input("elige una opción: "))
            if opcion == 1:
                nombre = input("introduce el nombre de la línea: ")
                linea = Linea(nombre)
                self.agregar_linea(linea)
                print(f"linea {nombre} añadida.")
            elif opcion == 2:
                nombre_linea = input("Introduce el nombre de la linea: ")
                estacion = input("introduce el nombre de la estacion: ")
                for linea in self.lineas:
                    if linea.nombre == nombre_linea:
                        linea.agregar_estacion(estacion)
                        print(f"estacion {estacion} añadida a la linea {nombre_linea}.")
                        break
                else:
                    print("Linea no encontrada ")
            elif opcion == 3:
                self.impMetro()
            elif opcion == 4:
                print("saliendo...")
                break
            else:
                print("errorr ")


metro = Metro()
metro.menu()
