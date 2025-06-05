import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def leerArchivo():
    archivo = ("notas.txt")
    try:
        with open(archivo, "r") as file:
            for enumerar, linea  in enumerate(file,1):
             print(f"{enumerar}:{linea.strip()}")
    except FileNotFoundError:
        print("El archivo  no se encuetra mi parceroooo")
leerArchivo()
