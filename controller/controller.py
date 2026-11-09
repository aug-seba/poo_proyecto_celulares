import sqlite3
import os
from model.repuesto import RepuestoEnStock
class Controller:
    '''aqui interactuariamos con la base de datos, recuperando y actualizando registros'''
        
    def getConnection(self):
        current_directory = os.getcwd()
        
        db = os.path.join(current_directory,"stock.db")
        connect = sqlite3.connect(db)
        return connect
    
    '''agregamos un registro a la tabla en nuestra base de datos'''   
    def insert(self,repuesto:RepuestoEnStock):
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
    
    '''Busca un registo a partir de su categoria, marca y modelo'''
    def buscar_registro(self,categoria=None,marca=None,modelo=None):
        con = self.getConnection()
        if not all([categoria,marca,modelo]):
                            raise ValueError("la categoria, la marca y el modelo deben ser indicados.")
        try:
            with con:
                cursor = con.cursor()
                query = f'SELECT * FROM repuestos WHERE descripción = ? AND marca = ? AND modelo = ?'
                cursor.execute(query,(categoria,marca,modelo))
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

