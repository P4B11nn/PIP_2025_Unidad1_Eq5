archivo = open("../Archivos/calificaciones_con_nombre.csv")
contenido = archivo.readlines()

print(contenido)
datos = [i.split(",") for i in contenido]

print(datos)

datos = [[i[0], list(map(int, i[1:]))] for i in datos ]

datos = [[i[0] , i [1], sum(i[1])/ len(i[1]) ] for i in datos]

nombres = [i[0] for i in datos]

promedios = [i[2]  for i in datos]

from matplotlib import pyplot as plt
import numpy as np

plt.show()

