import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Solicitar al usuario que ingrese las coordenadas del vector
x = float(input("Ingrese la coordenada X del vector: "))
y = float(input("Ingrese la coordenada Y del vector: "))
z = float(input("Ingrese la coordenada Z del vector: "))

 # Crear una figura y un conjunto de ejes 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibujar el vector desde el origen hasta las coordenadas ingresadas por el usuario
ax.quiver(0, 0, 0, x, y, z, color='b', label='Vector')
# Establecer límites de los ejes
ax.set_xlim([0, max(1, x)])
ax.set_ylim([0, max(1, y)])
ax.set_zlim([0, max(1, z)])

# Etiquetas de los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mostrar la leyenda
ax.legend()

# Mostrar el gráfico
plt.show()