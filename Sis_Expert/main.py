import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# Crear una variable para almacenar la opción seleccionada
opcion_seleccionada = tk.StringVar()

# Crear una lista de opciones
opciones = ['Opción 1', 'Opción 2', 'Opción 3']

# Crear una función para imprimir la opción seleccionada
def imprimir_opcion_seleccionada():
    print(opcion_seleccionada.get())

# Crear una etiqueta para las opciones
etiqueta_opciones = tk.Label(ventana, text="Seleccione una opción:")

# Crear un menú desplegable con las opciones
menu_opciones = tk.OptionMenu(ventana, opcion_seleccionada, *opciones)

# Crear un botón para imprimir la opción seleccionada
boton_imprimir = tk.Button(ventana, text="Imprimir opción seleccionada", command=imprimir_opcion_seleccionada)

# Añadir los widgets a la ventana
etiqueta_opciones.pack()
menu_opciones.pack()
boton_imprimir.pack()

# Mostrar la ventana
ventana.mainloop()
