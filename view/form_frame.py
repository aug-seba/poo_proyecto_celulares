import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from controller.controller import Controller
from model.repuesto import RepuestoEnStock
from model.productoVendido import RepuestoVendido
from model.carrito_compras import CarritoCompras
from model.venta import Venta




class FormFrame(tk.Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.configure(padx=10, pady=10,background="lightgray")
        self.controller = Controller()
        self.carrito_compras = CarritoCompras()
        
        self.pack()
        
        
        
        self._build_form()
        self.build_list_box()
        self.build_tree()
        

    def _build_form(self):
        self.vars = {
            'descripcion': tk.StringVar(),
            'marca': tk.StringVar(),
            'modelo': tk.StringVar(),
            'cantidad': tk.IntVar(),
            'precio': tk.DoubleVar()
        }
        label_frame = tk.LabelFrame(self,text="Formulario de registro de repuestos",relief="groove",borderwidth=5,background="lightblue")
        
        label_frame.grid(column=0, row=0, padx=10, pady=10,sticky="we")
        ttk.Label(label_frame, text='Descripcion:').grid(row=0, column=1,padx=5,pady=5)
        ttk.Entry(label_frame, textvariable=self.vars['descripcion']).grid(row=0, column=2,padx=5, pady=5)
        ttk.Label(label_frame, text='Marca:').grid(row=1, column=1,padx=5, pady=5)
        ttk.Entry(label_frame, textvariable=self.vars['marca']).grid(row=1, column=2,padx=5, pady=5)
        ttk.Label(label_frame, text='Modelo:').grid(row=2, column=1,padx=5, pady=5)
        ttk.Entry(label_frame, textvariable=self.vars['modelo']).grid(row=2, column=2,padx=5, pady=5)
        ttk.Label(label_frame, text='Cantidad:').grid(row=3, column=1,padx=5, pady=5)
        ttk.Entry(label_frame, textvariable=self.vars['cantidad']).grid(row=3, column=2,padx=5, pady=5)
        ttk.Label(label_frame, text='Precio:').grid(row=4, column=1,padx=5, pady=5)
        ttk.Entry(label_frame, textvariable=self.vars['precio']).grid(row=4, column=2,padx=5, pady=5)
        tk.Button(label_frame, text='Agregar producto', command=self._on_submit).grid(row=5, column=1,columnspan=2,sticky="nsew", padx=5, pady=5)
        

    
        

    def _on_submit(self):
        try:
            data = {k: v.get() for k, v in self.vars.items()}
        except tk.TclError as e:
            tk.messagebox.showerror("Error", f"Cantidad y Precio deben ser valores numéricos")
            return
        
        if not all([data['descripcion'],data['marca'],data['modelo']]):
            tk.messagebox.showwarning('validacion','descripcion marca y modelo son obligatorios')
            return
        
        if data['cantidad'] < 0:
            tk.messagebox.showwarning("Validacion","La cantidad debe ser un valor positivo")
            return
        if data['precio'] < 0.0:
            tk.messagebox.showwarning("Validacion","El precio debe ser un valor positivo")
            return
        
        
        
        
        
        registros = self.controller.buscar_registros()
        if registros:
            for registro in registros:
                repuesto = RepuestoEnStock(*registro[1:])
                
                
                if repuesto.get_nombre().lower() == data['descripcion'].lower() and repuesto.get_marca().lower() == data['marca'].lower() and repuesto.get_modelo().lower() == data['modelo'].lower():
                    tk.messagebox.showwarning('Advertencia', 'El producto ya existe en la base de datos.')
                    tk.messagebox.showinfo('Info', 'Se actualizará la cantidad y el precio del producto existente.')
                    self.controller._actualizar_registro(registro[0], 'stock', registro[4] + data['cantidad'])
                    self.controller._actualizar_registro(registro[0], 'precio', data['precio'])
                    self._reset()
                    self.actualizar_arbol(self.controller.buscar_registros())
                    return
        
        tk.messagebox.showinfo('Éxito', '¡Registro completado!')
        repuesto_en_stock = RepuestoEnStock(data['descripcion'],data['marca'],data['modelo'],data['cantidad'],data['precio'])
        self.controller.agregar_repuesto(repuesto_en_stock)
        self._reset()
        self.actualizar_arbol(self.controller.buscar_registros())
        self.add_elements_to_list_box()

    def _reset(self):
        for var in self.vars.values():
            var.set('')

    
        
        
    def build_tree(self):
        tree_frame = tk.Frame(self,background="lightblue")
        
        
        tree_frame.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
        
        self.tree = ttk.Treeview(tree_frame,columns=("categoria","marca","modelo","stock","precio"))
        self.tree.heading("#0",text="codigo")
        self.tree.heading("categoria",text="categoria")
        self.tree.heading("marca",text="marca")
        self.tree.heading("modelo",text="modelo")
        self.tree.heading("stock",text="stock")
        self.tree.heading("precio",text="precio")


        self.tree.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

        scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=2, sticky="ns")

        self.tree.tag_bind("data_row","<Button-1>", self.get_selected_elements)

        
        
    
    def actualizar_arbol(self,registros):
    
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        for elemento in registros:
            self.tree.insert("","end",text=elemento[0],values=elemento[1:],tags=("data_row",))
        

    def build_list_box(self):
        list_frame = tk.Frame(self,background="lightblue",relief="groove",borderwidth=5,width=100)
        list_frame.grid(row=0, column=1, padx=10, pady=10)
        tk.Label(list_frame, text="Seleccione los productos a visualizar").grid(row=0, column=0,sticky="nsew")
        
        
        
        
        
        
        self.list_box = tk.Listbox(list_frame, width=100, height=10, justify="center")
        self.list_box.grid(row=1, column=0, columnspan=1,sticky="ns", padx=10, pady=10)

        
        '''self.list_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)'''

        scroll = tk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.list_box.yview)
        self.list_box.config(yscrollcommand=scroll.set)

        scroll.grid(row=1, column=1, sticky="ns")
        
        
        
        
        panewindow = tk.PanedWindow(list_frame, orient=tk.HORIZONTAL)
        panewindow.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        boton = tk.Button(list_frame, text="Seleccionar", command=self.recuperar_seleccion)
        panewindow.add(boton)
        boton_mas_vendido = tk.Button(list_frame, text="Repuesto más vendido", command=self.mostrar_producto_mas_vendido)
        panewindow.add(boton_mas_vendido)
        boton_menos_vendido = tk.Button(list_frame, text="Repuesto menos vendido", command=self.mostrar_producto_menos_vendido)
        '''boton_iniciar_venta = tk.Button(list_frame, text="Iniciar venta",command=self.iniciar_venta)'''
        panewindow.add(boton_menos_vendido)
       
        self.list_box.grid(row=1, column=0,sticky="nsew")
        self.add_elements_to_list_box()
    

    def mostrar_producto_mas_vendido(self):
        resultado = self.controller.obtener_producto_mas_vendido()
        
        if resultado:
            descripcion, marca, modelo, total_vendido = resultado
            print(f'Nombre: {descripcion}, marca: {marca}, modelo: {modelo}, total vendido: {total_vendido}')
            
            tk.messagebox.showinfo("Repuesto más vendido", f"Descripción: {descripcion}\nMarca: {marca}\nModelo: {modelo}\nTotal vendido: {total_vendido}")
        else:
            tk.messagebox.showinfo("Repuesto más vendido", "No se encontraron registros de ventas.")

    def mostrar_producto_menos_vendido(self):
        resultado = self.controller.obtener_producto_menos_vendido()
        
        if resultado:
            
            if(len(resultado) == 3):
                descripcion, marca, modelo = resultado
                tk.messagebox.showinfo("Repuesto menos vendido", f"Descripción: {descripcion}\nMarca: {marca}\nModelo: {modelo}\nTotal vendido: 0")
            else:
                descripcion, marca, modelo, total_vendido = resultado
                tk. messagebox.showinfo("Repuesto menos vendido", f"Descripcion: {descripcion}\nMarca: {marca}\nModelo:{modelo}\nTotal vendido: {total_vendido}")
        
        else:
            tk.messagebox.showinfo("Repuesto menos vendido", "No se encontraron registros de ventas.")
        

    def add_elements_to_list_box(self):
        self.list_box.delete(0, tk.END)
        self.list_box.insert("end", "Todos los productos")
            
        for item in self.controller.buscar_valores_no_duplicados("descripción"):
            self.list_box.insert("end", item[0])
        
        
    '''Recupera la seleccion del usuario en la lista'''
    def recuperar_seleccion(self):
        valores =   self.list_box.get(0,tk.END)
        
        opcion = self.list_box.get(self.list_box.curselection()[0])
        if opcion in valores[1:]:
            registros = self.controller.buscar_registros_por_condicion("descripción", opcion)
        else:
            registros = self.controller.buscar_registros()
            if not registros:
                tk.messagebox.showinfo("Info", "No hay productos registrados en la base de datos.")
                return
    
        self.actualizar_arbol(registros)
        self.after(2000,self.recuperar_seleccion)

    def get_selected_elements(self,event):
        item_id = self.tree.identify_row(event.y)
        item_details = self.tree.item(item_id)
        codigo = item_details['text']
        
        producto ={'descripcion': tk.StringVar(self,item_details['values'][0]),
                        'marca': tk.StringVar(self,item_details['values'][1]),
                        'modelo': tk.StringVar(self,item_details['values'][2]),
                        'stock': tk.IntVar(self,int(item_details['values'][3])),
                        'precio': tk.DoubleVar(self,float(item_details['values'][4]))
                        }
        
        data = {k: v.get() for k, v in producto.items()}
        
        
        
        topLevel = tk.Toplevel(self)
        label_frame = tk.LabelFrame(topLevel,text="Repuesto seleccionado")
        label_frame.pack(padx=10,pady=10)
        ttk.Label(label_frame, text='Descripcion:').grid(row=0, column=0)
        ttk.Entry(label_frame, textvariable=producto['descripcion']).grid(row=0, column=1)
        ttk.Label(label_frame, text='Marca:').grid(row=1, column=0)
        ttk.Entry(label_frame, textvariable=producto['marca']).grid(row=1, column=1)
        ttk.Label(label_frame, text='Modelo:').grid(row=2, column=0)
        ttk.Entry(label_frame, textvariable=producto['modelo']).grid(row=2, column=1)
        ttk.Label(label_frame, text='Cantidad:').grid(row=3, column=0)
        ttk.Entry(label_frame, textvariable=producto['stock']).grid(row=3, column=1)
        ttk.Label(label_frame, text='Precio:').grid(row=4, column=0)
        ttk.Entry(label_frame, textvariable=producto['precio']).grid(row=4, column=1)

        tk.Button(topLevel,text="Eliminar",command= lambda: self._confirmar_eliminacion(codigo,topLevel)).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(topLevel,text="Actualizar",command= lambda: self._actualizar_producto(codigo,producto,data,topLevel)).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(topLevel,text="AgregarAlCarrito",command= lambda: self._agregar_al_carrito(codigo,data,producto,topLevel)).pack(side=tk.LEFT, padx=10, pady=10)
        
        
        self.tree.selection_set(item_id)
        self.tree.focus(item_id)

    
        
    def _confirmar_eliminacion(self, codigo, topLevel):
        opcion = messagebox.askquestion("info", "Estas seguro de eliminar este producto?")
        if opcion == "yes":
            self.controller.borrar_registro(codigo)
            self.actualizar_arbol(self.controller.buscar_registros())
            self.add_elements_to_list_box()
        topLevel.destroy()

    def _actualizar_producto(self, codigo, producto, data, topLevel):
        for k1, v1, k2, v2 in zip(producto.keys(), producto.values(), data.keys(), data.values()):
            try:
                if v1.get() != v2:
                    print(f'El valor de {k1} es {producto[k1].get()}  el valor de {k2} es {data[k2]}')
                    column_to_update = k1
                    value_to_update = producto[k1].get()
                    self.controller._actualizar_registro(codigo, column_to_update, value_to_update)
            except tk.TclError:
                tk.messagebox.showerror("Error", f'valor invalido para {k1}')
                return
        tk.messagebox.showinfo("Info","Producto Actualizado exitosamente")
        topLevel.destroy()
        self.actualizar_arbol(self.controller.buscar_registros())

    def finalizar_compra(self):
        tk.messagebox.showinfo("Info", "La compra ha sido finalizada. No se pueden agregar más productos al carrito.")
        tk.messagebox.showinfo("Total de ventas", f"El total de ventas para este carrito es: $ {self.carrito_compras.obtener_total_ventas()}")
        self.carrito_compras.vaciar_carrito()

    def _agregar_al_carrito(self, codigo, data, producto, toplevel):
        try:
            repuesto_vendido = RepuestoVendido(
                        producto['descripcion'].get(),
                        producto['marca'].get(),
                        producto['modelo'].get(),
                        data['stock'],
                        producto['precio'].get(),
                        producto['stock'].get()) 
                

            if not all([producto['descripcion'].get(),producto['marca'].get(),producto['modelo'].get()]):
                tk.messagebox.showwarning('validacion','descripcion marca y modelo son obligatorios')
                return
            if data['stock'] < producto['stock'].get():
                tk.messagebox.showwarning("Advertencia", "No hay stock disponible para este producto.")
                return
            if producto['stock'].get() < 0 or producto['precio'].get() < 0:
                tk.messagebox.showinfo("info","Cantidad vendida y precio de venta deben ser valores positivos")
                return
            repuesto = RepuestoEnStock(*data.values())
            print(f'estos son los valores para: {repuesto}')
        except tk.TclError as e:
            tk.messagebox.showerror('Error',"cantidad vendida y precio de venta deben ser valores numericos")
            return
            '''print(repuesto)'''

            
            
        


        self.carrito_compras.agregar_producto(repuesto_vendido)
        tk.messagebox.showinfo("Info", "Repuesto agregado al carrito de compras.")
        self.controller._actualizar_registro(codigo, 'stock', repuesto.get_stock() - repuesto_vendido.get_cantidad_vendida())
        repuesto.set_stock(repuesto.get_stock()-repuesto_vendido.get_cantidad_vendida())
        if(repuesto.verificar_stock()):
            tk.messagebox.showwarning("Alert",f'Stock bajo para el producto {repuesto.get_nombre()} {repuesto.get_marca()} {repuesto.get_modelo()}')
        venta = Venta(codigo,repuesto_vendido.get_cantidad_vendida(),repuesto_vendido.get_precio(),repuesto_vendido.get_cantidad_vendida()*repuesto_vendido.get_precio())
        self.controller.agregar_venta(venta)
        '''ACA PODRIAMOS AGREGAR EL REGISTRO DE LA VENTA A LA BASE DE DATOS, SI ES QUE QUEREMOS LLEVAR UN REGISTRO DE LAS VENTAS'''
        eleccion = tk.messagebox.askquestion("Info", "¿Desea finalizar la compra?", icon='info')

        if eleccion == "yes":
            self.finalizar_compra()
        else:
            tk.messagebox.showinfo("Info", "Seleccione un nuevo producto del panel principal para agregar al carrito.")
            toplevel.destroy()