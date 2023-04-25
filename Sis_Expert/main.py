import tkinter as tk
import pickle
# from PIL import Image, ImageTk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def on_question1_respuesta_changed(self, *args):
        print(f"Seleccionaste: {self.question1_respuesta.get()}")
        if self.question1_respuesta.get() == "Sí":
            print("es si")
        else:
            print("es no")

        return self.question1_respuesta.get()

        # self.descripcion_label = tk.Label(self, text="Descripción:")
        # self.descripcion_label.pack(side="top")
        # self.descripcion_text = tk.Text(self, height=5, width=50)
        # self.descripcion_text.pack()

        # self.ruta_label = tk.Label(self, text="Ruta de imagen:")
        # self.ruta_label.pack(side="top")
        # self.ruta_text = tk.Entry(self)
        # self.ruta_text.pack()

        # self.guardar_boton = tk.Button(self, text="Guardar", command=self.guardar_info)
        # self.guardar_boton.pack(side="bottom")

    # def guardar_info(self):
    #     descripcion = self.descripcion_text.get("1.0", tk.END)
    #     ruta = self.ruta_text.get()
    #     print(f"Descripción: {descripcion}")
    #     print(f"Ruta de imagen: {ruta}")

    #     archivo = "datos.pickle"
    #     try:
    #         with open(archivo, "rb") as f:
    #             datos = pickle.load(f)
    #     except FileNotFoundError:
    #         datos = {}

    #     # Agregamos la información al diccionario
    #     datos["descripcion"] = descripcion
    #     datos["ruta_imagen"] = ruta

    #     # Guardamos el diccionario en el archivo
    #     with open(archivo, "wb") as f:
    #         pickle.dump(datos, f)

    #     # Mostramos la información guardada
    #     print(datos)

    #     # Eliminamos los widgets de la ventana
    #     self.descripcion_label.destroy()
    #     self.descripcion_text.destroy()
    #     self.ruta_label.destroy()
    #     self.ruta_text.destroy()
    #     self.guardar_boton.destroy()


    def validacion(self):
        print(self.on_question1_respuesta_changed)

    def on_question2_respuesta_changed(self, *args):
        # print(f"Seleccionaste: {self.question2_respuesta.get()}")

        if self.question2_respuesta.get() == "Menor de edad":
            print("menor")
        elif self.question2_respuesta.get() == "Joven o adolescente":
            print("joven")
        elif self.question2_respuesta.get() == "Adulto responsable":
            print("adulto")
            


        # COMO IMPRIMIR IMAGEN Y TEXTO PARA EL RESULTADO FINAL 

        # imagen = Image.open("ruta/a/la/imagen.png")
        # imagen = imagen.resize((300, 300))
        # imagen_tk = ImageTk.PhotoImage(imagen)

        # imagen_label = tk.Label(self, image=imagen_tk)
        # imagen_label.pack()

        # texto_label = tk.Label(self, text="Texto encima de la imagen")
        # texto_label.place(relx=0.5, rely=0.1, anchor="center")

    def on_question3_respuesta_changed(self, *args):
        # print(f"Seleccionaste: {self.question3_respuesta.get()}")
        if self.question3_respuesta.get() == "Falla":
            print("falla")
        elif self.question3_respuesta.get() == "Estable":
            print("estable")
        elif self.question3_respuesta.get() == "Excelente":
            print("Exclente")

    def on_question4_respuesta_changed(self, *args):
        # print(f"Seleccionaste: {self.question4_respuesta.get()}")
        if self.question4_respuesta.get() == "Más de 4.5":
            print("mas de 4.5")
        elif self.question4_respuesta.get() == "Entre 4 y 4.5":
            print("entre")
        elif self.question4_respuesta.get() == "Menos de 4":
            print("menos")

    def on_question5_respuesta_changed(self, *args):
        # print(f"Seleccionaste: {self.question5_respuesta.get()}")
        if self.question5_respuesta.get() == "Juegos":
            print("juegos")
        elif self.question5_respuesta.get() == "Educación":
            print("educacion")

    def create_widgets(self):

        # Pregunta 1

        self.question1_respuesta = tk.StringVar(value="Ninguno")
        self.question1_respuesta.trace("w", self.on_question1_respuesta_changed)

        self.question1_label = tk.Label(self, text="¿Prefieres una aplicación gratuita o estás dispuesto a pagar por características adicionales?")
        self.question1_label.pack(side="top")

        self.question1_respuesta_azul = tk.Radiobutton(self, text="Sí", variable=self.question1_respuesta, value="Sí")
        self.question1_respuesta_azul.pack(anchor="center")

        self.question1_respuesta_rojo = tk.Radiobutton(self, text="No", variable=self.question1_respuesta, value="No")
        self.question1_respuesta_rojo.pack(anchor="center")

        self.question1_respuesta_label = tk.Label(self, textvariable=self.question1_respuesta)
        # self.question1_respuesta_label.pack(side="bottom")
        self.validacion()

        # Pregunta 2
        self.question2_respuesta = tk.StringVar(value="Ninguno")
        self.question2_respuesta.trace("w", self.on_question2_respuesta_changed)

        self.question2_label = tk.Label(self, text="¿Qué edad tiene el usuario?")
        self.question2_label.pack(side="top")

        self.question2_respuesta_azul = tk.Radiobutton(self, text="Menor de edad", variable=self.question2_respuesta, value="Menor de edad")
        self.question2_respuesta_azul.pack(anchor="center")

        self.question2_respuesta_rojo = tk.Radiobutton(self, text="Juven o adolescente", variable=self.question2_respuesta, value="Joven o adolescente")
        self.question2_respuesta_rojo.pack(anchor="center")

        self.question2_respuesta_rojo = tk.Radiobutton(self, text="Adulto responsable", variable=self.question2_respuesta, value="Adulto responsable")
        self.question2_respuesta_rojo.pack(anchor="center")

        self.question2_respuesta_label = tk.Label(self, textvariable=self.question2_respuesta)
        # self.question2_respuesta_label.pack(side="bottom")


        # # Pregunta 3
        self.question3_respuesta = tk.StringVar(value="Ninguno")
        self.question3_respuesta.trace("w", self.on_question3_respuesta_changed)

        self.question3_label = tk.Label(self, text="¿Qué tan estable es tu internet?")
        self.question3_label.pack(side="top")

        self.question3_respuesta_azul = tk.Radiobutton(self, text="Falla", variable=self.question3_respuesta, value="Falla")
        self.question3_respuesta_azul.pack(anchor="center")

        self.question3_respuesta_rojo = tk.Radiobutton(self, text="Estable", variable=self.question3_respuesta, value="Estable")
        self.question3_respuesta_rojo.pack(anchor="center")

        self.question3_respuesta_rojo = tk.Radiobutton(self, text="Excelente", variable=self.question3_respuesta, value="Excelente")
        self.question3_respuesta_rojo.pack(anchor="center")

        self.question3_respuesta_label = tk.Label(self, textvariable=self.question3_respuesta)
        # self.question3_respuesta_label.pack(side="bottom")

        # # Pregunta 4
        self.question4_respuesta = tk.StringVar(value="Ninguno")
        self.question4_respuesta.trace("w", self.on_question4_respuesta_changed)

        self.question4_label = tk.Label(self, text="¿Cuántas estrellas tendría que tener la aplicación para que la descargues, considerando que 5 es el más alto?")
        self.question4_label.pack(side="top")

        self.question4_respuesta_azul = tk.Radiobutton(self, text="Menos de 4", variable=self.question4_respuesta, value="Menos de 4")
        self.question4_respuesta_azul.pack(anchor="center")

        self.question4_respuesta_rojo = tk.Radiobutton(self, text="Entre 4 y 4.5", variable=self.question4_respuesta, value="Entre 4 y 4.5")
        self.question4_respuesta_rojo.pack(anchor="center")

        self.question4_respuesta_rojo = tk.Radiobutton(self, text="Más de 4.5", variable=self.question4_respuesta, value="Más de 4.5")
        self.question4_respuesta_rojo.pack(anchor="center")

        self.question4_respuesta_label = tk.Label(self, textvariable=self.question4_respuesta)
        # self.question4_respuesta_label.pack(side="bottom")

        # Pregunta 5
        self.question5_respuesta = tk.StringVar(value="Ninguno")
        self.question5_respuesta.trace("w", self.on_question5_respuesta_changed)

        self.question5_label = tk.Label(self, text="¿Qué tipo de categoría buscas?")
        self.question5_label.pack(side="top")

        self.question5_respuesta_azul = tk.Radiobutton(self, text="Juegos", variable=self.question5_respuesta, value="Juegos")
        self.question5_respuesta_azul.pack(anchor="center")

        self.question5_respuesta_rojo = tk.Radiobutton(self, text="Educación", variable=self.question5_respuesta, value="Educación")
        self.question5_respuesta_rojo.pack(anchor="center")

        self.question5_respuesta_label = tk.Label(self, textvariable=self.question5_respuesta)
        # self.question5_respuesta_label.pack(side="bottom")


        # Botón de salida
        # self.quit = tk.Button(self, text="Salir", fg="red", command=self.master.destroy)
        # self.quit.pack(side="left")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
