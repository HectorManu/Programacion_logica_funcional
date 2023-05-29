import pickle

# Crear un diccionario
datos = {
    "Monument Valley": ["No", "Menor de edad","Falla","Más de 4.5","Juegos","Monument Valley es un cautivador juego de rompecabezas en el que debes manipular arquitecturas imposibles para guiar a una princesa a través de un mundo surrealista y visualmente impresionante.", "/Monument_Valley.jpeg"]
}

# Guardar el diccionario en un archivo
with open("datos.pickle", "wb") as archivo:
    pickle.dump(datos, archivo)