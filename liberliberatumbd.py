from operator import contains
from queue import Empty
import mysql.connector
from tkinter import messagebox as mb

class RegistroDatos:
    def __init__ (self):
        self.conexion=mysql.connector.connect(host="localhost",user="root",
                                    passwd="",database="liberliberatum")

    def insertar(self,isbn,autor,titulo,edicion):
        con = self.conexion.cursor()
        sql='''INSERT INTO libro (ISBN,Autor,Titulo,Edicion)
        VALUES('{}','{}','{}','{}')'''.format(isbn,autor,titulo,edicion)
        con.execute(sql)
        self.conexion.commit()
        con.close()
        mb.showinfo(title="Opcion válida",message="Datos almacenados con éxito")
        

    def mostrar(self):
        con = self.conexion.cursor()
        sql="SELECT * FROM libro"
        con.execute(sql)
        registro = con.fetchall()
        return registro

    def buscarLibro(self,ISBN_libro):
        con = self.conexion.cursor()
        sql="SELECT * FROM libro where ISBN = {}".format(ISBN_libro)
        con.execute(sql)
        registroX = con.fetchall()
        con.close()
        if len(registroX)==0:            
            mb.showerror(title="Opcion inválida",message="El ISBN ingresado no existe en la base de datos") 
            return False
        return registroX


    def modificarLibro(self,isbn,autor,titulo,edicion):
        con = self.conexion.cursor()
        sql = f"UPDATE libro SET autor='{autor}', titulo='{titulo}', edicion={edicion} WHERE isbn='{isbn}' "
        con.execute(sql)
        self.conexion.commit()
        con.close()

    def eliminarLibro(self,edicion):
        con = self.conexion.cursor()
        sql='''DELETE FROM libro where edicion = {}'''.format(edicion)
        con.execute(sql)
        self.conexion.commit()
        con.close()
        mb.showinfo(title="Eliminado",message="Se ha eliminado el libro seleccionado.")

    def traerAutor(self,autor):
        con = self.conexion.cursor()
        sql="SELECT * FROM libro where autor = {}".format(autor)
        con.execute(sql)
        registroX = con.fetchall()
        con.close()
        return registroX
        
        