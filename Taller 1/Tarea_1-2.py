
import numpy as np

Matriz1 = np.array([[3,4,6],[10,34,2],[6,10,1]])
Matriz2 = np.array([[4,7,8],[8,45,90],[1,35,12]])

print("La suma de los Matrizes es: \n", Matriz1 + Matriz2)
print("La resta de los Matrizes es: \n", Matriz1 - Matriz2)
print("El producto Punto es: \n", np.dot(Matriz1, Matriz2))  
print("El producto cruz es: \n", np.cross(Matriz1, Matriz2))

try:
    resultado = np.divide(Matriz1, Matriz2)
    print("La división de los Matrizes es: /n", resultado)
except ZeroDivisionError:
    print("No se puede dividir por cero.")

print("Proceso finalizado")