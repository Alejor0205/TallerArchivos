A continuación se plantean ejercicios que combinan la lectura, escritura y manipulación de archivos de texto, CSV, JSON y el manejo de excepciones.

1. **Leer y mostrar un archivo de texto línea a línea**

   - Crea un archivo `notas.txt` con varias líneas de texto (por ejemplo, títulos de películas).
   - Escribe un script que abra `notas.txt` en modo lectura y muestre cada línea numerada.
   - Si el archivo no existe, captura la excepción `FileNotFoundError` y muestra un mensaje amigable.

2. **Sobrescribir un archivo de texto y luego añadir contenido**

   - Crea (o sobrescribe) el archivo `diario.txt` y escribe en la primera línea:

     ```yaml
     Fecha: 2025-06-02
     ```

   - Luego, abre el mismo archivo en modo append (`'a'`) para agregar dos líneas más con tus actividades del día.

   - Al final, vuelve a abrir en `'r'` y muestra todo el contenido por pantalla.

3. **Crear un CSV de usuarios y leerlo**

   - Define una lista de diccionarios con los campos: `{"id": int, "nombre": str, "ciudad": str}` para al menos 5 usuarios ficticios.
   - Genera un archivo `usuarios.csv` con encabezado `id,nombre,ciudad` usando `csv.DictWriter`.
   - Escribe un script que lea con `csv.DictReader` y filtre solo los usuarios que vivan en “Bogotá”.
   - Maneja la excepción `FileNotFoundError` si el CSV no existe.

4. **Actualizar un CSV (lectura-escritura)**

   - Lee `usuarios.csv` y modifica la ciudad de un usuario dado (ej. cambiar al usuario con `id=3` a ciudad “Cali”).
   - Sobrescribe el mismo archivo con los cambios.
   - Asegúrate de usar un bloque `try-except` para capturar errores de lectura/escritura.

5. **Leer y escribir JSON de productos**

   - Crea un diccionario en Python con al menos 3 productos, cada uno con campos: `{"id": int, "nombre": str, "precio": float}`.
   - Escribe ese diccionario en `productos.json` con `json.dump(..., indent=2)`.
   - Luego, abre `productos.json`, cárgalo con `json.load()`, añade un nuevo producto y guarda de nuevo.
   - Captura al menos `json.JSONDecodeError` si el JSON está mal formado.

6. **Convertir CSV a JSON**

   - Toma el `usuarios.csv` del ejercicio anterior, léelo con `csv.DictReader` y conviértelo a una lista de diccionarios.
   - Guarda esa lista en `usuarios.json` usando `json.dump()`.
   - Si ocurre un error de lectura en CSV o JSON, debe manejarse con `try-except`.

7. **Manejo de excepciones en concatenación de (str + int)**

   - Pide al usuario que ingrese un nombre (string) y una edad (que se intente convertir a entero).
   - Intenta concatenar `"La edad de " + nombre + " es " + edad`.
   - Si `edad` no se puede convertir, captura el `ValueError` y pide reingresar el dato.