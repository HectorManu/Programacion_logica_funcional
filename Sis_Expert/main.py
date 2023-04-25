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

    
    # def guardar_info(self):
        
    
    
    
    
    def validacion(self):
        archivo = "datos.pickle"
        try:
            with open(archivo, "rb") as f:
                datos = pickle.load(f)
        except FileNotFoundError:
            datos = {}


        # for clave, valor in datos.items():
        #     if isinstance(valor, list) and len(valor) > 0:
        #         print(valor[1])
        #     else:
        #         print("El valor para la clave {} no es una lista o está vacío".format(clave))
        #         print("los valores son ",valor[clave])

        
        
        
        # COMPROBAR SI ESTA LO QUE BUSCO DE ACUERDO A LOS PARÁMETROS 
        for clave, valor in datos.items():
            # print("AQUÍ SALE ESTA MMDA",valor[0])
            if valor[0] == self.respuesta1:
                print(valor[0])
                None
            #     if valor[1] == self.respuesta2:
            #         None
            #         if valor[2] == self.respuesta3:
            #             None
            #             if valor[3] == self.respuesta4:
            #                 None
            #                 if valor[4] == self.respuesta5:
            #                     # SI LLEGO ENTONCES PUES SÍ ESTÁ XD
            #                     # COMO IMPRIMIR IMAGEN Y TEXTO PARA EL RESULTADO FINAL 
            
            #                     # imagen = Image.open("ruta/a/la/imagen.png")
            #                     # imagen = imagen.resize((300, 300))
            #                     # imagen_tk = ImageTk.PhotoImage(imagen)

            #                     # imagen_label = tk.Label(self, image=imagen_tk)
            #                     # imagen_label = tk.Label(self)
            #                     # imagen_label.pack()

            #                     texto_label = tk.Label(self, text=clave)
            #                     texto_label.place(relx=0.5, rely=0.1, anchor="center")

            #                     texto_label = tk.Label(self, text=valor[5])
            #                     texto_label.place(relx=0.5, rely=0.1, anchor="center")

            #                     # Crear un botón
            #                     button = tk.Button(self, text="Mostrar mensaje", command=lambda: messagebox.showinfo("Mensaje", "¡Hola mundo!"))

            #                     # Ubicar el botón al final de la ventana
            #                     button.place(side="bottom")
            #                     None
            #                 else:
            #                     # NO HAY
            #                     ## METODO PARA 
            #                     None
            #             else:
            #                 # NO HAY
            #                 None
            #         else:
            #             # NO HAY
            #             None
            #     else:
            #         # NO HAY
            #         None
            else:
                # NO HAY
                print("PUES NO HAY PERRO")
                None



        # SI NO HAY ENTONCES LLAMAR A LA FUNCIÓN QUE PONE EL TEXTO Y AGREGAR __NOMBRE__, __DESCRIPCIÓN__, __RUTA DE IMAGEN__
        
        
        # DE ESTAR LO QUE BUSCO IMPRIMO UNA IMAGEN Y UN BOTON QUE DESPLIEGA UNA SUBVENTANA FLOTANTE LA CUAL DA UNA EXPLICACIÓN 


        
        # descripcion = "Juego de mundo abierto, supervivencia y construcción que se puede jugar de un solo jugador o multi"
        # ruta = "/minecraft.jpeg"
        # nombre = "Minecraft"
        # atributos = [self.respuesta1,self.respuesta2,self.respuesta3,self.respuesta4,self.respuesta5,descripcion,ruta]
        



        # # Agregamos la información al diccionario
        # datos[nombre] = atributos

        # # Guardamos el diccionario en el archivo
        # with open(archivo, "wb") as f:
        #     pickle.dump(datos, f)

        
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






    def create_widgets(self):
        # Crear un botón
        # button = tk.Button(self, text="Mostrar mensaje", command=lambda: messagebox.showinfo("Mensaje", "¡Hola mundo!"))

        # Ubicar el botón al final de la ventana
        # button.pack(side="bottom")
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
        # self.question1_respuesta_label.pack(side="bottom")
        

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
