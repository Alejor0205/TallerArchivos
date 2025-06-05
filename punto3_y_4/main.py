import csv
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def leerArchivoCSV(path: str) -> list:
    try:
        with open(path, mode='r', newline='') as file:
            filas = csv.DictReader(file)
            return list(filas)
    except FileNotFoundError:
        print(f" El archivo no fue encontrado parceirooooo")
        return  

def escribirArchivoCSV(path: str, lineas: list, encabezados: list, mode = 'w'):
    try:
        with open(path, mode=mode, newline= '') as file:
            escritor = csv.DictWriter(file, fieldnames=encabezados)
            escritor.writeheader()
            escritor.writerows(lineas)
    except Exception:
        print(f"error al escribir el archivo")


def filtrarUsuario(usuarios: list, ciudad: str):
    print(f"Usuarios que viven en {ciudad}:")
    for usuario in usuarios:
        if usuario["ciudad"].lower() == ciudad.lower():
            print(f"id: {usuario['id']}, Nombre: {usuario['nombre']}, Ciudad: {usuario['ciudad']}")
   

archivo = "usuarios.csv"

encabezados = [ "id","nombre","ciudad"]        

listas = [
  {"id": 1, "nombre": "Alejandro", "ciudad": "Bucaramanga"},
  {"id": 2, "nombre": "Luis", "ciudad": "Bogota"},
  {"id": 3, "nombre": "Maria", "ciudad": "Valledupar"},
  {"id": 4, "nombre": "Dario", "ciudad": "Bucaramanga"},
  {"id": 5, "nombre": "Jose", "ciudad": "Bogota"}
]

menu = """
*-----------------------------------------*
|          Menu   usuairos csv            |
*-----------------------------------------*
| 1. Escribir lista al archivo csv        |
| 2. Leer usuarios del archivo csv        |
| 3. Filtrar usuarios que viven en Bogota |
| 4. Salir                                |
*-----------------------------------------*
"""

while True:
    print(menu)
    try:
        opcion = int(input("Seleccione opcion del menu:\n"))
    except ValueError:
        print("opcion no valida, intente de nuevo\n")
        continue
    if opcion == 1:
        escribirArchivoCSV(archivo, listas, encabezados)
    elif opcion == 2:
        usuarios = leerArchivoCSV(archivo)
        print("Usuarios en el archivo:")
        for u in usuarios:
             print(f"id: {u['id']}, Nombre: {u['nombre']}, Ciudad: {u['ciudad']}")
             print()
    elif opcion == 3:
            usuarios = leerArchivoCSV(archivo)
            filtrarUsuario(usuarios, "Bogota")
            print()
    elif opcion == 4:
        print("Saliendo del programa")
        break
    else:
        print("Opcion no valida intente de nuevo\n")
