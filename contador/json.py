from .archivo import Archivo
import json
import re

class Json(Archivo):

    def __init__(self, rutaArchivo: str, nombreArchivo: str):
        super().__init__(rutaArchivo, nombreArchivo)
        

    def lectura(self):
        try:
          # Abrir el archivo en modo de lectura
          with open(self._rutaArchivo, "r") as archivo:
            # Cargar el contenido del archivo JSON en una variable
            datos = json.load(archivo)
            self.texto = str(datos)
            
        except FileNotFoundError:
           print(f"El archivo '{self._nombreArchivo}' no fue encontrado.")

        except json.JSONDecodeError as e:
         print(f"Error al decodificar el archivo JSON: {e}")

        except Exception as e:
          print(f"Ocurrió un error: {e}")


    def contar(self, palabra:str):
        totalPalabras = super().contar(palabra)
        return len(totalPalabras)


        