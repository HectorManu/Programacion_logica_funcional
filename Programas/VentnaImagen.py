import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

# Crear la ventana
ventana = tk.Tk()


# Establecer el tamaño de la ventana
ventana.geometry("400x300")


# Establecer el título de la ventana
ventana.title("Mi ventana")


# Centrar la ventana en la pantalla
ancho_ventana = ventana.winfo_reqwidth()
alto_ventana = ventana.winfo_reqheight()
posicion_x = int(ventana.winfo_screenwidth() / 2 - ancho_ventana / 2)
posicion_y = int(ventana.winfo_screenheight() / 2 - alto_ventana / 2)
ventana.geometry("+{}+{}".format(posicion_x, posicion_y))


ventana.configure(bg="blue")


imagen = ImageTk.PhotoImage(Image.open('./heroina.jpeg').resize((100, 100)))


# Crear un widget Label para mostrar la imagen
label_imagen = Label(ventana, image=imagen)
label_imagen.pack()

# Permitir que la ventana sea redimensionable
ventana.resizable(True, True)


# Iniciar el bucle de eventos de la ventana
ventana.mainloop()
