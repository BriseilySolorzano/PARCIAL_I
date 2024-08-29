"""
Un biólogo veterinario es el encargado de cuidar a los animales de un Zoologicológico.
Él posee su registro donde va el dato de cada animal por sus características y el área del Zoologicológico donde se encuentran.
Cada cierto tiempo hace sus reportes donde enlista todos los animales del Zoologicológico.
Al ser veterinario se encarga también de la salud de los animales, 
por lo cual enlista aquellos que están en tratamiento,
que dosis y cada cuanto tiempo se debe medicar a un animal.
"""

class Animal:
    def __init__(self, nombre, especie, area, estado_salud="saludable", tratamiento=None):
        self.nombre = nombre
        self.especie = especie
        self.area = area
        self.estado_salud = estado_salud
        self.tratamiento = tratamiento

    def __str__(self):
        return f"{self.nombre} ({self.especie}) - {self.area} - {self.estado_salud}"

class Zoologico:
    def __init__(self):
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def generar_reporte(self):
        print("Reporte de animales:")
        for animal in self.animales:
            print(animal)

    def listar_animales_tratamiento(self):
        animales_tratamiento = [animal for animal in self.animales if animal.estado_salud != "saludable"]
        if animales_tratamiento:
            print("Animales en tratamiento:")
            for animal in animales_tratamiento:
                print(f"{animal.nombre} - {animal.tratamiento['dosis']} - cada {animal.tratamiento['frecuencia']} horas")
        else:
            print("No hay animales en tratamiento.")

    def menu(self):
        while True:
            print("\nMenú del Zoo:")
            print("1. Agregar animal")
            print("2. Generar reporte")
            print("3. Listar animales en tratamiento")
            print("4. Salir")

            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                print("-----------------------------------------")
                nombre = input("Ingrese el nombre del animal: ")
                especie = input("Ingrese la especie del animal: ")
                area = input("Ingrese el área del zoo donde se encuentra: ")
                estado_salud = input("Ingrese el estado de salud del animal (saludable/enfermo): ")
                if estado_salud.lower() == "enfermo":
                    tratamiento = {
                        "dosis": input("Ingrese la dosis del tratamiento: "),
                        "frecuencia": input("Ingrese la frecuencia del tratamiento (horas): ")
                    }
                else:
                    tratamiento = None
                animal = Animal(nombre, especie, area, estado_salud, tratamiento)
                self.agregar_animal(animal)
                print("Animal agregado con éxito.")
            elif opcion == "2":
                print("-----------------------------------------")
                self.generar_reporte()
            elif opcion == "3":
                print("-----------------------------------------")
                self.listar_animales_tratamiento()
            elif opcion == "4":
                print("-----------------------------------------")
                print("Saliendo...")
                break
            else:
                print("-----------------------------------------")
                print("Opción inválida. Intente nuevamente.")
                continue

# Crear un objeto Zoologico y llamar al menú
zoologico = Zoologico()
zoologico.menu()