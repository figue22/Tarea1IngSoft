import re
from .archivo import Archivo

class Txt(Archivo):

    def __init__(self, rutaArchivo: str, nombreArchivo: str):
        super().__init__(rutaArchivo, nombreArchivo)

    def lectura(self):
        try:
            # Abrir el archivo en modo de lectura
            with open(self._rutaArchivo, "r") as archivo:
            # Leer el contenido del archivo y guardarlo en una variable
                 contenido = archivo.read()
                 self.texto = contenido
                 
        except FileNotFoundError:
            print(f"El archivo '{self._nombreArchivo}' no fue encontrado.")

        except Exception as e:
            print(f"Ocurrió un error: {e}")

    
    def contar(self, palabra:str):
         totalPalabras = super().contar(palabra)
         return len(totalPalabras)



        