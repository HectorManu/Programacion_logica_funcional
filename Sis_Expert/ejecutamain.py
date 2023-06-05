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

descripcion = """Este sistema inteligente te ayuda a descubrir aplicaciones de juegos y educativas de manera fácil y personalizada.

El sistema se basa en cinco factores principales para recomendarte las mejores opciones:

1. Gratis o de Pago: Puedes elegir entre aplicaciones gratuitas o aquellas que ofrecen características adicionales a cambio de un pago.

2. Puntaje de Estrellas: Las aplicaciones con mayor puntaje tienen una mejor calidad y son más populares entre los usuarios.

3. Calidad de Internet: El sistema considera tu conexión a Internet para recomendarte aplicaciones que se ajusten a tus necesidades y no tengan problemas de carga.

4. Restricciones de Edad: Las aplicaciones recomendadas son adecuadas para tu edad, brindándote una experiencia segura y adecuada.

5. Enfoque en Juegos o Educación: Puedes elegir si buscas aplicaciones de juegos entretenidos o aplicaciones educativas.

Cuando presiones 'Continuar', el sistema iniciará y te presentará recomendaciones personalizadas basadas en estos criterios. Obtendrás una selección óptima de aplicaciones de juegos y educación que se ajusten a tus preferencias y necesidades.

¡Explora nuevas aplicaciones y disfruta de una experiencia enriquecedora! Al presionar 'Continuar' en la interfaz, el sistema comenzará a brindarte las recomendaciones según los criterios mencionados.

NOTA: 
En caso de no encontrar aplicación se desplegará una ventana para el Experto que se encargará de rellenar la información, si no es experto NO LO RELLENE
"""



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

