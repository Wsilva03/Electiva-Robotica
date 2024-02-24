import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def dibujar_vector(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Dibuja el vector
    ax.quiver(0, 0, 0, x, y, z, color='b', label='Vector')

    # Ajusta los límites del gráfico
    max_coordinate = max(x, y, z)
    ax.set_xlim([0, max_coordinate])
    ax.set_ylim([0, max_coordinate])
    ax.set_zlim([0, max_coordinate])

    # Etiqueta los ejes
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')

    # Muestra la leyenda
    ax.legend()

    # Muestra el gráfico
    plt.show()

# Solicitar al usuario que ingrese las coordenadas del vector
x = float(input("Ingrese la coordenada x del vector: "))
y = float(input("Ingrese la coordenada y del vector: "))
z = float(input("Ingrese la coordenada z del vector: "))

# Llamar a la función para dibujar el vector
dibujar_vector(x, y, z)
