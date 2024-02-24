import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
 
num = [float(input("Ingrese el coeficiente 'K' (numerador): "))]
den = [1, float(input("Ingrese el coeficiente 'omega_n' (denominador): ")), float(input("Ingrese el coeficiente 'Zeta' (denominador): "))]

system = signal.TransferFunction(num, den)
tiempo, respuesta = signal.step(system)
 
damping_ratio = np.sqrt(den[1]) / (2 * np.sqrt(den[0]))

if damping_ratio < 1:
    print("\n***El sistema es subamortiguado.***")
elif damping_ratio == 1:
    print("\n***El sistema es críticamente amortiguado.***")
else:
    print("\n***El sistema es sobreamortiguado.***")

# Graficar la respuesta al escalón
plt.plot(tiempo, respuesta)
plt.title('Respuesta al Escalón de la Función de Transferencia')
plt.xlabel('Tiempo')
plt.ylabel('Respuesta')
plt.grid(True)
plt.show()



