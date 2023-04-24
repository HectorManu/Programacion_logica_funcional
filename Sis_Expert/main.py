import tkinter as tk

def question_window(question, option1, option2):
    def option1_selected():
        result_label.config(text="Has seleccionado la opción 1")
        # Aquí puedes mostrar la imagen correspondiente a la opción 1
    def option2_selected():
        result_label.config(text="Has seleccionado la opción 2")
        # Aquí puedes mostrar la imagen correspondiente a la opción 2
    def answer_text():
        result_label.config(text="Tu respuesta es: " + answer_entry.get())
    window = tk.Tk()
    window.title("Pregunta")
    question_label = tk.Label(window, text=question)
    question_label.pack()
    option1_button = tk.Button(window, text=option1, command=option1_selected)
    option1_button.pack()
    option2_button = tk.Button(window, text=option2, command=option2_selected)
    option2_button.pack()
    answer_label = tk.Label(window, text="Si ninguna de las opciones aplica, por favor escribe tu respuesta aquí:")
    answer_label.pack()
    answer_entry = tk.Entry(window)
    answer_entry.pack()
    answer_button = tk.Button(window, text="Enviar respuesta", command=answer_text)
    answer_button.pack()
    result_label = tk.Label(window, text="")
    result_label.pack()
    window.mainloop()

def ask_question():
    question_window("¿Cuál es tu opción preferida?", "Opción 1", "Opción 2")

def show_image():
    image_window("ruta/a/la/imagen.png")

def option1_selected():
    result_label.config(text="Has seleccionado la opción 1")
    show_image("ruta/a/la/imagen_opcion1.png")

def option2_selected():
    result_label.config(text="Has seleccionado la opción 2")
    show_image("ruta/a/la/imagen_opcion2.png")

ask_question()

