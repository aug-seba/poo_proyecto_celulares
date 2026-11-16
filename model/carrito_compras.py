from model.productoVendido import RepuestoVendido
class CarritoCompras:
    def __init__(self):
        self.productos_vendidos = []
        self.total_ventas = 0.0

    def agregar_producto(self, producto_vendido: RepuestoVendido):
        self.productos_vendidos.append(producto_vendido)
        self.total_ventas += producto_vendido.get_precio_total_venta()

    def obtener_total_ventas(self):
        return self.total_ventas

    def vaciar_carrito(self):
        self.productos_vendidos.clear()
        self.total_ventas = 0.0

    def __str__(self):
        productos_str = "\n".join(str(producto) for producto in self.productos_vendidos)
        return f"Carrito de Compras:\n{productos_str}\nTotal de Ventas: {self.total_ventas}"
