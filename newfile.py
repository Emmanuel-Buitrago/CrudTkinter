#------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ESTUDIANTE
#
# Created:     04/05/2023
# Copyright:   (c) ESTUDIANTE 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()
import tkinter as tk
import sqlite3
from tkinter import ttk
#crear la base
def crear():
    uno = sqlite3.connect("inpahu.db")
    resp = "Se ha creado la base de datos"
    imprimir_respuesta(resp)
#conectar tabla
def tabla():
    uno = sqlite3.connect("inpahu.db")
    cursor = uno.cursor()
    cursor.execute("create table if not exists estudiante (codigo int, nombre varchar(40), fecha date, genero varchar (1));")
    resp = "Se ha creado la tabla estudiante en caso de que no exista"
    imprimir_respuesta(resp)
    uno.commit()
#cargue llenado registros iniciales a la tabla
def cargue():
    uno = sqlite3.connect("inpahu.db")
    cursor = uno.cursor()
    cursor.execute("insert into estudiante values ( 100,'marta', '2019-05-02','f');")
    cursor.execute("insert into estudiante values ( 200,'paola','2015-06-01' ,'f');")
    cursor.execute("insert into estudiante values ( 300,'pedro','2020-07-02' ,'m');")
    cursor.execute("insert into estudiante values ( 400,'pablo','2018-07-04' ,'m');")
    cursor.execute("insert into estudiante values ( 500,'plutarco','2023-07-04' ,'m');")
    resp = "Se han cargado los datos iniciales"
    imprimir_respuesta(resp)
    uno.commit()
#mostrar tabla
def reporte():
    uno = sqlite3.connect("inpahu.db")
    cursor = uno.cursor()
    cursor.execute("select * from estudiante")
    data = cursor.fetchall()  # Fetch all rows from the query result
    if cursor==None:
        resp = "No hay estudiantes"
        imprimir_respuesta(resp)
        return None
    # Create the Tkinter window
    window = tk.Tk()
    window.title('Estudiantes')
    icono_grande = tk.PhotoImage(file="LOGO-UNINPAHU.png")
    window.iconphoto(False, icono_grande)
    # Create a treeview widget
    tree = ttk.Treeview(window)
    tree['columns'] = tuple(range(len(data[0]))) # Set the number of columns
    tree.column('#0', width=0, stretch=tk.NO)
    # Add columns to the treeview
    for i in range(len(data[0])):
        tree.column(i, width=100, anchor='center')
    tree.heading(i, text=f'Column {i+1}')
    tree.heading('0', text='Codigo')
    tree.heading('1', text='Nombre')
    tree.heading('2', text='Fecha')
    tree.heading('3', text='Genero')

    tree.pack()

    # Insert data rows into the treeview
    for row in data:
        tree.insert('', 'end', values=row)

    resp = "Se ha realizado la consulta de todos los estudiantes"
    imprimir_respuesta(resp)
    uno.commit()
#eliminar registro en tabla
def eliminar():
    estudiante = sqlite3.connect("inpahu.db")
    cursor = estudiante.cursor()
    cod=int(entry_cod.get())
    cursor.execute(f"DELETE from estudiante where codigo={cod}")
    resp = f"Se ha eliminado al estudiante {cod}"
    imprimir_respuesta(resp)
    estudiante.commit()
#insertar registro en la tabla
def insertar():
    uno = sqlite3.connect("inpahu.db")
    cursor = uno.cursor()
    cod = int(entry_cod.get())
    nom = str(entry_nom.get())
    fecha = str(entry_fecha.get())
    genero = str(entry_genero.get())
    resp = "Se han ingresado los datos"
    imprimir_respuesta(resp)
    cursor.execute("INSERT INTO estudiante VALUES('%s','%s','%s','%s')" % (cod,nom,fecha,genero))
    uno.commit()
#actualizar tabla por fecha
def actualizar():
    uno = sqlite3.connect("inpahu.db")
    cursor = uno.cursor()
    cod = int(entry_cod.get())
    codOld = int(entry_codOld.get())
    nom = str(entry_nom.get())
    fecha = str(entry_fecha.get())
    genero = str(entry_genero.get())
    resp = "Se han actualizado los datos"
    imprimir_respuesta(resp)
    print(fecha)
    #get all data from entry
    cursor. execute(f"update estudiante set fecha = '{fecha}', codigo = {cod}, nombre = '{nom}', genero = '{genero}' where codigo = {codOld} ")
    uno.commit()
def consultar():
    uno = sqlite3.connect("inpahu.db")
    cursor = uno.cursor()
    nom = str(entry_nom.get())
    cursor.execute(f"select * from estudiante where nombre='{nom}'")
    data = cursor.fetchall()  # Fetch all rows from the query result
    if cursor==None:
        resp = "No hay estudiantes con ese nombre"
        imprimir_respuesta(resp)
        return None
    # Create the Tkinter window
    window = tk.Tk()
    window.title(f'Estudiantes con el nombre {nom}')
    icono_grande = tk.PhotoImage(file="LOGO-UNINPAHU.png")
    window.iconphoto(False, icono_grande)

    # Create a treeview widget
    tree = ttk.Treeview(window)
    tree['columns'] = tuple(range(len(data[0]))) # Set the number of columns
    tree.column('#0', width=0, stretch=tk.NO)
    # Add columns to the treeview
    for i in range(len(data[0])):
        tree.column(i, width=100, anchor='center')
    tree.heading(i, text=f'Column {i+1}')
    tree.heading('0', text='Codigo')
    tree.heading('1', text='Nombre')
    tree.heading('2', text='Fecha')
    tree.heading('3', text='Genero')

    tree.pack()

    # Insert data rows into the treeview
    for row in data:
        tree.insert('', 'end', values=row)

    resp = "Se ha realizado la consulta de todos los estudiantes con el nombre "+str(nom)
    imprimir_respuesta(resp)
    uno.commit()
