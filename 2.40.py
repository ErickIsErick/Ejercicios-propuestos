class ListaBits:
    def __init__(self):
        self.bits = 0  
        self.longitud = 0

    def adicBit(self, bit):
        if bit in (0, 1):
            self.bits = (self.bits << 1) | bit
            self.longitud += 1

    def impBits(self):
        formato = f"0{self.longitud}b"
        cadena_bits = format(self.bits, formato)
        print(cadena_bits)

    def menu(self):
        while True:
            print("╔═════════════════════╗")
            print("║    MENU PRINCIPAL   ║")
            print("╠═════════════════════╣")
            print("║ 1. añadir bit (0/1)  ║")
            print("║ 2. mostrar bits      ║")
            print("║ 3. salir             ║")
            print("╚═════════════════════╝")
            opcion = int(input("Elige una opcion: "))
            if opcion == 1:
                bit = int(input("Introduce 0 o 1: "))
                if bit in [0, 1]:
                    self.adicBit(bit)
                    print(f"Bit {bit} añadido.")
                else:
                    print("solo puedes añadir 0 o 1 ")
            elif opcion == 2:
                self.impBits()
            elif opcion == 3:
                print("Saliendo...")
                break
            else:
                print("errorr ")


lista = ListaBits()
lista.menu()
