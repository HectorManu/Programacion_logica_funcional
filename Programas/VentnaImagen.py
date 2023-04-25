import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

# Crear la ventana
ventana = tk.Tk()

# Establecer el título de la ventana
ventana.title("Equipo#1 Avila Castellanos Macias Ruiz")

# Centrar la ventana en la pantalla
ancho_ventana = ventana.winfo_reqwidth() #calcula el ancho de la ventana
alto_ventana = ventana.winfo_reqheight() #calcula la altura de la ventana
posicion_x = int(ventana.winfo_screenwidth() / 2 - ancho_ventana / 2) #resta entre el ancho de pantalla con el de la ventana
posicion_y = int(ventana.winfo_screenheight() / 2 - alto_ventana / 2) #resta entre la altura de pantalla con la de la ventana

ventana.geometry("+{}+{}".format(posicion_x, posicion_y)) #Centra la ventana en la pantalla


#Se establece el azul cielo de fondo
ventana.configure(bg="#12a5ca")


# Cargar la imagen
image = Image.open("./2023-02-13_01.png")
image = image.resize((120,100),Image.ANTIALIAS)

# Crear un widget Label para mostrar la imagen
img = ImageTk.PhotoImage(image)


# Colocar el widget Label en la ventana
lbl = Label(ventana, image=img)


#colocar el label en la parte inferior derecha
lbl.place(relx=1.0, rely=1.0, anchor='se')


# Permitir que la ventana sea redimensionable
ventana.resizable(True, True)


# Iniciar el bucle de eventos de la ventana
ventana.mainloop()