def consultaCod():
    uno = sqlite3.connect("inpahu.db")
    cursor = uno.cursor()
    cod = int(entry_cod.get())
    cursor.execute(f"select * from estudiante where codigo={cod}")
    data = cursor.fetchall()  # Fetch all rows from the query result
    if cursor==None:
        resp = "No hay estudiantes con ese codigo"
        imprimir_respuesta(resp)
        return None
    # Create the Tkinter window
    window = tk.Tk()
    window.title(f'Estudiantes con el codigo{cod}')
    icono_grande = tk.PhotoImage(file="LOGO-UNINPAHU.png")
    window.iconphoto(False, icono_grande)

    # Create a treeview widget
    tree = ttk.Treeview(window)
    tree['columns'] = tuple(range(len(data[0]))) # Set the number of columns
    tree.column('#0', width=0, stretch=tk.NO)
    # Add columns to the treeview
    for i in range(len(data[0])):
        tree.column(i, width=100, anchor='center')
    tree.heading(i, text=f'Column {i+1}')
    tree.heading('0', text='Codigo')
    tree.heading('1', text='Nombre')
    tree.heading('2', text='Fecha')
    tree.heading('3', text='Genero')

    tree.pack()

    # Insert data rows into the treeview
    for row in data:
        tree.insert('', 'end', values=row)

    resp = "Se ha realizado la consulta de todos los estudiantes con el codigo "+str(cod)
    imprimir_respuesta(resp)
    uno.commit()
def salir():
    #print ("muchas gracias por particpiar")
    #print ("El programa se esta cerrando...")
    try:
        db.close()
        exit()
    except:
        exit()
def imprimir_respuesta(respuesta):
    etiqueta_respuesta.config(text=f"{respuesta}")
ventana = tk.Tk()
# Crear campos de entrada
etiqueta_codigo = tk.Label(ventana, text="Ingrese el codigo")
etiqueta_codigo.pack()
entry_cod = tk.Entry(ventana)
entry_cod.pack()
etiqueta_codOld = tk.Label(ventana, text="Ingrese el codigo antiguo")
etiqueta_codOld.pack()
entry_codOld = tk.Entry(ventana)
entry_codOld.pack()
etiqueta_nom = tk.Label(ventana, text="Ingrese el nombre")
etiqueta_nom.pack()
entry_nom = tk.Entry(ventana)
entry_nom.pack()
etiqueta_fecha = tk.Label(ventana, text="Ingrese el fecha")
etiqueta_fecha.pack()
entry_fecha = tk.Entry(ventana)
entry_fecha.pack()
etiqueta_genero = tk.Label(ventana, text="Ingrese el genero")
etiqueta_genero.pack()
entry_genero = tk.Entry(ventana)
entry_genero.pack()

# Crear botÃ³n para sumar nÃºmeros
boton_Create = tk.Button(ventana, text="1 Crear la base", command=crear)
boton_Create.pack()
boton_Table = tk.Button(ventana, text="2 Crear la tabla", command=tabla)
boton_Table.pack()
boton_Cargue = tk.Button(ventana, text="3 Cargue inicial a la tabla", command=cargue)
boton_Cargue.pack()
boton_Reporte = tk.Button(ventana, text="4 Reporte tabla", command=reporte)
boton_Reporte.pack()
boton_Eliminar = tk.Button(ventana, text="5 Eliminar estudiante por nombre", command=eliminar)
boton_Eliminar.pack()
boton_Actualizar = tk.Button(ventana, text="6 Actualizar registro por codigo antiguo", command=actualizar)
boton_Actualizar.pack()
boton_Insertar = tk.Button(ventana, text="7 Insertar registro ", command=insertar)
boton_Insertar.pack()
boton_ConsulCod = tk.Button(ventana, text="8 Consultar por codigo", command=consultaCod)
boton_ConsulCod.pack()
boton_ConsulAll = tk.Button(ventana, text="9 Consultar por nombre", command=consultar)
boton_ConsulAll.pack()
boton_Salir = tk.Button(ventana, text="10 Salir", command=salir)
boton_Salir.pack()
# Crear etiqueta para mostrar resultado
etiqueta_respuesta = tk.Label(ventana, text="")
etiqueta_respuesta.pack()
#Configuracion general de la ventana
ventana.title('CRUD Estudiantes')
ventana.geometry("370x500")
icono_grande = tk.PhotoImage(file="LOGO-UNINPAHU.png")
ventana.iconphoto(False, icono_grande)
ventana.mainloop()