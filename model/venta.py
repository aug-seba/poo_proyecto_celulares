class Venta:
    def __init__(self, codigo_producto,cantidad, precio_unitario, total):
        self.codigo_producto = codigo_producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.total = total

    def get_codigo_producto(self):
        return self.codigo_producto
    def set_codigo_producto(self, codigo_producto):
        self.codigo_producto = codigo_producto

    def get_descripcion(self):
        return self.descripcion
    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def get_cantidad(self):
        return self.cantidad
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio_unitario(self):
        return self.precio_unitario
    def set_precio_unitario(self, precio_unitario):
        self.precio_unitario = precio_unitario

    def get_total(self):
        return self.total
    def set_total(self, total):
        self.total = total