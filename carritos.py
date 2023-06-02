from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random

#---------------------
# variables globales
#---------------------

BASE=460
ALTURA=450
desplazamiento_x = random.randint(1,5)
desplazamiento_x1 = random.randint(1,5)
desplazamiento_y = 0
intervalo = 5



# jugar
def jugar():
    global desplazamiento_x, desplazamiento_y
    x0, y0, = canvas.coords(carro1)
    x1, y2, =canvas.coords(carro2)
    if x0 < 0 or y0> BASE: 
        desplazamiento_x = -desplazamiento_x
    if y0 < 0 or x0 > ALTURA: 
        desplazamiento_y = -desplazamiento_y
    canvas.move(carro1, desplazamiento_x, desplazamiento_y)
    canvas.move(carro2, desplazamiento_x1, desplazamiento_y)
    ventana.after(intervalo, jugar)



#---------------------
# ventana principal
#---------------------

ventana = Tk()
ventana.title("Carritos")
ventana.resizable(False,False)
ventana.geometry("500x650")
ventana.config(bg="white")

#---------------------
# frame canvas
#---------------------

frame = Frame(ventana,width=480,height=480)
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
canvas.create_polygon(0,0,BASE/2-170,0,BASE/2-170,ALTURA,0,ALTURA,fill="ORANGE",width=2)
# cuadricula banda de salida
cuadro1 = canvas.create_rectangle(0,0,BASE/2-200,ALTURA/2-195,fill="black",width=2)
cuadro2 = canvas.create_rectangle(BASE/2-200,0,BASE/2-170,ALTURA/2-195,fill="white",width=2)
cuadro3 = canvas.create_rectangle(0,ALTURA/2-195,BASE/2-200,ALTURA/2-165,fill="white",width=2)
cuadro4 = canvas.create_rectangle(BASE/2-200,ALTURA/2-195,BASE/2-170,ALTURA/2-165,fill="black",width=2)
cuadro5 = canvas.create_rectangle(0,ALTURA/2-165,BASE/2-200,ALTURA/2-135,fill="black",width=2)
cuadro6 = canvas.create_rectangle(BASE/2-200,ALTURA/2-165,BASE/2-170,ALTURA/2-135,fill="white",width=2)
cuadro7 = canvas.create_rectangle(0,ALTURA/2-135,BASE/2-200,ALTURA/2-105,fill="white",width=2)
cuadro8 = canvas.create_rectangle(BASE/2-200,ALTURA/2-135,BASE/2-170,ALTURA/2-105,fill="black",width=2)
cuadro9 = canvas.create_rectangle(0,ALTURA/2-105,BASE/2-200,ALTURA/2-75,fill="black",width=2)
cuadro10 = canvas.create_rectangle(BASE/2-200,ALTURA/2-105,BASE/2-170,ALTURA/2-75,fill="white",width=2)
cuadro11 = canvas.create_rectangle(0,ALTURA/2-75,BASE/2-200,ALTURA/2-45,fill="white",width=2)
cuadro12 = canvas.create_rectangle(BASE/2-200,ALTURA/2-75,BASE/2-170,ALTURA/2-45,fill="black",width=2)
cuadro13 = canvas.create_rectangle(0,ALTURA/2-45,BASE/2-200,ALTURA/2-15,fill="black",width=2)
cuadro14 = canvas.create_rectangle(BASE/2-200,ALTURA/2-45,BASE/2-170,ALTURA/2-15,fill="white",width=2)
cuadro15 = canvas.create_rectangle(0,ALTURA/2-15,BASE/2-200,ALTURA/2+15,fill="white",width=2)
cuadro16 = canvas.create_rectangle(BASE/2-200,ALTURA/2-15,BASE/2-170,ALTURA/2+15,fill="black",width=2)
cuadro17 = canvas.create_rectangle(0,ALTURA/2+15,BASE/2-200,ALTURA/2+45,fill="black",width=2)
cuadro18 = canvas.create_rectangle(BASE/2-200,ALTURA/2+15,BASE/2-170,ALTURA/2+45,fill="white",width=2)
cuadro19 = canvas.create_rectangle(0,ALTURA/2+45,BASE/2-200,ALTURA/2+75,fill="white",width=2)
cuadro20 = canvas.create_rectangle(BASE/2-200,ALTURA/2+45,BASE/2-170,ALTURA/2+75,fill="black",width=2)
cuadro21 = canvas.create_rectangle(0,ALTURA/2+75,BASE/2-200,ALTURA/2+105,fill="black",width=2)
cuadro22 = canvas.create_rectangle(BASE/2-200,ALTURA/2+75,BASE/2-170,ALTURA/2+105,fill="white",width=2)
cuadro23 = canvas.create_rectangle(0,ALTURA/2+105,BASE/2-200,ALTURA/2+135,fill="white",width=2)
cuadro24 = canvas.create_rectangle(BASE/2-200,ALTURA/2+105,BASE/2-170,ALTURA/2+135,fill="black",width=2)
cuadro25 = canvas.create_rectangle(0,ALTURA/2+135,BASE/2-200,ALTURA/2+165,fill="black",width=2)
cuadro26 = canvas.create_rectangle(BASE/2-200,ALTURA/2+135,BASE/2-170,ALTURA/2+165,fill="white",width=2)
cuadro27 = canvas.create_rectangle(0,ALTURA/2+165,BASE/2-200,ALTURA/2+195,fill="white",width=2)
cuadro28 = canvas.create_rectangle(BASE/2-200,ALTURA/2+165,BASE/2-170,ALTURA/2+195,fill="black",width=2)
cuadro29 = canvas.create_rectangle(0,ALTURA/2+195,BASE/2-200,ALTURA,fill="black",width=2)
cuadro30 = canvas.create_rectangle(BASE/2-200,ALTURA/2+195,BASE/2-170,ALTURA,fill="white",width=2)


