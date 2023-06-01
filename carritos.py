from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#---------------------
# variables globales
#---------------------

BASE=460
ALTURA=420


#---------------------
# ventana principal
#---------------------

ventana = Tk()
ventana.title("Carritos")
ventana.resizable(False,False)
ventana.geometry("500x600")
ventana.config(bg="white")

#---------------------
# frame canvas
#---------------------

frame = Frame(ventana,width=480,height=440)
frame.config(bg="navy")
frame.place(x=10,y=10)

#---------------------
# canvas
#---------------------

canvas = Canvas(frame,width=BASE,height=ALTURA)
canvas.config(bg="GRAY")
canvas.place(x=10,y=10)

# lineas divisorias
canvas.create_line(BASE/2,0,BASE/2,ALTURA,fill="RED",width=2)
canvas.create_line(0,ALTURA/2,BASE,ALTURA/2,fill="RED",width=2)

# banda de salida
canvas.create_polygon(0,0,BASE/2-170,0,BASE/2-170,ALTURA,0,ALTURA,fill="yellow",width=2)
# banda de llegada
canvas.create_polygon(BASE/2+170,0,BASE,0,BASE,ALTURA,BASE/2+170,ALTURA,fill="yellow",width=2)

#via 1

canvas.create_polygon(BASE/2-170,0,BASE/2+170,0,BASE/2+170,ALTURA/2-50,BASE/2-170,ALTURA/2-50,fill="BLACK",width=2)

#rayas via 1

canvas.create_line(BASE/2-170,ALTURA/2-135,BASE/2+170,ALTURA/2-135,fill="yellow",width=2)

#via 2

canvas.create_polygon(BASE/2-170,ALTURA/2+50,BASE/2+170,ALTURA/2+50,BASE/2+170,ALTURA,BASE/2-170,ALTURA,fill="BLACK",width=2)

#---------------------
# frame controles
#---------------------

frame_controles = Frame(ventana,width=480,height=130)
frame_controles.config(bg="navy")
frame_controles.place(x=10,y=460)









ventana.mainloop()