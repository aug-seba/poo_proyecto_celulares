class Producto:
    def __init__(self, nombre, marca):
        self.nombre = nombre
        self.marca = marca

    def set_nombre(self, nombre):
        self.nombre = nombre
    def get_nombre(self):
        return self.nombre

    def set_marca(self, marca):
        self.marca = marca
    def get_marca(self):
        return self.marca

    def __str__(self):
        return f"Producto: {self.nombre}, Marca: {self.marca}"