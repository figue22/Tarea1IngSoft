from contador.carpeta import Carpeta



print('------PRUEBA 1-------')
carpeta1 = Carpeta('./pruebas1')
carpeta1.palabraABuscar('arar')

print('------PRUEBA 2-------')
carpeta2 = Carpeta('./pruebas2')
carpeta2.palabraABuscar('foto')

print('------PRUEBA 3-------')
carpeta3 = Carpeta('./incorrecta')
carpeta3.palabraABuscar('ejemplo')

