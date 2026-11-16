import sqlite3
import os
from model.repuesto import RepuestoEnStock
from model.venta import Venta

class Controller:
    '''aqui interactuariamos con la base de datos, recuperando y actualizando registros'''
        
    def getConnection(self):
        current_directory = os.getcwd()
        
        db = os.path.join(current_directory,"stock.db")
        connect = sqlite3.connect(db)
        return connect

    def create_table(self):
        con = self.getConnection()
        try:
            with con:
                cursor = con.cursor()
                query = f'''CREATE TABLE IF NOT EXISTS repuestos(
                    id_prod INTEGER PRIMARY KEY,
                    descripción TEXT NOT NULL,
                    marca TEXT NOT NULL,
                    modelo TEXT NOT NULL,
                    stock INTEGER NOT NULL DEFAULT 0,
                    precio REAL NOT NULL DEFAULT 0.0 CHECK(precio >= 0.0)
                )'''
                cursor.execute(query)
        except sqlite3.IntegrityError as e:
            print(f'Error de Integridad {e}')
        finally:
            con.close()

    def create_table_ventas(self):
            con = self.getConnection()
            try:
                with con:
                    cursor = con.cursor()
                    query = f'''CREATE TABLE IF NOT EXISTS ventas(
                        id_venta INTEGER PRIMARY KEY,
                        id_prod INTEGER NOT NULL,
                        cantidad INTEGER NOT NULL,
                        precio_unitario REAL NOT NULL,
                        total REAL NOT NULL,
                        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (id_prod) REFERENCES repuestos(id_prod)
                    )'''
                    cursor.execute(query)
            except sqlite3.IntegrityError as e:
                print(f'Error de Integridad {e}')
            finally:
                con.close()
                        
    
    '''agregamos un registro a la tabla en nuestra base de datos'''   
    def agregar_repuesto(self,repuesto:RepuestoEnStock):
        con = self.getConnection()
        try:
            with con:
                cursor = con.cursor()

                query = f"INSERT INTO repuestos(descripción,marca,modelo,stock,precio)VALUES(?,?,?,?,?)"
                cursor.execute(query,(repuesto.get_nombre(),repuesto.get_marca(),repuesto.get_modelo(),repuesto.get_stock(),repuesto.get_precio()))
        except sqlite3.IntegrityError as e:
            print(f'Error de Integridad {e}')
        finally:
            con.close()
        
        
        print("registro agregado")

    def agregar_venta(self,venta:Venta):
            con = self.getConnection()
            try:
                with con:
                    cursor = con.cursor()
    
                    query = f"INSERT INTO ventas(id_prod,cantidad,precio_unitario,total)VALUES(?,?,?,?)"
                    cursor.execute(query,(venta.get_codigo_producto(),venta.get_cantidad_vendida(),venta.get_precio_unitario(),venta.get_total()))
            except sqlite3.IntegrityError as e:
                print(f'Error de Integridad {e}')
            finally:
                con.close()
        
    '''devuelve todos los registros de la table'''    
    def buscar_registros(self):
        
            con = self.getConnection()
            try:
                with con:
                    cursor = con.cursor()
                    query = f'SELECT * FROM repuestos'
                    cursor.execute(query)
                    registros = cursor.fetchall()
                    return registros
            except sqlite3.IntegrityError as e:
                print(f'Error de Integridad {e}')
            finally:
                con.close()
    def buscar_registro_por_codigo(self, codigo):
        con = self.getConnection()
        try:
            with con:
                cursor = con.cursor()
                query = 'SELECT * FROM repuestos WHERE id_prod = ?'
                cursor.execute(query, (codigo,))
                registro = cursor.fetchall()
                return registro
        except sqlite3.IntegrityError as e:
            print(f'Error de Integridad {e}')
        finally:
            con.close()

    def buscar_registro(self, categoria=None, marca=None, modelo=None):
        con = self.getConnection()
        if not all([categoria, marca, modelo]):
            raise ValueError("la categoria, la marca y el modelo deben ser indicados.")
        try:
            with con:
                cursor = con.cursor()
                query = 'SELECT * FROM repuestos WHERE descripción = ? AND marca = ? AND modelo = ?'
                cursor.execute(query, (categoria, marca, modelo))
                registros = cursor.fetchall()
                return registros
        except sqlite3.IntegrityError as e:
            print(f'Error de Integridad {e}')
        finally:
            con.close()
    
    '''obtenemos valores no duplicados de una determinada columna'''
    def buscar_valores_no_duplicados(self,column_to_select):
        con = self.getConnection()
        try:
            with con:
                cursor = con.cursor()
                if not column_to_select:
                    raise ValueError("Debe indicar la columna")
                query = f'SELECT DISTINCT {column_to_select} FROM repuestos'
                cursor.execute(query)
                registros = cursor.fetchall()
                
                return registros
        except sqlite3.IntegrityError as e:
            print("Error de integridad {e}")
            
        finally:
            con.close()

    def buscar_registros_por_condicion(self,*args):
        column,value = args
        
        con = self.getConnection()
        try:
            with con:
                    cursor = con.cursor()
                    query = f'SELECT * FROM repuestos WHERE {column}=?'
                    cursor.execute(query,(value,))
                    registros = cursor.fetchall()
                    return registros
        except sqlite3.IntegrityError as e:
                print("Error de integridad {e}")
                    
        finally:
                con.close()
    '''actualiza un registro determinado'''            
    def actualizar_registro(self,id,repuesto:Repuesto):
        con = self.getConnection()
        try:
            with con:
                cursor = con.cursor()
                if not all([repuesto.descripcion, repuesto.marca, repuesto.modelo]):
                    raise ValueError("la columna a actualizar y la condicion no pueden faltar")
    
                query = f"UPDATE repuestos set descripción = ?, marca = ?, modelo = ?, stock = ?, precio = ? WHERE id_prod = ?"
                cursor.execute(query,(str(repuesto.descripcion), str(repuesto.marca), str(repuesto.modelo), repuesto.stock, repuesto.precio, id))
        except sqlite3.IntegrityError as e:
            print(f'Error de Integridad {e}')
        finally:
            con.close()

    def obtener_producto_mas_vendido(self):
        con = self.getConnection()
        try:
            with con:
                cursor = con.cursor()
                query = f'''
                    SELECT r.descripción, r.marca, r.modelo, SUM(v.cantidad) AS total_vendido
                    FROM repuestos r
                    JOIN ventas v ON r.id_prod = v.id_prod
                    GROUP BY r.id_prod
                    ORDER BY total_vendido DESC
                    LIMIT 1
                    
                '''
                cursor.execute(query)
                resultado = cursor.fetchone()
                return resultado
        except sqlite3.IntegrityError as e:
            print(f'Error de Integridad {e}')
        finally:
            con.close()

    def obtener_producto_menos_vendido(self):
        con = self.getConnection()
        try:
            with con:
                cursor = con.cursor()
                query = f'''SELECT descripción,marca,modelo FROM repuestos
                            WHERE id_prod NOT IN(SELECT id_prod FROM ventas)
                            '''
                
                cursor.execute(query)
                resultado = cursor.fetchone()
                print(resultado)

                if resultado:
                    print("Estoy aca")
                    print("Hola")
                    return resultado
                else:
                    print("Estoy aqui")
                    print("Chau")
                    query = f'''
                                SELECT r.descripción, r.marca, r.modelo, SUM(v.cantidad) AS total_vendido
                                FROM repuestos r
                                JOIN ventas v ON r.id_prod = v.id_prod
                                GROUP BY r.id_prod
                                ORDER BY total_vendido ASC
                                LIMIT 1
                                        
                                    '''
                    cursor.execute(query)
                    resultado = cursor.fetchone()
                    print(resultado)
                    return resultado
        except sqlite3.IntegrityError as e:
            print(f'Error de Integridad {e}')
        finally:
            con.close()

    def _actualizar_registro(self,id,column_to_update,value_to_update):
        con = self.getConnection()
        try:
            with con:
                cursor = con.cursor()
                '''if not all([repuesto['descripcion'], repuesto['marca'], repuesto['modelo']]):
                    raise ValueError("la columna a actualizar y la condicion no pueden faltar")'''

                query = f"UPDATE repuestos set {column_to_update} = ? WHERE id_prod = ?"
                cursor.execute(query,(value_to_update, id))
        except sqlite3.IntegrityError as e:
            print(f'Error de Integridad {e}')
        finally:
            con.close()
            
    '''elimina un registro de la tabla'''
    def borrar_registro(self,id):
        con = self.getConnection()
        try:
            with con:
                cursor = con.cursor()
                if not id:
                    raise ValueError("debo especificar id de producto")

                query = f"DELETE from repuestos WHERE id_prod = {id}"
                cursor.execute(query)
        except sqlite3.IntegrityError as e:
            print(f'Error de Integridad {e}')
        finally:
            con.close()

