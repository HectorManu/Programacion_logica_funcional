import tkinter as tk
import pickle
from tkinter import messagebox
from PIL import Image, ImageTk

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Sistema Experto para Juegos y Educación")
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
            # self.boton_para_validacion()
        elif self.question5_respuesta.get() == "Educación":
            self.respuesta5 = "Educación"
            # self.boton_para_validacion()

    # def boton_para_validacion(self):

    def validacion(self):
        self.archivo = "datos.pickle"
        try:
            with open(self.archivo, "rb") as f:
                self.datos = pickle.load(f)
        except FileNotFoundError:
            self.datos = {}
        
        false = []

        # COMPROBAR SI ESTA LO QUE BUSCO DE ACUERDO A LOS PARÁMETROS 
        for clave, valor in self.datos.items():
            self.valores_recorridos(clave,valor)
            # print(self.valor)
            print(f"aquí es  lo que determinará la parte de {self.valor}")  
            false.append(self.valor)

        print(false)

        if any(false):
            None
        else:
            self.validar_for()
        
    def valores_recorridos(self, clave, valor):
        print(clave)
        print(valor)
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
                            self.descripcion = valor[5]
                            self.ruta = valor[6]
                            self.nombre = clave
                            self.valor = True
                            self.validar_for()
                            return True
                        else:
                            self.valor = False
                    else:
                        self.valor = False
                else:
                    self.valor = False
            else:
                self.valor = False
        else:
            self.valor = False
    
    def validar_for(self):
        print(f"el valor valor paso {self.valor}")
        if self.valor == True:
            self.create_image_frame()
            
            # Crear el botón
            self.create_button() 
            
        else:
            self.create_textboxes()
            self.create_buttons()

    def create_widgets(self):

        # Pregunta 1

        self.question1_respuesta = tk.StringVar(value="Ninguno")
        self.question1_respuesta.trace("w", self.on_question1_respuesta_changed)

        self.question1_label = tk.Label(self, text="¿Prefieres una aplicación gratuita (SI) o estás dispuesto a pagar por características adicionales (NO)?")
        self.question1_label.config(font=("Arial", 11, "bold")) 
        self.question1_label.pack(side="top")

        self.question1_respuesta_si = tk.Radiobutton(self, text="Sí", variable=self.question1_respuesta, value="Sí")
        self.question1_respuesta_si.config(font=("Arial", 10))
        self.question1_respuesta_si.pack(anchor="center")

        self.question1_respuesta_no = tk.Radiobutton(self, text="No", variable=self.question1_respuesta, value="No")
        self.question1_respuesta_no.config(font=("Arial", 10))
        self.question1_respuesta_no.pack(anchor="center")

        self.question1_respuesta_label = tk.Label(self, textvariable=self.question1_respuesta)

        # Pregunta 4
        self.question4_respuesta = tk.StringVar(value="Ninguno")
        self.question4_respuesta.trace("w", self.on_question4_respuesta_changed)

        self.question4_label = tk.Label(self, text="¿Cuántas estrellas tendría que tener la aplicación para que la descargues, considerando que 5 es el más alto?")
        self.question4_label.config(font=("Arial", 11, "bold")) 
        self.question4_label.pack(side="top")

        self.question4_respuesta_menosde4 = tk.Radiobutton(self, text="Menos de 4", variable=self.question4_respuesta, value="Menos de 4")
        self.question4_respuesta_menosde4.config(font=("Arial", 10))
        self.question4_respuesta_menosde4.pack(anchor="center")

        self.question4_respuesta_entre = tk.Radiobutton(self, text="Entre 4 y 4.5", variable=self.question4_respuesta, value="Entre 4 y 4.5")
        self.question4_respuesta_entre.config(font=("Arial", 10))
        self.question4_respuesta_entre.pack(anchor="center")

        self.question4_respuesta_masde45 = tk.Radiobutton(self, text="Más de 4.5", variable=self.question4_respuesta, value="Más de 4.5")
        self.question4_respuesta_masde45.config(font=("Arial", 10))
        self.question4_respuesta_masde45.pack(anchor="center")

        self.question4_respuesta_label = tk.Label(self, textvariable=self.question4_respuesta)

        # Pregunta 3
        self.question3_respuesta = tk.StringVar(value="Ninguno")
        self.question3_respuesta.trace("w", self.on_question3_respuesta_changed)

        self.question3_label = tk.Label(self, text="¿Qué tan estable es tu internet?")
        self.question3_label.config(font=("Arial", 11, "bold")) 
        self.question3_label.pack(side="top")

        self.question3_respuesta_falla = tk.Radiobutton(self, text="Falla", variable=self.question3_respuesta, value="Falla")
        self.question3_respuesta_falla.config(font=("Arial", 10))
        self.question3_respuesta_falla.pack(anchor="center")

        self.question3_respuesta_estable = tk.Radiobutton(self, text="Estable", variable=self.question3_respuesta, value="Estable")
        self.question3_respuesta_estable.config(font=("Arial", 10))
        self.question3_respuesta_estable.pack(anchor="center")

        self.question3_respuesta_excelente = tk.Radiobutton(self, text="Excelente", variable=self.question3_respuesta, value="Excelente")
        self.question3_respuesta_excelente.config(font=("Arial", 10))
        self.question3_respuesta_excelente.pack(anchor="center")

        self.question3_respuesta_label = tk.Label(self, textvariable=self.question3_respuesta)


        # Pregunta 2
        self.question2_respuesta = tk.StringVar(value="Ninguno")
        self.question2_respuesta.trace("w", self.on_question2_respuesta_changed)

        self.question2_label = tk.Label(self, text="¿Qué edad tiene el usuario?")
        self.question2_label.config(font=("Arial", 11, "bold")) 
        self.question2_label.pack(side="top")

        self.question2_respuesta_menor = tk.Radiobutton(self, text="Menor de edad", variable=self.question2_respuesta, value="Menor de edad")
        self.question2_respuesta_menor.config(font=("Arial", 10))
        self.question2_respuesta_menor.pack(anchor="center")

        self.question2_respuesta_joven = tk.Radiobutton(self, text="Joven o adolescente", variable=self.question2_respuesta, value="Joven o adolescente")
        self.question2_respuesta_joven.config(font=("Arial", 10))
        self.question2_respuesta_joven.pack(anchor="center")

        self.question2_respuesta_adulto = tk.Radiobutton(self, text="Adulto responsable", variable=self.question2_respuesta, value="Adulto responsable")
        self.question2_respuesta_adulto.config(font=("Arial", 10))
        self.question2_respuesta_adulto.pack(anchor="center")

        self.question2_respuesta_label = tk.Label(self, textvariable=self.question2_respuesta)

        # Pregunta 5
        self.question5_respuesta = tk.StringVar(value="Ninguno")
        self.question5_respuesta.trace("w", self.on_question5_respuesta_changed)

        self.question5_label = tk.Label(self, text="¿Qué tipo de categoría buscas?")
        self.question5_label.config(font=("Arial", 11, "bold")) 
        self.question5_label.pack(side="top")

        self.question5_respuesta_juegos = tk.Radiobutton(self, text="Juegos", variable=self.question5_respuesta, value="Juegos")
        self.question5_respuesta_juegos.config(font=("Arial", 10))
        self.question5_respuesta_juegos.pack(anchor="center")

        self.question5_respuesta_edu = tk.Radiobutton(self, text="Educación", variable=self.question5_respuesta, value="Educación")
        self.question5_respuesta_edu.config(font=("Arial", 10))
        self.question5_respuesta_edu.pack(anchor="center")

        self.question5_respuesta_label = tk.Label(self, textvariable=self.question5_respuesta)

            # Botón para validación
        self.validacion_button_frame = tk.Frame(self)
        self.validacion_button_frame.pack(pady=10)

        self.validacion_button = tk.Button(self.validacion_button_frame, text="Buscar", command=self.validacion,  bg="#4CAF50", fg="white", relief="flat", width=10)
        self.validacion_button.config(font=("Arial", 10))
        self.validacion_button.pack()
        
        
    def create_image_frame(self):
        self.image_frame = tk.Frame(self.master)
        self.image_frame.pack(side="bottom", pady=10, fill="both", expand=True)

        # Agregar una etiqueta para el texto
        self.text_label = tk.Label(self.image_frame, text=self.nombre)
        self.text_label.pack(side="top")

        # Cargar una imagen y agregarla al marco
        self.load_and_add_image()

    def load_and_add_image(self):
        image = Image.open(f"./{self.ruta}")  # Reemplazar "imagen.png" con la ruta de la imagen
        image = image.resize((125, 125))
        photo = ImageTk.PhotoImage(image)
        self.image_label = tk.Label(self.image_frame, image=photo)
        self.image_label.image = photo  # Mantener una referencia a la imagen para evitar que sea eliminada por el recolector de basura
        self.image_label.pack(side="top", padx=10, pady=10)

    def create_button(self):
        self.button = tk.Button(self.image_frame, text="Imprimir descripción", command=self.print_text,bg="#4CAF50", fg="white", relief="flat", width=10)
        self.button.pack(side="top")

        self.regresar_button = tk.Button(self.image_frame, text="Regresar", command=self.regresar_pri, bg="#FF5252", fg="white", relief="flat", width=10)
        self.regresar_button.pack(side="top")

    def regresar_pri(self):
        # Restablecer la variable a su valor predeterminado
        self.question1_respuesta.set("Ninguno")
        self.question2_respuesta.set("Ninguno")
        self.question3_respuesta.set("Ninguno")
        self.question4_respuesta.set("Ninguno")
        self.question5_respuesta.set("Ninguno")
        self.regresar_button.pack_forget()
        self.button.pack_forget()
        self.image_label.pack_forget()
        self.text_label.pack_forget()
        self.image_frame.pack_forget()
        self.regresar_button.pack_forget()

    def print_text(self):
        # Crear una nueva ventana
        self.popup_window = tk.Toplevel()
        self.popup_window.title("Descripción")
        self.popup_window.geometry("200x100")

        # Agregar una etiqueta con el texto a imprimir
        self.print_label = tk.Label(self.popup_window, text=self.descripcion, wraplength=180)
        self.print_label.pack(pady=10)

        # Agregar un botón para cerrar la ventana flotante
        self.close_button = tk.Button(self.popup_window,text="Cerrar", command=self.popup_window.destroy)
        self.close_button.pack(pady=10)

    def create_textboxes(self):
        # Cuadros de texto
        self.textbox1_label = tk.Label(self, text="Nombre de la aplicación:")
        self.textbox1_label.pack()

        self.textbox1 = tk.Entry(self)
        self.textbox1.pack()

        self.textbox2_label = tk.Label(self, text="Inserta descripción:")
        self.textbox2_label.pack()

        self.textbox2 = tk.Entry(self)
        self.textbox2.pack()

        self.textbox3_label = tk.Label(self, text="Inserta ruta de la imágen:")
        self.textbox3_label.pack()

        self.textbox3 = tk.Entry(self)
        self.textbox3.pack()

    def create_buttons(self):
        # Botones
        self.guardar_button = tk.Button(self, text="Guardar", command=self.guardar_respuestas)
        self.guardar_button.pack(side="left")

        self.regresar_button = tk.Button(self, text="Regresar", command=self.regresar)
        self.regresar_button.pack(side="right")

    def guardar_respuestas(self):

        # guardar los valores en un diccionario
        nombre = self.textbox1.get()
        atributos = [self.respuesta1,self.respuesta2,self.respuesta3,self.respuesta4,self.respuesta5,self.textbox2.get(),self.textbox3.get()]

        # Agregamos la información al diccionario
        self.datos[nombre] = atributos

        # Guardamos el diccionario en el self.archivo
        with open(self.archivo, "wb") as f:
            pickle.dump(self.datos, f)

        self.regresar()

        # Mostrar un mensaje de confirmación
        messagebox.showinfo("Respuestas guardadas", "Las respuestas han sido guardadas correctamente.")

    def regresar(self):
        # Ocultar los cuadros de texto y los botones
        self.textbox1_label.pack_forget()
        self.textbox1.pack_forget()
        self.textbox2_label.pack_forget()
        self.textbox2.pack_forget()
        self.textbox3_label.pack_forget()
        self.textbox3.pack_forget()
        self.guardar_button.pack_forget()
        self.regresar_button.pack_forget()
        
root = tk.Tk()
app = Application(master=root)
app.mainloop()
