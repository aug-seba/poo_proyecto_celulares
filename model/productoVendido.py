from model.producto import Producto

class ProductoVendido(Producto):
    def __init__(self, nombre,marca,modelo,cantidad_vendida,precio_unitario):
        super().__init__(nombre,marca)
        self.modelo = modelo        
        self.cantidad_vendida = cantidad_vendida
        self.precio_unitario = precio_unitario
        self.precio_total_venta = precio_unitario*cantidad_vendida

    def set_modelo(self,modelo):
        self.modelo = modelo
    def get_modelo(self):
        return self.modelo

    def set_cantidad_vendida(self,cantidad_vendida):
        self.cantidad_vendida = cantidad_vendida
    def get_cantidad_vendida(self):
        return self.cantidad_vendida

    def set_precio_unitario(self,precio_unitario):
        self.precio_unitario = precio_unitario
    def get_precio_unitario(self):
        return self.precio_unitario

    def set_precio_total_venta(self,precio_total_venta):
        self.precio_total_venta = precio_total_venta
    def get_precio_total_venta(self):
        return self.precio_total_venta

    def __str__(self) -> str:
        return f"Producto vendido: {super().__str__}, Modelo: {self.modelo}, Cantidad vendida: {self.cantidad_vendida}, Precio unitario: {self.precio_unitario}, Precio total de venta: {self.precio_total_venta}"