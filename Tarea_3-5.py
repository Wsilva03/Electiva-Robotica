import matplotlib.pyplot as plt


# Coordenadas de los nombres de los integrantes (puedes ajustarlas según tus necesidades)
integrantes = {
'Integrante1': (2, 3),
'Integrante2': (7, 8),
'Integrante3': (4, 5),
# ... Puedes agregar más integrantes según sea necesario
}
fig, ax = plt.subplots()

for nombre, coordenadas in integrantes.items():
    x, y = coordenadas
    ax.annotate(nombre, (x, y), fontsize=12, ha='center', va='center')

ax.set_xlim([0, 10])  # Ajusta los límites del gráfico según tus necesidades
ax.set_ylim([0, 10])

plt.grid(True)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Nombres de los Integrantes del Grupo')

plt.show()



