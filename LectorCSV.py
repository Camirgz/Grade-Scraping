import csv
import tkinter as tk
from tkinter import filedialog
import csv


def abrir_archivo():
    # Abrir un cuadro de diálogo para seleccionar el archivo CSV
    nombre_archivo = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])
    if nombre_archivo:
        # Abrir el archivo CSV seleccionado en modo lectura
        with open(nombre_archivo, newline='') as archivo_csv:
            # Crear un objeto lector de CSV
            lector_csv = csv.reader(archivo_csv)

            # Leer cada línea del archivo CSV
            for linea in lector_csv:
                # Procesar la línea como desees
                print(linea)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Explorador de Archivos CSV")

# Botón para abrir el archivo CSV
boton_abrir = tk.Button(ventana, text="Abrir Archivo CSV", command=abrir_archivo)
boton_abrir.pack(pady=10)

# Ejecutar el bucle principal de la interfaz gráfica
ventana.mainloop()
