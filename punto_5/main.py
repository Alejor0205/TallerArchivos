import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def leerJson(path: str):
    try:
        with open(path, 'r') as file:
            datos = json.load(file)
            return datos
    except json.JSONDecodeError:
        print(f"error el JSON esta mal")
        
def escribirJson(path: str, data: list):
        with open(path, 'w') as file:
            json.dump(data, file, indent=2)
        
productos= [
    {"id": 1, "nombre": "Libro", "precio": 5_000},
    {"id": 2, "nombre": "Cuaderno", "precio": 3_500},
    {"id": 3, "nombre": "Lapiz", "precio": 1_000}
]

archivoJson = "productos.json"

menu = """
*-------------------------------------*
|         menu   productoscsv         |
*-------------------------------------*
| 1. Guardar productos                |
| 2. Leer y mostrar productos         |
| 3. Añadir nuevo producto            |
| 4. Salir                            |
*-------------------------------------*
"""

while True:
    print(menu)
    try:
        opcion = int(input("Seleccione opcion del menu:\n"))
    except ValueError:
        print("opcion no valida, intente de nuevo\n")
        continue

    if opcion == 1:
        escribirJson(archivoJson, productos)

    elif opcion == 2:
        datos = leerJson(archivoJson)
        print("Productos")
        for p in datos:
            print(f'Id: {p['id']}, Nombre: {p['nombre']}, Precio: ${p['precio']}')
        print()

    elif opcion == 3:
        datos = leerJson(archivoJson)
        try:
            nuevoId = int(input("Ingrese ID del nuevo producto:\n"))
            nuevoNombre = input("Ingrese nombre del nuevo producto:\n")
            nuevoPrecio = float(input("Ingrese precio del nuevo producto:\n"))
        except ValueError:
            print("Datos inválidos, ID debe ser entero y precio número decimal.\n")
            continue
        
        nuevoProducto = {"id": nuevoId, "nombre": nuevoNombre, "precio": nuevoPrecio}
        datos.append(nuevoProducto)
        escribirJson(archivoJson, datos)

    elif opcion == 4:
        print("Saliendo es, saliendoooo")
        break

    else:
        print("Esta opcion no es valida\n")