# banda de llegada
canvas.create_polygon(BASE/2+170,0,BASE,0,BASE,ALTURA,BASE/2+170,ALTURA,fill="orange",width=2)
# cuadros de llegada

cuadro31 = canvas.create_rectangle(BASE/2+170,0,BASE/2+200,ALTURA/2-195,fill="white",width=2)
cuadro32 = canvas.create_rectangle(BASE/2+200,0,BASE/2+230,ALTURA/2-195,fill="black",width=2)
cuadro33 = canvas.create_rectangle(BASE/2+170,ALTURA/2-195,BASE/2+200,ALTURA/2-165,fill="black",width=2)
cuadro34 = canvas.create_rectangle(BASE/2+200,ALTURA/2-195,BASE/2+230,ALTURA/2-165,fill="white",width=2)
cuadro35 = canvas.create_rectangle(BASE/2+170,ALTURA/2-165,BASE/2+200,ALTURA/2-135,fill="white",width=2)
cuadro36 = canvas.create_rectangle(BASE/2+200,ALTURA/2-165,BASE/2+230,ALTURA/2-135,fill="black",width=2)
cuadro37 = canvas.create_rectangle(BASE/2+170,ALTURA/2-135,BASE/2+200,ALTURA/2-105,fill="black",width=2)
cuadro38 = canvas.create_rectangle(BASE/2+200,ALTURA/2-135,BASE/2+230,ALTURA/2-105,fill="white",width=2)
cuadro39 = canvas.create_rectangle(BASE/2+170,ALTURA/2-105,BASE/2+200,ALTURA/2-75,fill="white",width=2)
cuadro40 = canvas.create_rectangle(BASE/2+200,ALTURA/2-105,BASE/2+230,ALTURA/2-75,fill="black",width=2)
cuadro41 = canvas.create_rectangle(BASE/2+170,ALTURA/2-75,BASE/2+200,ALTURA/2-45,fill="black",width=2)
cuadro42 = canvas.create_rectangle(BASE/2+200,ALTURA/2-75,BASE/2+230,ALTURA/2-45,fill="white",width=2)
cuadro43 = canvas.create_rectangle(BASE/2+170,ALTURA/2-45,BASE/2+200,ALTURA/2-15,fill="white",width=2)
cuadro44 = canvas.create_rectangle(BASE/2+200,ALTURA/2-45,BASE/2+230,ALTURA/2-15,fill="black",width=2)
cuadro45 = canvas.create_rectangle(BASE/2+170,ALTURA/2-15,BASE/2+200,ALTURA/2+15,fill="black",width=2)
cuadro46 = canvas.create_rectangle(BASE/2+200,ALTURA/2-15,BASE/2+230,ALTURA/2+15,fill="white",width=2)
cuadro47 = canvas.create_rectangle(BASE/2+170,ALTURA/2+15,BASE/2+200,ALTURA/2+45,fill="white",width=2)
cuadro48 = canvas.create_rectangle(BASE/2+200,ALTURA/2+15,BASE/2+230,ALTURA/2+45,fill="black",width=2)
cuadro49 = canvas.create_rectangle(BASE/2+170,ALTURA/2+45,BASE/2+200,ALTURA/2+75,fill="black",width=2)
cuadro50 = canvas.create_rectangle(BASE/2+200,ALTURA/2+45,BASE/2+230,ALTURA/2+75,fill="white",width=2)
cuadro51 = canvas.create_rectangle(BASE/2+170,ALTURA/2+75,BASE/2+200,ALTURA/2+105,fill="white",width=2)
cuadro52 = canvas.create_rectangle(BASE/2+200,ALTURA/2+75,BASE/2+230,ALTURA/2+105,fill="black",width=2)
cuadro53 = canvas.create_rectangle(BASE/2+170,ALTURA/2+105,BASE/2+200,ALTURA/2+135,fill="black",width=2)
cuadro54 = canvas.create_rectangle(BASE/2+200,ALTURA/2+105,BASE/2+230,ALTURA/2+135,fill="white",width=2)
cuadro55 = canvas.create_rectangle(BASE/2+170,ALTURA/2+135,BASE/2+200,ALTURA/2+165,fill="white",width=2)
cuadro56 = canvas.create_rectangle(BASE/2+200,ALTURA/2+135,BASE/2+230,ALTURA/2+165,fill="black",width=2)
cuadro57 = canvas.create_rectangle(BASE/2+170,ALTURA/2+165,BASE/2+200,ALTURA/2+195,fill="black",width=2)
cuadro58 = canvas.create_rectangle(BASE/2+200,ALTURA/2+165,BASE/2+230,ALTURA/2+195,fill="white",width=2)
cuadro59 = canvas.create_rectangle(BASE/2+170,ALTURA/2+195,BASE/2+200,ALTURA,fill="white",width=2)
cuadro60 = canvas.create_rectangle(BASE/2+200,ALTURA/2+195,BASE/2+230,ALTURA,fill="black",width=2)

