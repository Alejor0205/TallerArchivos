import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def escribirArchivo():
    with open('diario.txt', mode='a', newline='') as agregar:
        agregar.write("Fecha: 2025-06-02")
        agregar.write(f"\n{input('Agregueeee la primera actividad de tu dia:  ' )}")
        agregar.write(f"\n{input('Agregueeee la segunda actividad de tu dia:  ' )}")
    with open ("diario.txt","r") as agregar:
        for enumerar, linea in enumerate(agregar,1):
            print(f"{enumerar}:{linea.strip()}")

escribirArchivo()