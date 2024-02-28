import csv
from .archivo import Archivo
import re

class Csv(Archivo):

    def __init__(self, rutaArchivo: str, nombreArchivo: str):
        super().__init__(rutaArchivo, nombreArchivo)



    def lectura(self):
        try:
          # Abrir el archivo CSV en modo de lectura
          with open(self._rutaArchivo, "r", newline="") as archivo:
              # Crear un lector CSV
              lector_csv = csv.DictReader(archivo)
        
              # Inicializar una lista para almacenar los datos
              datos = []
              
              # Iterar sobre las filas del archivo CSV
              for fila in lector_csv:
                  # Agregar cada fila como un diccionario a la lista de datos
                  datos.append(dict(fila))
                  self.texto = str(datos)

        except FileNotFoundError:
              print(f"El archivo '{self._nombreArchivo}' no fue encontrado.")

        except Exception as e:
              print(f"Ocurrió un error: {e}")
    
    def contar(self, palabra:str):
         totalPalabras = super().contar(palabra)
         return len(totalPalabras)