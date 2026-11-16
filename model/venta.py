class Venta:
    def __init__(self, codigo_producto,cantidad_vendida, precio_unitario, total):
        self.codigo_producto = codigo_producto
        self.cantidad_vendida = cantidad_vendida
        self.precio_unitario = precio_unitario
        self.total = total

    def get_codigo_producto(self):
        return self.codigo_producto
    def set_codigo_producto(self, codigo_producto):
        self.codigo_producto = codigo_producto

    def get_cantidad_vendida(self):
        return self.cantidad_vendida
    def set_cantidad_vendida(self, cantidad_vendida):
        self.cantidad_vendida = cantidad_vendida
    
    def get_precio_unitario(self):
        return self.precio_unitario
    def set_precio_unitario(self, precio_unitario):
        self.precio_unitario = precio_unitario

    def get_total(self):
        return self.total
    def set_total(self, total):
        self.total = total