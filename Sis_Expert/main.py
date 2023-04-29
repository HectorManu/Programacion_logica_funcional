import tkinter as tk
import pickle
from tkinter import messagebox
from PIL import Image, ImageTk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def on_question1_respuesta_changed(self, *args):
        # print(f"Seleccionaste: {self.question1_respuesta.get()}")
        self.respuesta1 = ""
        if self.question1_respuesta.get() == "Sí":
            self.respuesta1 = "Si"
        else:
            self.respuesta1 = "No"

    def on_question2_respuesta_changed(self, *args):
        # print(f"Seleccionaste: {self.question2_respuesta.get()}")
        self.respuesta2 = ""
        if self.question2_respuesta.get() == "Menor de edad":
            self.respuesta2 = "Menor de edad"
        elif self.question2_respuesta.get() == "Joven o adolescente":
            self.respuesta2 = "Joven o adolescente"
        elif self.question2_respuesta.get() == "Adulto responsable":
            self.respuesta2 = "Adulto responsable"

    def on_question3_respuesta_changed(self, *args):
        # print(f"Seleccionaste: {self.question3_respuesta.get()}")
        self.respuesta3 = ""
        if self.question3_respuesta.get() == "Falla":
            self.respuesta3 = "Falla"
        elif self.question3_respuesta.get() == "Estable":
            self.respuesta3 = "Estable"
        elif self.question3_respuesta.get() == "Excelente":
            self.respuesta3 = "Excelente"

    def on_question4_respuesta_changed(self, *args):
        # print(f"Seleccionaste: {self.question4_respuesta.get()}")
        self.respuesta4 = ""
        if self.question4_respuesta.get() == "Más de 4.5":
            self.respuesta4 = "Más de 4.5"
        elif self.question4_respuesta.get() == "Entre 4 y 4.5":
            self.respuesta4 = "Entre 4 y 4.5"
        elif self.question4_respuesta.get() == "Menos de 4":
            self.respuesta4 = "Menos de 4"

    def on_question5_respuesta_changed(self, *args):
        # print(f"Seleccionaste: {self.question5_respuesta.get()}")
        self.respuesta5 = ""
        if self.question5_respuesta.get() == "Juegos":
            self.respuesta5 = "Juegos"
            self.validacion()
        elif self.question5_respuesta.get() == "Educación":
            self.respuesta5 = "Educación"
            self.validacion()

    def validacion(self):
        archivo = "datos.pickle"
        try:
            with open(archivo, "rb") as f:
                datos = pickle.load(f)
        except FileNotFoundError:
            datos = {}

        # COMPROBAR SI ESTA LO QUE BUSCO DE ACUERDO A LOS PARÁMETROS 
        for clave, valor in datos.items():
            # print("AQUÍ SALE ESTA MMDA",valor[0])
            if valor[0] == self.respuesta1:
                print(valor[0])
                if valor[1] == self.respuesta2:
                    print(valor[1])
                    if valor[2] == self.respuesta3:
                        print(valor[2])
                        if valor[3] == self.respuesta4:
                            print(valor[3])
                            if valor[4] == self.respuesta5:
                                print(valor[4])
                                print(f'El juego que consultaste es: {clave}')
                                print(f'La descripción es: {valor[5]}')
                                print(f'La ruta de la imagen es: {valor[6]}')
                            else:
                                ## METODO PARA 
                                print(f"No coincidio con {self.respuesta5}")
                        else:
                            print(f"No coincidio con {self.respuesta4}")
                    else:
                        print(f"No coincidio con {self.respuesta3}")
                else:
                    print(f"No coincidio con {self.respuesta2}")
            else:
                print(f"No coincidio con {self.respuesta1}")

        # SI NO HAY ENTONCES LLAMAR A LA FUNCIÓN QUE PONE EL TEXTO Y AGREGAR __NOMBRE__, __DESCRIPCIÓN__, __RUTA DE IMAGEN__
        
        # DE ESTAR LO QUE BUSCO IMPRIMO UNA IMAGEN Y UN BOTON QUE DESPLIEGA UNA SUBVENTANA FLOTANTE LA CUAL DA UNA EXPLICACIÓN

    def guardar_datos(self):
        print("Estoy guardando cosas")

    def create_widgets(self):
        # Pregunta 1

        self.question1_respuesta = tk.StringVar(value="Ninguno")
        self.question1_respuesta.trace("w", self.on_question1_respuesta_changed)

        self.question1_label = tk.Label(self, text="¿Prefieres una aplicación gratuita (SI) o estás dispuesto a pagar por características adicionales (NO)?")
        self.question1_label.pack(side="top")

        self.question1_respuesta_azul = tk.Radiobutton(self, text="Sí", variable=self.question1_respuesta, value="Sí")
        self.question1_respuesta_azul.pack(anchor="center")

        self.question1_respuesta_rojo = tk.Radiobutton(self, text="No", variable=self.question1_respuesta, value="No")
        self.question1_respuesta_rojo.pack(anchor="center")

        self.question1_respuesta_label = tk.Label(self, textvariable=self.question1_respuesta)

        # Pregunta 2
        self.question2_respuesta = tk.StringVar(value="Ninguno")
        self.question2_respuesta.trace("w", self.on_question2_respuesta_changed)

        self.question2_label = tk.Label(self, text="¿Qué edad tiene el usuario?")
        self.question2_label.pack(side="top")

        self.question2_respuesta_azul = tk.Radiobutton(self, text="Menor de edad", variable=self.question2_respuesta, value="Menor de edad")
        self.question2_respuesta_azul.pack(anchor="center")

        self.question2_respuesta_rojo = tk.Radiobutton(self, text="Joven o adolescente", variable=self.question2_respuesta, value="Joven o adolescente")
        self.question2_respuesta_rojo.pack(anchor="center")

        self.question2_respuesta_rojo = tk.Radiobutton(self, text="Adulto responsable", variable=self.question2_respuesta, value="Adulto responsable")
        self.question2_respuesta_rojo.pack(anchor="center")

        self.question2_respuesta_label = tk.Label(self, textvariable=self.question2_respuesta)

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

        # Pregunta 4
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
        

root = tk.Tk()
app = Application(master=root)
app.mainloop()
