import tkinter as tk
from tkinter import HORIZONTAL, VERTICAL, Button, Entry, Frame, IntVar, Label, Scrollbar, StringVar, Tk, Toplevel, ttk, font
from tkinter import messagebox
from tkinter import scrolledtext as st
from unicodedata import numeric
from unittest.util import _MAX_LENGTH
from webbrowser import BackgroundBrowser

from liberliberatumbd import RegistroDatos




class Registro(Frame):
    def __init__(self, master, *args,**kwargs):
        super().__init__(master,*args,**kwargs)

        self.frame1= Frame(master)
        self.frame1.grid(columnspan=2,column=0,row=0)

        self.frame2= Frame(master,bg='#b77037')
        self.frame2.grid(column=0,row=1)

        self.frame3= Frame(master)
        self.frame3.grid(rowspan=2,column=1,row=1)

        self.frame4= Frame(master,bg='#b77037')
        self.frame4.grid(column=2,row=2)

        self.frame5= Frame(master,bg='#b77037')
        self.frame5.grid(column=2,row=1)

        self.isbn =StringVar()
        self.autor=StringVar()
        self.titulo=StringVar()
        self.edicion=StringVar()
        self.buscarAutor=StringVar()
        self.buscar=StringVar()
        
        self.isbn2 =StringVar()
        self.autor2=StringVar()
        self.titulo2=StringVar()
        self.edicion2=StringVar()

        self.base_datos=RegistroDatos()
        self.create_widgets()

    def create_widgets(self):
        
        Label(self.frame2, text='Agregar nuevos datos',bg='#9e561c',fg='white',font=('URW Gothic',12,'bold')).grid(columnspan=2,column=0,row=0,pady=5)
        Label(self.frame2, text='ISBN',bg='#b77037',fg='white',font=('URW Gothic',13,'bold')).grid(column=0,row=1,pady=15)
        Label(self.frame2, text='Autor',bg='#b77037',fg='white',font=('URW Gothic',13,'bold')).grid(column=0,row=2,pady=15)
        Label(self.frame2, text='Título',bg='#b77037',fg='white',font=('URW Gothic',13,'bold')).grid(column=0,row=3,pady=15)
        Label(self.frame2, text='Año de edición',bg='#b77037',fg='white',font=('URW Gothic',13,'bold')).grid(column=0,row=4,pady=15)
        Button(self.frame2,command=self.agregar_datos,text= '+ Registrar',font=('URW Gothic',10,'bold'),bg='#9e561c').grid(column=0,row=6,pady=15,padx=4)
        Button(self.frame2,command=self.limpiar_campos_tabla,text= 'Limpiar',font=('URW Gothic',10,'bold'),bg='#9e561c').grid(column=1,row=6,pady=15,padx=4)

        Entry(self.frame2,textvariable=self.isbn,font=('URW Gothic',12)).grid(column=1,row=1,padx=5)
        Entry(self.frame2,textvariable=self.autor,font=('URW Gothic',12)).grid(column=1,row=2)
        Entry(self.frame2,textvariable=self.titulo,font=('URW Gothic',12)).grid(column=1,row=3)
        Entry(self.frame2,textvariable=self.edicion,font=('URW Gothic',12)).grid(column=1,row=4)
        
        Label(self.frame5, text='Modificar datos',bg='#9e561c',fg='white',font=('URW Gothic',12,'bold')).grid(columnspan=2,column=0,row=0,pady=5)
        Label(self.frame5, text='Autor',bg='#b77037',fg='white',font=('URW Gothic',13,'bold')).grid(column=0,row=2,pady=15)
        Label(self.frame5, text='Título',bg='#b77037',fg='white',font=('URW Gothic',13,'bold')).grid(column=0,row=3,pady=15)
        Label(self.frame5, text='Año de edición',bg='#b77037',fg='white',font=('URW Gothic',13,'bold')).grid(column=0,row=4,pady=15)
        Button(self.frame5,command=self.modificar_fila,text= 'Actualizar',font=('URW Gothic',10,'bold'),bg='#9e561c').grid(column=1,row=5,pady=15,padx=4)
        Button(self.frame5,command=self.eliminar_fila,text= 'Eliminar',font=('URW Gothic',10,'bold'),bg='#9e561c').grid(column=1,row=6,pady=10,padx=4)
        Entry(self.frame5,textvariable=self.autor2,font=('URW Gothic',12)).grid(column=1,row=2)
        Entry(self.frame5,textvariable=self.titulo2,font=('URW Gothic',12)).grid(column=1,row=3)
        Entry(self.frame5,textvariable=self.edicion2,font=('URW Gothic',12)).grid(column=1,row=4)

        Entry(self.frame4,textvariable=self.buscar,font=('URW Gothic',12),width=10).grid(column=1,row=3,pady=1,padx=8)
        Button(self.frame4,command=self.buscar_isbn,text= 'Buscar por ISBN',font=('URW Gothic',10,'bold'),bg='#9e561c').grid(column=3,row=3,pady=10,padx=4)
        Button(self.frame4,command=self.mostrar_todo,text= 'Mostrar todo',font=('URW Gothic',10,'bold'),bg='#9e561c').grid(column=3,row=5,pady=10,padx=4)
        
        
        
        self.tabla = ttk.Treeview(self.frame3,height=21)
        self.tabla.grid(column=0,row=0)

        ladox= Scrollbar(self.frame3, orient= HORIZONTAL,command=self.tabla.xview)
        ladox.grid(column=0,row=1,sticky='ew')
        ladoy=Scrollbar(self.frame3, orient= VERTICAL,command=self.tabla.yview)
        ladoy.grid(column=1,row=0,sticky='ns')

        self.tabla.configure(xscrollcommand=ladox.set,yscrollcommand=ladoy.set)
        self.tabla['columns'] = ('Autor','Título','Año de edición')

    
        self.tabla.column('#0',minwidth=100,width=120,anchor='center')
        self.tabla.column('Autor',minwidth=100,width=130,anchor='center')
        self.tabla.column('Título',minwidth=100,width=130,anchor='center')
        self.tabla.column('Año de edición',minwidth=120,width=130,anchor='center')

        self.tabla.heading('#0',text='ISBN',anchor='center')
        self.tabla.heading('Autor',text='Autor',anchor='center')
        self.tabla.heading('Título',text='Título',anchor='center')
        self.tabla.heading('Año de edición',text='Año de edición',anchor='center')


        estilo= ttk.Style(self.frame3)
        estilo.theme_use('alt')
        estilo.configure(".",font=('Helvetica',12,'bold'),foreground='black')
        estilo.configure("Treeview",font=('Helvetica',12,'bold'),foreground='black',background='white')
        estilo.map('Treeview',background=[('selected','#edd484')],foreground=[('selected','black')])

        self.tabla.bind("<<TreeviewSelect>>",self.obtener_fila)
 
    def agregar_datos(self):
        self.tabla.get_children()
        isbn=self.isbn.get()
        autor=self.autor.get()
        titulo=self.titulo.get()
        edicion=self.edicion.get()
        datos = (autor, titulo, edicion)
        if isbn and autor and titulo and edicion !='':
            isbn_numerico(self,isbn)
            edicion_numerico(self,edicion)
            validar_autor(self,autor)
            validar_titulo(self,titulo)
            self.tabla.insert('',0,text=isbn, values=datos)
            self.base_datos.insertar(isbn,autor,titulo,edicion)
            limpiar_campos(self)
            self.mostrar_todo()
        else:
            messagebox.showerror(title="Opcion inválida",message="Debe completar todos los campos porque son obligatorios.")

  

    def limpiar_campos_tabla(self):
        self.tabla.delete(*self.tabla.get_children())
        self.isbn.set('')
        self.autor.set('')
        self.titulo.set('')
        self.edicion.set('')

    def buscar_isbn(self):
        isbn=self.buscar.get()
        isbnBuscado=self.base_datos.buscarLibro(isbn)
        self.tabla.delete(*self.tabla.get_children())
        i=-1
        for dato in isbnBuscado:
            i=i+1 
            self.tabla.insert('',i,text=isbnBuscado[i][0:1],values=isbnBuscado[i][1:5])

    
    def mostrar_todo(self):
        self.tabla.delete(*self.tabla.get_children())
        registro=self.base_datos.mostrar()
        i= -1
        for dato in registro:
            i=i+1
            self.tabla.insert('',i,text=registro[i][0:1], values=registro[i][1:5])

    def eliminar_fila(self):
        fila=self.tabla.selection()
        if len(fila)!=0:
            #isbn=self.isbn.get()
            self.tabla.delete(fila)
            Libro =self.edicionBorrar
            self.base_datos.eliminarLibro(Libro)
    
    def modificar_fila(self):
        isbn=self.isbn2.get()
        autor=self.autor2.get()
        titulo=self.titulo2.get()
        edicion=self.edicion2.get()
        datos = (autor, titulo, edicion)
        print(autor, titulo, edicion)
        if isbn and autor and titulo and edicion != "":
            edicion_numerico(self,edicion)
            validar_autor(self,autor)
            validar_titulo(self,titulo)
            self.base_datos.modificarLibro(isbn,autor,titulo,edicion)
            limpiar_campos(self)
            self.mostrar_todo()

    def obtener_fila(self,event):
        current_item= self.tabla.focus()
        if not current_item:
            return
        data = self.tabla.item(current_item)
        self.edicionBorrar = data['values'][2]
        self.isbn2.set(data['text'])
        self.autor2.set(data['values'][0])
        self.titulo2.set(data['values'][1])
        self.edicion2.set(data['values'][2])
        

