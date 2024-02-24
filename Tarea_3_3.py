import matplotlib.pyplot as plt
import numpy as np

def carga_descarga_RC(t, V, R, C):
    """
    Calcula el voltaje en un circuito RC durante la carga y descarga.

    Parameters:
        t (array): Array de tiempo.
        V (float): Voltaje de la fuente.
        R (float): Resistencia en ohmios.
        C (float): Capacitancia en faradios.

    Returns:
        array: Array de voltajes en función del tiempo.
    """
    tau = R * C  # Constante de tiempo del circuito RC
    return V * (1 - np.exp(-t / tau))

# Solicitar al usuario que ingrese los valores
V = float(input("Ingrese el voltaje de la fuente (V): "))
R = float(input("Ingrese la resistencia (Ω): "))
C = float(input("Ingrese la capacitancia (μF): ")) * 1e-6  # Convertir microfaradios a faradios

# Crear un array de tiempo para la gráfica
tiempo_carga = np.linspace(0, 5 * R * C, 1000)  # Tiempo durante la carga
tiempo_descarga = np.linspace(0, 5 * R * C, 1000)  # Tiempo durante la descarga

# Calcular los voltajes durante carga y descarga
voltajes_carga = carga_descarga_RC(tiempo_carga, V, R, C)
voltajes_descarga = carga_descarga_RC(tiempo_descarga, V, R, C)[::-1]  # Invertir para la descarga

# Graficar los resultados
plt.plot(tiempo_carga, voltajes_carga, label='Carga')
plt.plot(tiempo_descarga, voltajes_descarga, label='Descarga', linestyle='dashed')
plt.title('Carga y Descarga en un Circuito RC')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (V)')
plt.legend()
plt.grid(True)
plt.show()