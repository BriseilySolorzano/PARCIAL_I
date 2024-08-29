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
        print(f"Precio sugerido: {self.precioSugerido()}")
        
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
        nombreCli = ("Ingrese el nombre del cliente: ")
        self.my_stock[nombre] = {"nombre": nombre, "precio": precio, "cantidad": cantidad, "cliente":nombreCli}
        print(f"producto {nombre} agregado al inventario.") 
    
    def mostrar_stock(self): # funcion para mostrar los datos
        if not self.my_stock:
            print("No hay productos en el inventario \nReabastezca el Inventario")
        else:
            for key, value in self.my_stock.items(): 
                print(f"Nombre: {value['nombre']}, Precio: {value['precio']}, Cantidad: {value['cantidad']}, CLiente: {value['cliente']}") 
                print("--------------------------------------------")
