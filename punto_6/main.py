import csv
import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def leerCSV(path: str) -> list:
    try:
        with open(path, mode='r', newline='') as file:
            lector = csv.DictReader(file)
            return list(lector)
    except Exception as a:
        print(f"error al leer el archivo CSV: {a}")
        return []

def escribirJson(path: str, data: list):
    try:
        with open(path, mode='w') as file:
            json.dump(data, file, indent=2)
    except Exception as a:
        print(f"error al guardar el archivo JSON: {a}")


csvArchivo = "usuarios.csv"
jsonArchivo = "usuarios.json"

menu = """
*------------------------------------------*
|         Menu   csv y json                |
*------------------------------------------*
| 1. Leer archivo csv                      |
| 2. Convertir y guardar como Json         |
| 3. Salir                                 |
*------------------------------------------*
"""

usuariosCsv = []  
while True:
    print(menu)
    try:
        opcion = int(input("Seleccione opcion del menu:\n"))
    except ValueError:
        print("opcion no valida, intente de nuevo\n")
        continue

    if opcion == 1:
        usuariosCsv = leerCSV(csvArchivo)
        print("Usuarios cargados desde csv:")
        for usuario in usuariosCsv:
            print(f"{usuario['id']}, {usuario['nombre']}, {usuario['ciudad']}")
        print('---------------------------')
        
    elif opcion == 2:
            usuariosCsv = leerCSV(csvArchivo)
            escribirJson(jsonArchivo, usuariosCsv)

    elif opcion == 3:
        print("Saliendo es, saliendoooo")
        break

    else:
        print("Esta opcion no es valida\n")
