from model.producto_en_stock import ProductoEnStock 

class RepuestoEnStock(ProductoEnStock):
    
    def __init__(self,nombre,marca,modelo,stock,precio):
        super().__init__(nombre,marca,stock,precio)
        self.modelo = modelo
        
    

    def set_modelo(self,modelo):
        self.modelo = modelo
    def get_modelo(self):
        return self.modelo

    

    def __str__(self) -> str:
        return f"{super().__str__()}, Modelo: {self.modelo}"
    
