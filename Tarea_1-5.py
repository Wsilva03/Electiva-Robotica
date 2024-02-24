import numpy as np

angulo = 45  

# Rotación en el eje X
radianes = np.radians(angulo)
matriz_rotacion_x = np.array([[1, 0, 0], [0, np.cos(radianes), -np.sin(radianes)], [0, np.sin(radianes), np.cos(radianes)]])
print(f"Matriz de rotación en el eje X para un ángulo de {angulo} grados:\n{matriz_rotacion_x}\n")

# Rotación en el eje Y
radianes = np.radians(angulo)
matriz_rotacion_y = np.array([[np.cos(radianes), 0, np.sin(radianes)], [0, 1, 0],[-np.sin(radianes), 0, np.cos(radianes)]])
print(f"Matriz de rotación en el eje Y para un ángulo de {angulo} grados:\n{matriz_rotacion_y}\n")

# Rotación en el eje Z
radianes = np.radians(angulo)
matriz_rotacion_z = np.array([[np.cos(radianes), -np.sin(radianes), 0], [np.sin(radianes), np.cos(radianes), 0],[0, 0, 1]])
print(f"Matriz de rotación en el eje Z para un ángulo de {angulo} grados:\n{matriz_rotacion_z}")