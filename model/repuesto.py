from model.producto import Producto

class RepuestoEnStock(Producto):
    LIMITE_STOCK = 3
    def __init__(self,nombre:str,marca:str,modelo:str,cantidad:int,precio:float):
        super().__init__(nombre,marca)
        self.modelo = modelo
        self.stock = cantidad
        self.precio = precio
        
    def verificar_stock(self):
        return self.stock < RepuestoEnStock.LIMITE_STOCK

    def set_nombre(self,nombre):
        self.nombre = nombre
    def get_nombre(self):
        return self.nombre

    def set_marca(self,marca):
        self.marca = marca
    def get_marca(self):
        return self.marca

    def set_modelo(self,modelo):
        self.modelo = modelo
    def get_modelo(self):
        return self.modelo

    def set_stock(self,stock):
        self.stock = stock
    def get_stock(self):
        return self.stock

    def set_precio(self,precio):
        self.precio = precio
    def get_precio(self):
        return self.precio

    def __str__(self) -> str:
        return f"Hay {self.stock} unidades del {self.nombre} marca {self.marca}, modelo {self.modelo}"
    