#via 

canvas.create_polygon(BASE/2-170,ALTURA/2-200,BASE/2+170,ALTURA/2-200,BASE/2+170,ALTURA/2+200,BASE/2-170,ALTURA/2+200,fill="BLACK",width=2)

# división vías

canvas.create_polygon(BASE/2-160,ALTURA/2-2,BASE/2+160,ALTURA/2-2,BASE/2+160,ALTURA/2+2,BASE/2-160,ALTURA/2+2,outline="yellow",fill="yellow",width=2)

#aceras

acera1=canvas.create_polygon(BASE/2-170,ALTURA/2-230,BASE/2+170,ALTURA/2-230,BASE/2+170,ALTURA/2-200,BASE/2-170,ALTURA/2-200,fill="grey10",width=2)

acera2=canvas.create_polygon(BASE/2-170,ALTURA/2+200,BASE/2+170,ALTURA/2+200,BASE/2+170,ALTURA/2+230,BASE/2-170,ALTURA/2+230,fill="grey10",width=2)

# contorno aceras

ca1=canvas.create_polygon(BASE/2-170,ALTURA/2-230,BASE/2+170,ALTURA/2-230,BASE/2+170,ALTURA/2-220,BASE/2-170,ALTURA/2-220,fill="grey",width=2)

ca1=canvas.create_polygon(BASE/2-170,ALTURA/2-220,BASE/2-165,ALTURA/2-220,BASE/2-165,ALTURA/2-200,BASE/2-170,ALTURA/2-200,fill="grey",width=2)

ca1=canvas.create_polygon(BASE/2+170,ALTURA/2-230,BASE/2+165,ALTURA/2-230,BASE/2+165,ALTURA/2-200,BASE/2+170,ALTURA/2-200,fill="grey",width=2)

ca1=canvas.create_polygon(BASE/2-170,ALTURA/2-205,BASE/2+170,ALTURA/2-205,BASE/2+170,ALTURA/2-200,BASE/2-170,ALTURA/2-200,fill="grey",width=2)

