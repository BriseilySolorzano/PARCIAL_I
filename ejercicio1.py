""""
 EJERCICIO 1 -- CONSULTORIO MEDICO
"""

class pacientes:
    def __init__(self, nombre, edad,consulta ):
        self.nombre = nombre
        self.edad = edad
        self.consulta = False  # Esto es para ver si ya tiene un consulta o ncesita una nueva


    def agregar_consulta(self):# Cambia el estado de la consulta
        self.consulta = True
        print(f"Agregar consulta {self.nombre}.\n")

    def mostrar_info(self):# Muestra la información del paciente
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}") 
        print(f"Consulta: {self.consulta}")

class consultas:
    def __init__(self, fecha, ):
        self.fecha = fecha

class Clinica_consulta:
    def __init__(self):
        self.epacientes = []  # Lista para almacenar a los pacientes
    def agregar_pacientes(self, nombre, edad,fecha):
        nuevo_paciente = paciente(nombre, edad, fecha)
        self.paciente.append(nuevo_paciente)
        print(f"Paciente '{nombre}' ha sido registrado.\n")

    def mostrar_lista_pacientes(self): # Muestra la lista de estudiantes registrados.
        if not self.agregar_paciente:
            print("No hay pacientes con consultas")
        else:
            print("Lista de  pacientes\n")
            for pacientes in self.pacientes:
                pacientes.mostrar_info()  # Muestra la información de cada estudiante.
            print("-----------------------")
        


Pacientes = pacientes()

while True:
    print("1. Registrar el nombre del paciente")
    print("2. Mostrar lista de pacientes")
    print("3. Agregar nueva consulta")
    print("4. Salir")
    opcion = input("Seleccione una opción(colocar numero):  ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del paciente: ")
        edad = int(input("Ingrese la edad del paciente: "))
        consulta = input("Ingrese el motivo de su consulta ")
        Pacientes.agregar_pacientes(nombre, edad, consulta)

    elif opcion == "2":
        Pacientes.mostrar_lista_pacientes()

    elif opcion == "3":
        nombre = input("Ingrese el nombre del paciente para crear una nueva consulta ")
        Pacientes.nueva_consulta_paciente(nombre)

    elif opcion == "4":
        print("Gracias por preferir nuestra clinica!")
        break

    else:
        print("Opción inválida. Por favor, intente de nuevo.\n")


    
