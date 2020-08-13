import msvcrt
import math
import tkinter as tk
from tkinter import *
from tkinter import messagebox

#############################

#RAIZ
raiz=Tk()
raiz.title("Programa de Porcentaje")
raiz.resizable(0,0)
raiz.config(bg="Green")

def infocreador():
    messagebox.showinfo("PORCENTAJE", "Creado por Claudio Martinez con Ayuda de Karim Brizuela")

def salirapp():
    valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")
    if valor=="yes":
        raiz.destroy()



barraMenu=Menu(raiz)
raiz.config(menu=barraMenu)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Salir", command=salirapp)
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Info", command=infocreador)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)


#FRAME
frame=Frame(raiz)
frame.pack()
frame.config(width=200, height=400)
frame.config(bg="Pink")
frame.config(bd=25)
frame.config(relief="groove")




#FUNCIONES
var=StringVar()
numerototal=StringVar()
numerodescuento=StringVar()

res= Label(frame, bg="pink", fg="black",font=("Arial",18), textvariable=var)
res.place(x=35, y=315)


def cuentaboton():
    mult= float(numerototal.get()) * float(numerodescuento.get())
    resultado= mult / 100
    cuentaboton2= float(numerototal.get()) - resultado
    return var.set("{:.2f}".format(cuentaboton2))




#LABEL
porcentaje= Label(frame, text="PORCENTAJE", bg="Black",fg="Pink",font=("Arial",14))
porcentaje.place(x=9, y= 5)

cifratotal= Label(frame, text="Ingrese el Monto Total:", bg="Pink",fg="Black",font=("Arial",10))
cifratotal.place(x=7, y= 40)

descuento= Label(frame, text="Ingrese el Porcentaje\n Descontar:", bg="Pink",fg="Black",font=("Arial",10))
descuento.place(x=10, y= 100)

desctotal= Label(frame, text="Valor con\nDescuento Incluido", bg="Black",fg="Pink",font=("Arial",10))
desctotal.place(x=18, y= 270)

#CUADRO DE TEXTO
cuadrotexto1=Entry(frame, textvariable=numerototal)
cuadrotexto1.place(x=10, y= 65)

cuadrotexto1=Entry(frame, textvariable=numerodescuento)
cuadrotexto1.place(x=10, y= 140)




#BOTON DE ENVIO
botonenvio= Button(frame, text="Enviar\nCuenta", command=cuentaboton)
botonenvio.place(x=53, y=220)



#FINAL
raiz.mainloop()
msvcrt.getch()
