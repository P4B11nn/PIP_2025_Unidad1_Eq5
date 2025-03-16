#y  = mx + b

x = [i for i in range(-5, 5 + 1, 1)]

m = 3
b = 2

y = []

for i in x:
    y.append(m * i + b)

print(y)

from matplotlib import pyplot as plt
plt.plot(x, y,marker = 'X')
plt.show()

#Practica 4 ---> Probar otras maneras de personalizar el diseño de las graficas
