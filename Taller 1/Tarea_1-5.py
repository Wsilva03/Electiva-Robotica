import numpy as np

def calculo_x(rad):
    calculo=np.array([[1, 0, 0], [0, np.cos(radianes), -np.sin(radianes)], [0, np.sin(radianes), np.cos(radianes)]])
    return calculo
def calculo_y(rad):
    calculo1 = np.array([[np.cos(radianes), 0, np.sin(radianes)], [0, 1, 0],[-np.sin(radianes), 0, np.cos(radianes)]])
    return calculo1
def calculo_z(rad):
    calculo = np.array([[np.cos(radianes), -np.sin(radianes), 0], [np.sin(radianes), np.cos(radianes), 0],[0, 0, 1]])
    return calculo
# Rotación en el eje X
angulo = 45
radianes = np.radians(angulo)
matriz_rotacion_x = calculo_x (radianes)
print(f"Matriz de rotación en el eje X para un ángulo de {angulo} grados:\n{matriz_rotacion_x}\n")

# Rotación en el eje Y
matriz_rotacion_y = calculo_y(radianes)
print(f"Matriz de rotación en el eje Y para un ángulo de {angulo} grados:\n{matriz_rotacion_y}\n")

# Rotación en el eje Z
matriz_rotacion_z = calculo_z(radianes)
print(f"Matriz de rotación en el eje Z para un ángulo de {angulo} grados:\n{matriz_rotacion_z}")