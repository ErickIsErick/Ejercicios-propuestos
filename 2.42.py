class Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.sig = None


class ListaEnlazada:
    def __init__(self):
        self.head = Nodo()  #nodo de encabezado

    def adicLista(self, elem):
        nuevo_nodo = Nodo(elem)
        actual = self.head
        while actual.sig:
            actual = actual.sig
        actual.sig = nuevo_nodo

    def impLista(self):
        actual = self.head.sig
        if not actual:
            print("la lista esta vacia ")
        else:
            while actual:
                print(actual.dato, end=" -> ")
                actual = actual.sig
            print("none")

#lista compacta de elementos repetidos
class ListaCompacta:
    def __init__(self):
        self.lista = []

    def adicLista(self, elem):
        if not self.lista or self.lista[-1][0] != elem:
            self.lista.append([elem, 1])
        else:
            self.lista[-1][1] += 1

    def impLista(self):
        if not self.lista:
            print("la lista esta vacia ")
        else:
            for elem, count in self.lista:
                print(f"{elem} aparece {count} veces")

#metodo para convertir 
#lista enlazada a compacta
def convertirACompacta(lista_enlazada):
    lista_compacta = ListaCompacta()
    actual = lista_enlazada.head.sig
    while actual:
        lista_compacta.adicLista(actual.dato)
        actual = actual.sig
    return lista_compacta

#metodo para convertir de lista compacta a enlazada
def convertirAEnlazada(lista_compacta):
    lista_enlazada = ListaEnlazada()
    for elem, count in lista_compacta.lista:
        for _ in range(count):
            lista_enlazada.adicLista(elem)
    return lista_enlazada


def menu():
    lista_enlazada = ListaEnlazada()
    lista_compacta = None

    while True:
        print("╔═════════════════════╗")
        print("║    MENU PRINCIPAL   ║")
        print("╠═════════════════════╣")
        print("║ 1. añadir a lista enlazada ║")
        print("║ 2. mostrar lista enlazada  ║")
        print("║ 3. convertir a compacta    ║")
        print("║ 4. mostrar lista compacta  ║")
        print("║ 5. convertir a enlazada    ║")
        print("║ 6. salir                   ║")
        print("╚═════════════════════╝")
        opcion = int(input("Elige una opcion: "))

        if opcion == 1:
            elem = int(input("Introduce un numero: "))
            lista_enlazada.adicLista(elem)
            print(f"elemento {elem} añadido a la lista enlazada")
        elif opcion == 2:
            lista_enlazada.impLista()
        elif opcion == 3:
            lista_compacta = convertirACompacta(lista_enlazada)
            print("conversion a lista compacta completada ")
        elif opcion == 4:
            if lista_compacta:
                lista_compacta.impLista()
            else:
                print("no se ha convertido la lista a compacta ")
        elif opcion == 5:
            if lista_compacta:
                lista_enlazada = convertirAEnlazada(lista_compacta)
                print("conversion a lista enlazada completada ")
            else:
                print("no hay una lista compacta para convertir.")
        elif opcion == 6:
            print("saliendo...")
            break
        else:
            print("errorr ")

# Ejemplo de uso
menu()
