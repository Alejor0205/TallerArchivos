def validicacionDeEdad():
    while True:
        nombre = input("Ingresa tu nombre: ")
        try:
            edad = int(input("Ingresa tu edad: "))
            print(f"La edad de {nombre} es {edad}")
            break
        except ValueError:
            print("Edad es invalida  \nvuelva intentar")
    
validicacionDeEdad()