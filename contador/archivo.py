from abc import ABC, abstractmethod
import re




class Archivo(ABC):

    def __init__(self, rutaArchivo: str, nombreArchivo: str):
        self._rutaArchivo = rutaArchivo
        self._nombreArchivo = nombreArchivo
        self.texto = ''


    def contar(self, palabra:str):
        self.lectura()
          # Usar expresión regular para encontrar ocurrencias exactas de la palabra
          # Se busca la palabra entre límites de palabra completa (\b)
        totalPalabras = re.findall(r'\b' + re.escape(palabra) + r'\b', self.texto, flags=re.IGNORECASE)
        return totalPalabras

    @abstractmethod
    def lectura(self, palabra:str):
        pass
    
            