def limpiar_campos(self):
        self.isbn.set('')
        self.autor.set('')
        self.titulo.set('')
        self.edicion.set('')

def isbn_numerico(self,isbn):
        while len (isbn) not in range (10,13) or any(num.isalpha() for num in isbn):
            messagebox.showerror(title="Opcion inválida",message="El campo ISBN acepta sólo números. Mínimo de caracteres: 10 y máximo de caracteres: 13")
            self.isbn.set('')
            isbn_numerico(isbn)
        else:
            isbnInt= int(isbn)
            return True
            
def edicion_numerico(self,edicion):
        while len (edicion) != 4 or any(num.isalpha() for num in edicion):
            messagebox.showerror(title="Opcion inválida",message="El campo año de edición acepta sólo 4 números.")
            self.edicion.set('')
            edicion_numerico(edicion)
        else:
            edicionInt = int(edicion)
            return True
  
def validar_autor(self,a):
    while (a.isspace() or len(a) < 2):
        messagebox.showerror(title="Opcion inválida",message="El nombre del autor debe contener al menos 2 caracteres.")
        self.autor.set('')
        validar_autor(a)
    else:
        return True

def validar_titulo(self,a):
    while (a.isspace() or len(a) < 2):
        messagebox.showerror(title="Opcion inválida",message="El título debe tener al menos 2 caracteres.")
        self.titulo.set('')
        validar_titulo(a)
    else:
        return True

def main():
    ventana= Tk()
    ventana.title("Liber Liberatum")
    ventana.config(bg='#b77037')
    ventana.geometry('1250x470')
    ventana.resizable(0,0)
    app= Registro(ventana)
    app.mainloop()

if __name__ =="__main__":
    main()