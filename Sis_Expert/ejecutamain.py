import tkinter as tk
import subprocess

def execute_program():
    # Ocultar la ventana principal
    window.withdraw()

    # Ejecutar el otro programa usando subprocess
    subprocess.run(["python", "C:\\Users\\Hector Ruiz\\Desktop\\Universidad\\Programación Lógica y Funcional\\Programacion_logica_funcional\\Sis_Expert\\main.py"])

def close_window():
    # Cerrar la ventana
    window.destroy()

# Crear la ventana principal
window = tk.Tk()

# Configurar la ventana
window.title("Ventana de Inicio")
window.configure(bg="#F0F0F0")

descripcion = """Este sistema utiliza un enfoque inteligente para recomendar aplicaciones de juegos y educativas.\n\nSe basa en tres factores principales:\n\n• Puntaje de estrellas, velocidad de internet y restricciones de edad.\n\nEl puntaje de estrellas indica la calidad y popularidad de una aplicación. Cuanto mayor sea el puntaje, mejor será la experiencia.\n\nLa velocidad de internet se considera para asegurar una experiencia fluida y sin interrupciones al utilizar las aplicaciones.\n\nAdemás, se tienen en cuenta las restricciones de edad para garantizar que las aplicaciones sean adecuadas para el usuario.\n\nAl presionar 'Continuar', el programa iniciará y presentará recomendaciones personalizadas basadas en estos criterios, brindando a los usuarios una selección óptima de aplicaciones de juegos y educación.\n\nUna vez que presiones 'Continuar' en la interfaz, el programa se iniciará y comenzará a proporcionar las recomendaciones según los criterios mencionados."""

# Crear un widget de texto
text_label = tk.Label(window, text=descripcion, font=("Arial", 12), wraplength=400, justify="left", bg="#F0F0F0")
text_label.pack(pady=20, padx=10)

# Crear un botón para ejecutar el otro programa
execute_button = tk.Button(window, text="Continuar", command=execute_program, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", relief="flat", width=10)
execute_button.pack(pady=10)

# Crear un botón para cerrar la ventana
close_button = tk.Button(window, text="Cerrar", command=close_window, font=("Arial", 12), bg="#FF5252", fg="white", relief="flat", width=10)
close_button.pack(pady=5)

# Mostrar la ventana
window.mainloop()

