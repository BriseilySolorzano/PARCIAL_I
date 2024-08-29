"""
Una tienda local vende diversos productos, cada vez que un cliente hace una compra niña mary se encarga de anotarlo en una libreta. 
A su vez, con una calculadora le da el total a cada cliente y les da su respectivo vuelto en caso de necesitarlo. 
 Niña mary también se encarga de atender a los proveedores que le dan cierta cantidad de producto y un precio sugerido de venta, 
propón una solución dentro de tu programa para ayudarle.
"""

class producto:
    def __init__(self, nombre, precio, cantidad): # creo el constructor
        self.nombre = nombre 
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_datos(self): # muestra los datos organizadamente 
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Cantidad: {self.cantidad}")        
        
class proveedor:
    def __init__(self, nombreProveedor, numContacto, nombreProducto, precioCompra):
        self.nombreProveedor = nombreProveedor
        self.numContacto = numContacto
        self.nombreProducto = nombreProducto
        self.precioCompra = precioCompra
        self.precioSugerido = self.precioSugerido()
        
    def precioSugerido(self):
        return (self.precioCompra*0.25)+self.precioCompra
    
    def mostrar_datos(self):
        print(f"Nombre del proveedor: {self.nombreProveedor}")
        print(f"Numero de contacto: {self.numContacto}")
        print(f"Nombre del producto: {self.nombreProducto}")
        print(f"Precio de compra: {self.precioCompra}")
        print(f"Precio sugerido: {self.precioSugerido()}")