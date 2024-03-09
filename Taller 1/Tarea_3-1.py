import matplotlib.pyplot as plt
import numpy as np

def resistencia_pt100(temperatura):
    R0 = 100.0  
    A = 3.9083e-3
    B = -5.775e-7
    C = -4.183e-12

    if temperatura >= 0 :
        R_t = R0 * (1 + A * temperatura + B * (temperatura ** 2))
    else :
        R_t = R0 * (1 + A * temperatura + B * (temperatura ** 2) + C * (temperatura-100) * temperatura ** 3)

    return R_t
#temperatura = input("Ingrese un valor de temperatura: ")
temperaturas = np.arange(-200, 201, 1)

# Calcular las resistencias correspondientes
resistencias = [resistencia_pt100(temp) for temp in temperaturas]

# Crear el gráfico
plt.plot(temperaturas, resistencias, label='Comportamiento PT100')
plt.title('Comportamiento de un Sensor PT100')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Resistencia (Ohmios)')
plt.legend()
plt.grid(True)
plt.show()
