from .archivo import Archivo
import re
import xml.etree.ElementTree as ET

class Xml(Archivo):

    def __init__(self, rutaArchivo: str, nombreArchivo: str):
        super().__init__(rutaArchivo, nombreArchivo)

    def lectura(self):
        try:
          # Parsear el archivo XML
          arbol = ET.parse(self._rutaArchivo)
    
          # Obtener la raíz del árbol XML
          raiz = arbol.getroot()
    
          # Crear un diccionario para almacenar los datos
          datos = {}
    
          # Iterar sobre los elementos hijos de la raíz
          for elemento in raiz:
            # Agregar el nombre del elemento y su texto al diccionario
            datos[elemento.tag] = elemento.text
            self.texto = str(datos)
    
            # Si necesitas imprimir los datos, puedes hacerlo aquí
            #print(datos)

        except FileNotFoundError:
            print(f"El archivo '{self._nombreArchivo}' no fue encontrado.")

        except Exception as e:
            print(f"Ocurrió un error: {e}")
    
    def contar(self, palabra:str):
        totalPalabras = super().contar(palabra)
        return len(totalPalabras)