class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None

    def impBiblioteca(self):
        if not self.libros:
            print("no hay libros en la biblioteca")
        else:
            for libro in self.libros:
                print(f"titulo: {libro.titulo}, autor: {libro.autor}")

    def menu(self):
        while True:
            print("╔═════════════════════╗")
            print("║    MENU PRINCIPAL   ║")
            print("╠═════════════════════╣")
            print("║ 1. añadir libro      ║")
            print("║ 2. buscar libro      ║")
            print("║ 3. mostrar biblioteca║")
            print("║ 4. salir             ║")
            print("╚═════════════════════╝")
            opcion = int(input("elige una opcion: "))
            if opcion == 1:
                titulo = input("introduce el título del libro: ")
                autor = input("introduce el autor del libro: ")
                libro = Libro(titulo, autor)
                self.agregar_libro(libro)
                print(f"libro '{titulo}' añadido a la biblioteca.")
            elif opcion == 2:
                titulo = input("Introduce el titulo a buscar: ")
                libro = self.buscar_libro(titulo)
                if libro:
                    print(f"libro encontrado: titulo: {libro.titulo}, autor: {libro.autor}")
                else:
                    print("libro no encontrado.")
            elif opcion == 3:
                self.impBiblioteca()
            elif opcion == 4:
                print("saliendo...")
                break
            else:
                print("errorr ")


biblioteca = Biblioteca()
biblioteca.menu()
