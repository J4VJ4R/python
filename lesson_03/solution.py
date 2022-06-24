# NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para el funcionamiento de las libreria csv y json respectivamente
import csv
import json
"""NOTAS:
    - PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    - LA CONSOLA TE DIRa SI TU SOLUCIoN ES CORRECTA O NO
    - NO olvidar evaluar tu solucion
"""


"""Inicio espacio para programar funciones propias"""
# En este espacio podras programar las funciones que deseas usar en la funcion solucion (ES OPCIONAL)


"""Fin espacio para programar funciones propias"""


cabecera = ['Fecha', 'Comportamiento_de_la_accion',
            'Diferencia_absoluta_open-high']
# registros = []
sube = []
baja = []
estable = []
result1 = []
result2 = []
rowtxt = []


def solucion():
    with open('TWITTER.csv', 'r') as twitter_file:
        reader = csv.reader(twitter_file)
        c1 = 0
        for line in reader:
            result1.append((int(float(line[4]))) - int(float((line[1]))))
            c1 += 1
            if (result1[c1-1] > 0):
                sube.append('SUBE')
                result2.append((float(line[4]) - (float(line[1]))))
                rowtxt.append([line[0],sube[c1-1],result2[c1-1]])
            if (result1[c1-1] < 0):
                sube.append('BAJA')
                result2.append((float(line[4]) - (float(line[1]))))
                rowtxt.append([line[0],sube[c1-1],result2[c1-1]])
            if (result1[c1-1] == 0):
                sube.append('ESTABLE')
                result2.append((float(line[4]) - (float(line[1]))))
                rowtxt.append([line[0],sube[c1-1],result2[c1-1]])
     
    with open('analisis_archivo.csv', 'w') as csvfile:
        escritor = csv.writer(csvfile, delimiter=' ')
        # escritura de la cabecera
        escritor.writerow(cabecera)
        # escritura del cuerpo
        escritor.writerows(rowtxt)
solucion()
