import pickle

def eliminaUnaApp(name):
    # Cargar el diccionario desde el archivo
    with open("datos.pickle", "rb") as archivo:
        datos = pickle.load(archivo)

    # Verificar si "Manuals Cars" está en el diccionario
    if name in datos:
        # Eliminar la entrada correspondiente a name
        del datos[name]

    # Guardar el diccionario actualizado en el archivo
    with open("datos.pickle", "wb") as archivo:
        pickle.dump(datos, archivo)

name = "Bubble Shooter Rainbow"
eliminaUnaApp(name)