ca2=canvas.create_polygon(BASE/2-170,ALTURA/2+230,BASE/2+170,ALTURA/2+230,BASE/2+170,ALTURA/2+220,BASE/2-170,ALTURA/2+220,fill="grey",width=2)

ca2=canvas.create_polygon(BASE/2-170,ALTURA/2+220,BASE/2-165,ALTURA/2+220,BASE/2-165,ALTURA/2+200,BASE/2-170,ALTURA/2+200,fill="grey",width=2)

ca2=canvas.create_polygon(BASE/2+170,ALTURA/2+230,BASE/2+165,ALTURA/2+230,BASE/2+165,ALTURA/2+200,BASE/2+170,ALTURA/2+200,fill="grey",width=2)

ca2=canvas.create_polygon(BASE/2-170,ALTURA/2+205,BASE/2+170,ALTURA/2+205,BASE/2+170,ALTURA/2+200,BASE/2-170,ALTURA/2+200,fill="grey",width=2)


# texto salida

s=canvas.create_text(BASE/2-200,ALTURA/2-120,text="S",font=("Arial",30),fill="grey",)
a=canvas.create_text(BASE/2-200,ALTURA/2-80,text="A",font=("Arial",30),fill="grey",)
l=canvas.create_text(BASE/2-200,ALTURA/2-30,text="L",font=("Arial",30),fill="grey",)
i=canvas.create_text(BASE/2-200,ALTURA/2+30,text="I",font=("Arial",30),fill="grey",)
d=canvas.create_text(BASE/2-200,ALTURA/2+80,text="D",font=("Arial",30),fill="grey",)
a=canvas.create_text(BASE/2-200,ALTURA/2+120,text="A",font=("Arial",30),fill="grey",)

s1=canvas.create_text(BASE/2-196,ALTURA/2-120,text="S",font=("Arial",30),fill="white",)
a1=canvas.create_text(BASE/2-196,ALTURA/2-80,text="A",font=("Arial",30),fill="white",)
l1=canvas.create_text(BASE/2-196,ALTURA/2-30,text="L",font=("Arial",30),fill="white",)
i1=canvas.create_text(BASE/2-196,ALTURA/2+30,text="I",font=("Arial",30),fill="white",)
d1=canvas.create_text(BASE/2-196,ALTURA/2+80,text="D",font=("Arial",30),fill="white",)
a1=canvas.create_text(BASE/2-196,ALTURA/2+120,text="A",font=("Arial",30),fill="white",)

# texto meta

m=canvas.create_text(BASE/2+200,ALTURA/2-90,text="M",font=("Arial",30),fill="grey",)
e=canvas.create_text(BASE/2+200,ALTURA/2-30,text="E",font=("Arial",30),fill="grey",)
t=canvas.create_text(BASE/2+200,ALTURA/2+30,text="T",font=("Arial",30),fill="grey",)
a=canvas.create_text(BASE/2+200,ALTURA/2+90,text="A",font=("Arial",30),fill="grey",)

m1=canvas.create_text(BASE/2+203,ALTURA/2-90,text="M",font=("Arial",30),fill="white",)
e1=canvas.create_text(BASE/2+203,ALTURA/2-30,text="E",font=("Arial",30),fill="white",)
t1=canvas.create_text(BASE/2+203,ALTURA/2+30,text="T",font=("Arial",30),fill="white",)
a1=canvas.create_text(BASE/2+203,ALTURA/2+90,text="A",font=("Arial",30),fill="white",)

#crear objetos para las imagenes
carro1 = PhotoImage(file="img/carro1.png")
carro2 = PhotoImage(file="img/carro2.png")

#insertar imagenes en el canvas
canvas.create_image(0,0,anchor=NW,image=carro1)
canvas.create_image(0,ALTURA/2+130,anchor=NW,image=carro2)

#---------------------
# frame controles
#---------------------

frame_controles = Frame(ventana,width=480,height=130)
frame_controles.config(bg="navy")
frame_controles.place(x=10,y=510)

#boton jugar
boton_jugar = Button(frame_controles,text="Jugar",command=jugar)
boton_jugar.config(bg="green",width=5)
boton_jugar.place(x=220,y=10)

#boton salir
boton_salir = Button(frame_controles,text="Salir",command=ventana.destroy)
boton_salir.config(bg="red",width=5)
boton_salir.place(x=220,y=50)








ventana.mainloop()