"""" 
 EJERCICIO 1 -- CONSULTORIO MEDICO

Un consultorio médico atiende a una serie de pacientes, solo está una
secretaria y en el consultorio hay varios doctores cada paciente llega y
deja sus datos además del motivo de su consulta y posteriormente la
secretaria les asigna la fecha de su consulta.
 En el caso que una persona ya tenga una consulta previa en lugar
de tomar datos se le pasará a sala de esperas. Implementa esta
problemática a tu código.

"""

class Paciente:
    def __init__(self, nombre, edad, consulta):
        self.nombre = nombre
        self.edad = edad
        self.consulta = consulta

    def agregar_consulta(self):  # Cambia el estado de la consulta
        self.consulta = True
        print(f"Agregar consulta {self.nombre}.\n")

    def mostrar_info(self):  # Muestra la información del paciente
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Consulta: {self.consulta}")

class ClinicaConsulta:
    def __init__(self):
        self.pacientes = []  # Lista para almacenar a los pacientes

    def agregar_paciente(self, nombre, edad, consulta):
        nuevo_paciente = Paciente(nombre, edad, consulta)
        self.pacientes.append(nuevo_paciente)
        print(f"Paciente '{nombre}' ha sido registrado.\n")

    def mostrar_lista_pacientes(self):  # Muestra la lista de estudiantes registrados.
        if not self.pacientes:
            print("No hay pacientes con consultas")
        else:
            print("Lista de  pacientes\n")
            for paciente in self.pacientes:
                paciente.mostrar_info()  # Muestra la información de cada estudiante.
            print("-----------------------")

    def nueva_consulta_paciente(self, nombre):
        for paciente in self.pacientes:
            if paciente.nombre == nombre:
                paciente.agregar_consulta()
                return
        print("Paciente no encontrado")

clinica = ClinicaConsulta()

while True:
    print("1. Registrar el nombre del paciente")
    print("2. Mostrar lista de pacientes")
    print("3. Agregar nueva consulta")
    print("4. Salir")
    opcion = input("Seleccione una opción (colocar numero): ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del paciente: ")
        edad = int(input("Ingrese la edad del paciente: "))
        consulta = input("Ingrese el motivo de su consulta ")
        clinica.agregar_paciente(nombre, edad, consulta)

    elif opcion == "2":
        clinica.mostrar_lista_pacientes()

    elif opcion == "3":
        nombre = input("Ingrese el nombre del paciente para crear una nueva consulta ")
        clinica.nueva_consulta_paciente(nombre)

    elif opcion == "4":
        print("Gracias por preferir nuestra clinica!")
        break

    else:
        print("Opción inválida. Por favor, intente de nuevo.\n")

