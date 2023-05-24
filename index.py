from tkinter import ttk
from tkinter import *
from tkcalendar import Calendar

import sqlite3

class Product:
    # connection dir property
    db_name = "inpahu.db"

    def __init__(self, window):
        # Initializations
        self.wind = window
        self.wind.title('CRUD Estudiantes')
        self.wind.iconphoto(False, PhotoImage(file="LOGO-UNINPAHU.png"))
        self.wind.geometry("600x470")

        # Creating a Frame Container
        frame = LabelFrame(self.wind, text='Registrar nuevo estudiante')
        frame.grid(row=0, column=1, columnspan=1, pady=20)

        # Name Input
        Label(frame, text='Codigo: ').grid(row=1, column=0)
        self.code = Entry(frame)
        self.code.focus()
        self.code.grid(row=1, column=1)

        # Price Input
        Label(frame, text='Nombre: ').grid(row=2, column=0)
        self.name = Entry(frame)
        self.name.grid(row=2, column=1)

        # Name Input
        Label(frame, text='Fecha: ').grid(row=3, column=0)
        self.date_entry = Entry(frame)
        self.date_entry.bind("<Button-1>", lambda event: self.get_date(self.date_entry))
        self.date_entry.grid(row=3, column=1)

        # Price Input
        Label(frame, text='Genero: ').grid(row=4, column=0)
        self.gender = Entry(frame)
        self.gender.grid(row=4, column=1)

        # Button Add Product
        ttk.Button(frame, text='Guardar Estudiante', command=self.add_product).grid(row=5, columnspan=2, sticky=W + E)

        # Output Messages
        self.message = Label(text='', fg='red')
        self.message.grid(row=3, column=0, columnspan=2, sticky=W + E)

        # Table
        self.tree = ttk.Treeview(height=10, columns=(1, 2, 3))
        self.tree.grid(row=6, column=0, columnspan=3)
        self.tree.heading('#0', text='Codigo', anchor=CENTER)
        self.tree.heading('#1', text='Nombre', anchor=CENTER)
        self.tree.heading('#2', text='Fecha', anchor=CENTER)
        self.tree.heading('#3', text='Genero', anchor=CENTER)

        self.tree.column("#0", width=125)
        self.tree.column("#1", width=225)
        self.tree.column("#2", width=175)
        self.tree.column("#3", width=75)

        # Buttons
        ttk.Button(text='MODIFICAR', command=self.edit_product).grid(row=7, column=0)
        ttk.Button(text='MOSTRAR', command=self.get_products).grid(row=7, column=1)
        ttk.Button(text='ELIMINAR', command=self.delete_product).grid(row=7, column=2)

        # Filling the Rows

    # Function to Execute Database Queries
    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    # Get Products from Database
    def get_products(self):
        # Cleaning Table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # Getting data
        query = 'SELECT * FROM estudiante ORDER BY codigo DESC'
        db_rows = self.run_query(query)
        # Filling data
        for row in db_rows:
            self.tree.insert('', 0, text=row[0], values=[row[1], row[2], row[3]])

    def convertir_formato_fecha(self, fecha):
        partes = fecha.split("/")
        dia = partes[0]
        mes = partes[1]
        anio = partes[2]
        fecha_convertida = f"20{anio}-{mes.zfill(2)}-{dia.zfill(2)}"
        return fecha_convertida

    def get_date_from_calendar(self, date):
        date.delete(0, END)
        formato_inicial = self.edit_wind.cal.get_date()
        cambio_form = self.convertir_formato_fecha(formato_inicial)
        date.insert(0, cambio_form)

    def get_date(self, obj):
        self.edit_wind = Toplevel()
        self.edit_wind.title('Edit Product')
        self.edit_wind.cal = Calendar(self.edit_wind)
        self.edit_wind.cal.pack()
        Button(self.edit_wind, text="Obtener", command=lambda: self.get_date_from_calendar(obj)).pack()

    # User Input Validation
    def validationField(self):
        if len(self.name.get()) == 0:
            return 'Name is Required'
        elif len(self.code.get()) == 0:
            return 'Code is Required'
        elif len(self.date_entry.get()) == 0:
            return 'Date is Required'
        elif len(self.gender.get()) == 0:
            return 'Gender is Required'
        elif not self.code.get().isdigit():
            return 'Code is Required in int format'
        else:
            return True

    def add_product(self):
        validator = self.validationField()
        if validator == True:
            query = 'INSERT INTO estudiante VALUES(?, ?, ?, ?)'
            parameters = (self.code.get(), self.name.get(), self.date_entry.get(), self.gender.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Student {} added Successfully'.format(self.name.get())
            self.code.delete(0, END)
            self.name.delete(0, END)
            self.date_entry.delete(0, END)
            self.gender.delete(0, END)
        else:
            self.message['text'] = validator

    def delete_product(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text']
        except IndexError as e:
            self.message['text'] = 'Please select a Record'
            return
        self.message['text'] = ''
        code = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM estudiante WHERE codigo = ?'
        self.run_query(query, (code,))
        self.message['text'] = 'Record {} deleted Successfully'.format(code)

    def edit_product(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'Please, select Record'
            return
        code = self.tree.item(self.tree.selection())['text']
        old_name = self.tree.item(self.tree.selection())['values'][0]
        old_date = self.tree.item(self.tree.selection())['values'][1]
        old_gender = self.tree.item(self.tree.selection())['values'][2]
        self.edit_wind = Toplevel()
        self.edit_wind.title('Edit Product')
        # Old Name
        Label(self.edit_wind, text='Old code:').grid(row=0, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=code), state='readonly').grid(row=0, column=2)
        # New Name
        Label(self.edit_wind, text='New code:').grid(row=1, column=1)
        new_code = Entry(self.edit_wind)
        new_code.grid(row=1, column=2)

        # Old Name
        Label(self.edit_wind, text='Old name:').grid(row=2, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=old_name), state='readonly').grid(row=2, column=2)
        # New Name
        Label(self.edit_wind, text='New name:').grid(row=3, column=1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row=3, column=2)

        # Old Date
        Label(self.edit_wind, text='Old date:').grid(row=4, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=old_date), state='readonly').grid(row=4, column=2)
        # New Date
        Label(self.edit_wind, text='New date:').grid(row=5, column=1)
        new_date = Entry(self.edit_wind)
        new_date.bind("<Button-1>", lambda event: self.get_date(new_date))
        new_date.grid(row=5, column=2)

        # Old Gender
        Label(self.edit_wind, text='Old gender:').grid(row=6, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=old_gender), state='readonly').grid(row=6, column=2)
        # New Gender
        Label(self.edit_wind, text='New gender:').grid(row=7, column=1)
        new_gender = Entry(self.edit_wind)
        new_gender.grid(row=7, column=2)

        Button(self.edit_wind, text='Update',
               command=lambda: self.edit_records(new_code.get(), new_name.get(), new_date.get(), new_gender.get(),
                                                 code, old_name)).grid(row=8, column=2, sticky=W)
        self.edit_wind.mainloop()

    def edit_records(self, new_code, new_name, new_date, new_gender, old_code, old_name):
        query = 'UPDATE estudiante SET codigo = ?, nombre = ?, fecha = ?, genero = ? WHERE codigo = ? AND nombre = ?'
        parameters = (new_code, new_name, new_date, new_gender, old_code, old_name)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message['text'] = 'Record {} updated successfully'.format(old_name)


if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()
