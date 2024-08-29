"""
Una tienda local vende diversos productos, cada vez que un cliente hace una compra niña mary se encarga de anotarlo en una libreta. 
A su vez, con una calculadora le da el total a cada cliente y les da su respectivo vuelto en caso de necesitarlo. 
 Niña mary también se encarga de atender a los proveedores que le dan cierta cantidad de producto y un precio sugerido de venta, 
propón una solución dentro de tu programa para ayudarle.
"""

class producto:
    def __init__(self, nombre, precio, cantidad, nombreCLiente): # creo el constructor
        self.nombre = nombre 
        self.precio = precio
        self.cantidad = cantidad
        self.nombreCli = nombreCLiente

    def mostrar_datos(self): # muestra los datos organizadamente 
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Nombre del cliente: {self.nombreCli}")
        
class proveedor:
    def __init__(self, nombreProveedor, numContacto, nombreProducto, precioCompra, cantidad):
        self.nombreProveedor = nombreProveedor
        self.numContacto = numContacto
        self.nombreProducto = nombreProducto
        self.precioCompra = precioCompra
        self.cantidad = cantidad
        self.precioSugerido = self.precioSugerido()
        
    def precioSugerido(self):
        return (self.precioCompra*0.25)+self.precioCompra
    
    def mostrar_datos(self):
        print(f"Nombre del proveedor: {self.nombreProveedor}")
        print(f"Numero de contacto: {self.numContacto}")
        print(f"Nombre del producto: {self.nombreProducto}")
        print(f"Nombre del producto: {self.cantidad}")
        print(f"Precio de compra: {self.precioCompra}")
        print(f"Precio sugerido: {self.precioSugerido}")
        
class tienda:
    def __init__(self): 
        self.my_stock = {} 
        self.productos_comprados = []  
        self.proveedores=[]
        self.total = 0 
        
    def ingresar_producto(self): # funcion para ingresar productos
        # los solicito los datos al usuario
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        nombreCli = input("Ingrese el nombre del cliente: ")
        self.my_stock[nombre] = {"nombre": nombre, "precio": precio, "cantidad": cantidad, "cliente":nombreCli}
        print(f"producto {nombre} agregado al inventario.") 
        
    def ingresarProveedor(self):
        nombreProveedor = input("Ingrese el nombre del proveedor: ")
        numContacto = input("Ingrese el numero de contacto del proveedor: ")
        nombreProducto = input("Ingrese el nombre del producto: ")
        precioCompra = float(input("Ingrese el precio de compra del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        self.proveedores.append(proveedor(nombreProveedor, numContacto, nombreProducto, precioCompra, cantidad))
        
    def mostrar_proveedores(self):
        if not self.proveedores:
            print("No hay proveedores registrados")
        else:
            for i in self.proveedores:
                i.mostrar_datos()
            
        
    
    def mostrar_stock(self): # funcion para mostrar los datos
        if not self.my_stock:
            print("No hay productos en el inventario \nReabastezca el Inventario")
        else:
            for key, value in self.my_stock.items(): 
                print(f"Nombre: {value['nombre']}, Precio: {value['precio']}, Cantidad: {value['cantidad']}, CLiente: {value['cliente']}") 
                print("--------------------------------------------")


    def comprar(self): # funcion para mostrar los productos 
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad a comprar: "))
        cliComprador = input("Nombre del cliente: ")
        if nombre in self.my_stock: # un  if para comprobar si hay ese producto para ejecutar la compra
            if self.my_stock[nombre]["cantidad"] >= cantidad: 
                self.my_stock[nombre]["cantidad"] -= cantidad
                self.productos_comprados.append((nombre, cantidad)) 
                self.total += self.my_stock[nombre]["precio"] * cantidad 
                print(f"{cliComprador} ha comprado {cantidad} unidades de {nombre}")
            else:
                print(f"No hay suficiente stock de {nombre}")
        else: 
            print(f"No hay {nombre} en el inventario")

        # Resumen de la compra
        print("\nResumen de la compra:")
        for producto, cantidad in self.productos_comprados: 
            print(f"{producto}: {cantidad} x {self.my_stock[producto]['precio']} = {self.my_stock[producto]['precio'] * cantidad}") 
        print(f"Total: {self.total}") 
        cash = float(input("Ingrese el efectivo: ")) # Solicito el efectivo
        if cash >= self.total: 
            cambio = cash - self.total 
            print(f"Cambio: {round(cambio,2)}")
        else:
            print("No hay suficiente efectivo.")
            

    def menu(self): # el menu
        while True:
            print("---------------------")
            print("BIENVENIDO")
            print("---------------------")
            print("\nMenu:")
            print("1. Ingresar productos")
            print("2. Mostrar stock")
            print("3. Ingresar proveedor")
            print("4. Mostrar proveedores")
            print("5. Comprar")
            print("6. Salir")
            print("------------------------")
            opcion = input("Ingrese una opcion: ") # opcion ayuda al usuario a esocger que hacer
            match opcion: # matcheo esa opcion, para ejecutar una sentencia dependiendo el caso
                case "1": 
                    print("------------------------")
                    self.ingresar_producto()
                case "2": 
                    print("------------------------")
                    self.mostrar_stock()
                case "3":
                    print("------------------------")
                    self.ingresarProveedor()
                case "4":
                    print("------------------------")
                    self.mostrar_proveedores()
                case "5": 
                    print("------------------------")
                    self.comprar()
                case "6":
                    print("------------------------")
                    print("Gracias por utilizar el sistema de inventario")
                    break 
                case _:
                    print("------------------------")
                    print("Opcion invalida. Por favor, ingrese una opcion valida.")
                    continue 
tienda = tienda() 
tienda.menu()