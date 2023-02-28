import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

# Creamos la ventana principal
ventana = tk.Tk()

# cargar la imagen
imagen = Image.open("/img")

# convertir la imagen en un objeto de imagen
imagen_tk = ImageTk.PhotoImage(imagen)

# Configuramos el tamaño y la posición de la ventana principal
ventana.geometry('300x200+400+300')
ventana.title('Equipo#1 Avila Castellanos Macias Ruiz')
ventana.configure(bg='blue')

# crear un widget de imagen y agregarlo a la ventana
widget_imagen = Label(ventana, image=imagen_tk)
widget_imagen.pack()


# Creamos un marco que ocupará toda la ventana principal
marco = tk.Frame(ventana,bg='blue')
marco.place(relx=0.5, rely=0.5, anchor='center')



# Ejecutamos el bucle principal de la ventana
ventana.mainloop()
