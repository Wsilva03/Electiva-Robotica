import numpy as np

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
print ("La suma de los vectores es: ", vector1 + vector2)
print ("La resta de los vectores es: ", vector1 - vector2)
print ("El producto Punto es:", np.dot(vector1, vector2))
print ("El producto cruz es:", np.cross(vector1, vector2))

try:
    print ("La division de los vectores es: ", np.divide(vector1, vector2))
except ZeroDivisionError:
    print("No se puede dividir por cero.")

print("proceso finalizado")