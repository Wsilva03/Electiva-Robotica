import matplotlib.pyplot as plt

    # Coordenadas de los puntos de inicio y fin de cada letra
    # Cada letra se representa como una lista de tuplas donde cada tupla es un punto (x, y)
camilo = {
    'C': [(0.75, 0), (0, 0), (0, 0), (0, 1), (0, 1), (0.75, 1)],
    'A': [(1, 0), (1.35, 1), (1.35, 1), (1.7, 0)],
    'M': [(2, 0), (2, 1), (2, 1), (2.4, 0.5), (2.4, 0.5), (2.8, 1), (2.8, 1), (2.8, 0)],
    'I': [(3.5, 0), (3.5, 1)],
    'L': [(4.8, 0), (4, 0), (4, 0), (4, 1)],
    'O': [(5, 0), (5, 1), (5, 1), (6, 1), (6, 0), (6, 0), (5, 0)],
}
wendy = {
    'W': [(0, 1), (0, 0), (0, 0), (0.35, 0.4 ), (0.35, 0.4 ), (0.7, 0), (0.7, 0), (0.7, 1) ],
    'E': [(1.7, 0), (1, 0), (1, 0), (1, 0.5), (1, 0.5), (1.5, 0.5), (1.5, 0.5), (1, 0.5), (1, 0.5), (1, 1), (1, 1), (1.7, 1)],
    'N': [(2, 0), (2, 1), (2, 1), (2.7, 0), (2.7, 0), (2.7, 1)],
    'D': [(3, 0), (3, 1), (3, 1), (3.7, 0.7), (3.7, 0.7), (3.7, 0.35), (3.7, 0.35), (3, 0)],
    'Y': [(4.4, 0), (4.4, 0.4), (4.4, 0.4), (4, 1), (4, 1), (4.4, 0.4), (4.4, 0.4), (5, 1) ],
}
manuel = {
    'M': [(0, 0), (0, 1), (0, 1), (0.35, 0.4), (0.35, 0.4), (0.7, 1), (0.7, 1), (0.7, 0)],
    'A': [(1, 0), (1.35, 1), (1.35, 1), (1.7, 0)],
    'N': [(2, 0), (2, 1), (2, 1), (2.7, 0), (2.7, 0), (2.7, 1)],
    'U': [(3, 1), (3, 0), (3, 0), (3.7, 0), (3.7, 0), (3.7, 1)],
    'E': [(4.7, 0), (4, 0), (4, 0), (4, 0.5), (4, 0.5), (4.5, 0.5), (4.5, 0.5), (4, 0.5), (4, 0.5), (4, 1), (4, 1), (4.7, 1)],
    'L': [(5.8, 0), (5, 0), (5, 0), (5, 1)],
}
jeslan = {
    'J': [(0, 0), (0.7, 0), (0.7, 0), (0.7, 1), (0.7, 1), (0.2, 1),],
    'E': [(1.7, 0), (1, 0), (1, 0), (1, 0.5), (1, 0.5), (1.5, 0.5), (1.5, 0.5), (1, 0.5), (1, 0.5), (1, 1), (1, 1), (1.7, 1)],
    'S': [(2, 0), (2.7, 0), (2.7, 0), (2.7, 0.5), (2.7, 0.5), (2, 0.5), (2, 0.5), (2, 1), (2, 1), (2.7, 1),],
    'L': [(3.8, 0), (3, 0), (3, 0), (3, 1)],
    'A': [(4, 0), (4.35, 1), (4.35, 1), (4.7, 0)],
    'N': [(5, 0), (5, 1), (5, 1), (5.7, 0), (5.7, 0), (5.7, 1)],
}

# Crear una figura y un eje
fig, ax= plt.subplots()
fig1, ax1= plt.subplots()
fig2, ax2= plt.subplots()
fig3, ax3= plt.subplots()

# Iterar sobre las letras y dibujarlas
for letra, coordenadas in camilo.items():
    x, y = zip(*coordenadas)  # Separar las coordenadas en listas de x y y
    ax.plot(x, y, label=letra)  # Dibujar la letra
    
# Iterar sobre las letras y dibujarlas
for letra1, coordenadas1 in wendy.items():
    x, y = zip(*coordenadas1)  # Separar las coordenadas en listas de x y y
    ax1.plot(x, y, label=letra1)  # Dibujar la letra
# Iterar sobre las letras y dibujarlas
for letra2, coordenadas2 in manuel.items():
    x, y = zip(*coordenadas2)  # Separar las coordenadas en listas de x y y
    ax2.plot(x, y, label=letra2)  # Dibujar la letra
for letra3, coordenadas3 in jeslan.items():
    x, y = zip(*coordenadas3)  # Separar las coordenadas en listas de x y y
    ax3.plot(x, y, label=letra3)  # Dibujar la letra

# Configurar el aspecto del gráfico
ax.set_aspect('equal')  # Relación de aspecto igual
ax.set_xlim(-1, 8)  # Límites del eje x
ax.set_ylim(-1, 2)  # Límites del eje y
ax.legend()  # Mostrar leyenda

# Configurar el aspecto del gráfico
ax1.set_aspect('equal')  # Relación de aspecto igual
ax1.set_xlim(-1, 7)  # Límites del eje x
ax1.set_ylim(-1, 2)  # Límites del eje y
ax1.legend()  # Mostrar leyenda

# Configurar el aspecto del gráfico
ax2.set_aspect('equal')  # Relación de aspecto igual
ax2.set_xlim(-1, 8)  # Límites del eje x
ax2.set_ylim(-1, 2)  # Límites del eje y
ax2.legend()  # Mostrar leyenda

# Configurar el aspecto del gráfico
ax3.set_aspect('equal')  # Relación de aspecto igual
ax3.set_xlim(-1, 8)  # Límites del eje x
ax3.set_ylim(-1, 2)  # Límites del eje y
ax3.legend()  # Mostrar leyenda
# Mostrar el gráfico
plt.show()


