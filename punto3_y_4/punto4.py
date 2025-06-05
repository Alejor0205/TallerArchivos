import csv
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def leerArchivoCSV(path: str) -> list:
    try:
        with open(path, mode='r', newline='') as file:
            filas = csv.DictReader(file)
            return list(filas)
    except FileNotFoundError:
        print(f"error en el archivo no se encontro")  
    
def escribirArchivoCSV(path: str, lineas: list, encabezados: list, mode='w'):
    try:
        with open(path, mode=mode, newline='') as file:
            escritor = csv.DictWriter(file, fieldnames=encabezados)
            escritor.writeheader()
            escritor.writerows(lineas)
    except Exception:
        print(f"error al escribir el archivo")

def updateUsuario(usuarios: list, userId: int, nuevaCiudad: str) -> list:
    update = []
    for usuario in usuarios:
        if int(usuario["id"]) == userId:
            usuario["ciudad"] = nuevaCiudad
        update.append(usuario)
    return update        

archivo = ("usuarios.csv")

encabezados = ["id","nombre","ciudad"]     
idUpdate= int(input("Agrege el id que vas a cambiar cambiar:\n"))   
_ciudad= (input("Agrege la ciudad que necesita cambiar:\n"))
print()

_usuarios = leerArchivoCSV(archivo)
usuarioUpdate = updateUsuario(_usuarios, userId=idUpdate, nuevaCiudad=_ciudad)
escribirArchivoCSV(archivo, usuarioUpdate, encabezados)

print("Su archivo fue actualizado:\n")
for i in usuarioUpdate:
    print(f"{i['id']}, {i['nombre']}, {i['ciudad']}")