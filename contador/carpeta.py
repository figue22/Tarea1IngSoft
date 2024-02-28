
import os 
from .archivo import Archivo
from contador.json import Json
from contador.csv import Csv
from contador.xml import Xml
from contador.txt import Txt



class Carpeta:

    def __init__(self, ruta:str) -> None:
        self.ruta = ruta
        self.archivos = []
        self.crearArchivos()


    def verificarCarpetas(self):
        if not os.path.isdir(self.ruta):
            print(f'Mensaje indicado que no se encuentra en la carpeta indicada ({self.ruta})')
            return False
        return True

    #metodo para agregar los nombres de los archivos dentro de la carpeta a el arreglo.
    def crearArchivos(self):
        if self.verificarCarpetas():
            for nombreArchivo in os.listdir(self.ruta):
                #Obtenemos la ruta completa

                rutaCompleta = os.path.isfile(f'{self.ruta}/{nombreArchivo}')

            # Verificamos si es archivo
                if rutaCompleta:
                    #Obtenemos su extension
                    extension = nombreArchivo.split('.')[-1].lower()
                    
                    #Verificar el tipo de archivo
                    if extension == 'json':
                        self.archivos.append(Json(f'{self.ruta}/{nombreArchivo}', nombreArchivo))
                    if extension == 'csv':
                        self.archivos.append(Csv(f'{self.ruta}/{nombreArchivo}', nombreArchivo))
                    if extension == 'txt':
                        self.archivos.append(Txt(f'{self.ruta}/{nombreArchivo}', nombreArchivo))
                    if extension == 'xml':
                        self.archivos.append(Xml(f'{self.ruta}/{nombreArchivo}', nombreArchivo))
                    if extension not in ['json', 'csv', 'txt', 'xml']:
                        print(f'No se encontraton archivos de texto en la carpeta {self.ruta}') 


    def palabraABuscar(self, palabra: str):
        total = 0
        for archivo in self.archivos:
            cantidad = archivo.contar(palabra)
            total += cantidad
            print(f'El archivo {archivo._nombreArchivo} tiene {cantidad} veces la palabra {palabra}')

        print(f'En total hay {total}')


 
        