import tkinter as tk
from tkinter import ttk

class equipo:#Clase de equipo, puede llamar a las clases de insertar y modificar
    def __init__(self, root, db):
        self.db = db
        self.data = []
        
        # Toplevel es una ventana que está un nivel arriba que la principal
        self.root = tk.Toplevel() 
        self.root.geometry('600x400')
        self.root.title("Equipos")
        self.root.resizable(width=0, height=0)
        
        # toplevel modal
        self.root.transient(root)
        
        #
        self.config_treeview_jugador()
        self.config_buttons_jugador()
        
    def config_treeview_jugador(self):#Se configura el treeview
        self.treeview = ttk.Treeview(self.root)
        self.treeview.configure(columns = ("#1", "#2"))
        self.treeview.heading("#0", text = "Id")
        self.treeview.heading("#1", text = "Equipo")
        self.treeview.heading("#2", text = "Puntos")
        self.treeview.column("#0", minwidth = 50, width = 50, stretch = False)
        self.treeview.column("#1", minwidth = 275, width = 275, stretch = False)
        self.treeview.column("#2", minwidth = 275, width = 275, stretch = False)
        self.treeview.place(x = 0, y = 0, height = 350, width = 600)
        self.llenar_treeview_equipo()
        
    def config_buttons_jugador(self):#Botones de insertar, modificar y eliminar
        tk.Button(self.root, text="Insertar equipo", 
            command = self.insertar_equipo).place(x = 0, y = 350, width = 200, height = 50)
        tk.Button(self.root, text="Modificar equipo", 
            command = self.modificar_equipo).place(x = 200, y = 350, width = 200, height = 50)
        tk.Button(self.root, text="Eliminar equipo", 
            command = self.eliminar_equipo).place(x = 400, y = 350, width = 200, height = 50)
        
    def llenar_treeview_equipo(self):#Se llena el treeview de datos. 
        sql = "select * from equipo"
        # Ejecuta el select
        data = self.db.run_select(sql)
        
        # Si la data es distina a la que hay actualmente...
        if(data != self.data):
            # Elimina todos los rows del treeview
            self.treeview.delete(*self.treeview.get_children())
            for i in data:
                #Inserta los datos
                self.treeview.insert("", "end", text = i[0], 
                                    values = (i[1], i[2]), iid = i[0])
            self.data = data#Actualiza la data

    def insertar_equipo(self):
        insertar_equipo(self.db, self)

    def modificar_equipo(self):
        sql = "select * from equipo where id_equipo = %(id_equipo)s"
        row_data = self.db.run_select_filter(sql, {"id_equipo": self.treeview.focus()})[0]
        modificar_equipo(self.db, self, row_data)

    def eliminar_equipo(self):
        sql = "delete from equipo where id_equipo = %(id_equipo)s"
        self.db.run_sql(sql, {"id_equipo": self.treeview.focus()})
        self.llenar_treeview_equipo()

class insertar_equipo:#Clase para insertar data
    def __init__(self, db, padre):
        self.padre = padre
        self.db = db
        self.insert_datos = tk.Toplevel()
        self.config_window()
        self.config_label()
        self.config_entry()
        self.config_button()

    def config_window(self):#Settings
        self.insert_datos.geometry('200x90')
        self.insert_datos.title("Insertar equipo")
        self.insert_datos.resizable(width=0, height=0)
    
    def config_label(self):#Labels
        tk.Label(self.insert_datos, text =  "Equipo: ").place(x = 10, y = 10, width = 80, height = 20)
        tk.Label(self.insert_datos, text =  "Puntos: ").place(x = 10, y = 40, width = 80, height = 20)
    
    def config_entry(self):#Se configuran los inputs
        self.entry_nombre = tk.Entry(self.insert_datos)
        self.entry_nombre.place(x = 110, y = 10, width = 80, height = 20)
        self.entry_puntos = tk.Entry(self.insert_datos)
        self.entry_puntos.place(x = 110, y = 40, width = 80, height = 20)

    def config_button(self):#Se configura el boton
        tk.Button(self.insert_datos, text = "Aceptar", 
            command = self.insertar).place(x=0, y =70, width = 200, height = 20)

    def insertar(self): #Insercion en la base de datos. 
        sql = """insert equipo (nom_equipo, puntos) values (%(nom_equipo)s, %(puntos)s)"""
        self.db.run_sql(sql, {"nom_equipo": self.entry_nombre.get(), 
                            "puntos": int(self.entry_puntos.get())})
        self.insert_datos.destroy()
        self.padre.llenar_treeview_equipo()

class modificar_equipo:#Clase para modificar
    def __init__(self, db, padre, row_data):
        self.padre = padre
        self.db = db
        self.row_data = row_data
        self.insert_datos = tk.Toplevel()
        self.config_window()
        self.config_label()
        self.config_entry()
        self.config_button()

    def config_window(self):#Configuración de la ventana. 
        self.insert_datos.geometry('200x90')
        self.insert_datos.title("Insertar equipo")
        self.insert_datos.resizable(width=0, height=0)
    
    def config_label(self):#Se configuran las etiquetas.
        tk.Label(self.insert_datos, text =  "Equipo: ").place(x = 10, y = 10, width = 80, height = 20)
        tk.Label(self.insert_datos, text =  "Puntos: ").place(x = 10, y = 40, width = 80, height = 20)
    
    def config_entry(self):#Se configuran los inputs
        self.entry_nombre = tk.Entry(self.insert_datos)
        self.entry_nombre.place(x = 110, y = 10, width = 80, height = 20)
        self.entry_puntos = tk.Entry(self.insert_datos)
        self.entry_puntos.place(x = 110, y = 40, width = 80, height = 20)
        self.entry_nombre.insert(0, self.row_data[1])
        self.entry_puntos.insert(0, self.row_data[2])

    def config_button(self): #Botón aceptar, llama a la función modificar cuando es clickeado. 
        tk.Button(self.insert_datos, text = "Aceptar", 
            command = self.modificar).place(x=0, y =70, width = 200, height = 20)

    def modificar(self): #Insercion en la base de datos. 
        sql = """update equipo set nom_equipo = %(nom_equipo)s, puntos = %(puntos)s 
                where id_equipo = %(id_equipo)s"""
        self.db.run_sql(sql, {"nom_equipo": self.entry_nombre.get(), 
            "puntos": int(self.entry_puntos.get()), "id_equipo": int(self.row_data[0])})
        self.insert_datos.destroy()
        self.padre.llenar_treeview_equipo()
