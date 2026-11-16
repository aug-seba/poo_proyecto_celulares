from model.producto import Producto
from model.repuesto import RepuestoEnStock


class RepuestoVendido(RepuestoEnStock):
    def __init__(self,nombre,marca,modelo,stock,precio,cantidad_vendida):
        super().__init__(nombre,marca,modelo,stock,precio)
        self.cantidad_vendida = cantidad_vendida
        self.precio_total_venta = self.precio*cantidad_vendida
        
    def set_cantidad_vendida(self,cantidad_vendida):
        self.cantidad_vendida = cantidad_vendida
    def get_cantidad_vendida(self):
        return self.cantidad_vendida

    def set_precio_total_venta(self,precio_total_venta):
        self.precio_total_venta = precio_total_venta
    def get_precio_total_venta(self):
        return self.precio_total_venta

    def __str__(self) -> str:
        return f"Producto vendido: {super().__str__}, Cantidad vendida: {self.cantidad_vendida}, Precio total de venta: {self.precio_total_venta}"