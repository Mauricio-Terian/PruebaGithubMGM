# Este es para reconocer archivo de datos .txt
entrada_datos = "datos.txt"

# Vamos a leer de manera automática el archivo .txt
with open(entrada_datos, "r") as archivo:
    contenido = archivo.read()
 #Separamos el contenido con saltos de linea   
    lineas = contenido.split('\n')

# Archivo que se va a crear en formato .csv para leer en Excel
salida_datos = "conversion.csv"

# Crearemos el archivo .csv y lo abriremos en modo de escritura  
with open(salida_datos, "w") as archivo:

    # Encabezados de las columnas 
    archivo.write("RFC,RAZON SOCIAL,CODIGO POSTAL\n")

    # Escribiremos cada línea obtenida del archivo txt (realizamos un recorrido con un bucle for)
    for linea in lineas:

        # Escribimos en el archivo .csv de los datos que se obtuvieron del archivo .txt
        archivo.write(linea + "\n")
#Impresion de pantalla para confirmar que se creo el archivo.   
print("Archivo generado exitosamente")