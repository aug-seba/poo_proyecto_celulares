from model.producto import Producto
LIMITE_STOCK = 3
class ProductoEnStock(Producto):
    def __init__(self,nombre, marca, stock, precio):
        super().__init__(nombre, marca)
        self.stock = stock
        self.precio = precio

    def set_stock(self, stock):
        self.stock = stock
    def get_stock(self):
        return self.stock
        
    
    def set_precio(self, precio):
        self.precio = precio
    def get_precio(self):
        return self.precio

    def verificar_stock(self):
            return self.stock < LIMITE_STOCK

    def __str__(self):
        return f"{super().__str__()}, Precio: {self.precio}, Stock: {self.stock}"

