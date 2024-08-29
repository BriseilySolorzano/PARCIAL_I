"""
EJERCICIO 2 --- BIBLIOTECA

Una biblioteca ofrece préstamos de libros a través de una tarjeta impresa que contiene los datos de la persona que realiza el préstamo. 
El sistema de préstamos registra la fecha en que se retira el libro y la fecha límite para su devolución.
 Realiza un programa que solvente esto de una manera más eficaz.  
Implementar la sección de devolución la cual si la fecha excede la que devolución se dará una sanción.
"""

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.prestatarios = {}

    def agregar_libro(self, titulo, autor):
        self.libros[titulo] = {"autor": autor, "prestatario": None, "fecha_limite_devolucion": None}

    def prestar_libro(self, titulo, prestatario, fecha_prestamo, fecha_limite_devolucion):
        if titulo in self.libros and self.libros[titulo]["prestatario"] is None:
            self.libros[titulo]["prestatario"] = prestatario
            self.libros[titulo]["fecha_limite_devolucion"] = fecha_limite_devolucion
            self.prestatarios[prestatario] = titulo
            print(f"Libro '{titulo}' prestado a {prestatario} hasta {fecha_limite_devolucion}")
        else:
            print("Libro no disponible para préstamo")

    def devolver_libro(self, titulo, prestatario, fecha_devolucion):
        if titulo in self.libros and self.libros[titulo]["prestatario"] == prestatario:
            if fecha_devolucion > self.libros[titulo]["fecha_limite_devolucion"]:
                print("Devolución tardía! Se aplicará una sanción.")
            else:
                print("Libro devuelto con éxito")
            self.libros[titulo]["prestatario"] = None
            self.libros[titulo]["fecha_limite_devolucion"] = None
            del self.prestatarios[prestatario]
        else:
            print("Libro no prestado a ti")

    def menu(self):
        while True:
            print("Menú de la Biblioteca:")
            print("1. Agregar libro")
            print("2. Prestar libro")
            print("3. Devolver libro")
            print("4. Salir")
            opcion = input("Elige una opción: ")
            match opcion:
                case "1":
                    titulo = input("Ingrese título del libro: ")
                    autor = input("Ingrese autor del libro: ")
                    self.agregar_libro(titulo, autor)
                case "2":
                    titulo = input("Ingrese título del libro: ")
                    prestatario = input("Ingrese su nombre: ")
                    fecha_prestamo = input("Ingrese fecha de préstamo (AAAA-MM-DD): ")
                    fecha_limite_devolucion = input("Ingrese fecha límite de devolución (AAAA-MM-DD): ")
                    self.prestar_libro(titulo, prestatario, fecha_prestamo, fecha_limite_devolucion)
                case "3":
                    titulo = input("Ingrese título del libro: ")
                    prestatario = input("Ingrese su nombre: ")
                    fecha_devolucion = input("Ingrese fecha de devolución (AAAA-MM-DD): ")
                    self.devolver_libro(titulo, prestatario, fecha_devolucion)
                case "4":
                    print("Adiós!")
                    break
                case _:
                    print("Opción inválida. Intente de nuevo!")

biblioteca = Biblioteca()
biblioteca.menu()