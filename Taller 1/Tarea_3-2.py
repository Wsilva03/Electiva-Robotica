import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
numerador =[]
denominador=[]
num = [float(input("Ingrese el coeficiente 'K' (numerador): "))]
den = [1, float(input("Ingrese el coeficiente 'omega_n' (denominador): ")), float(input("Ingrese el coeficiente 'Zeta' (denominador): "))]

numerador.append(num[0] * den[1] ** 2)
denominador.append(den[0])
denominador.append(2 * den[2] * den[1])
denominador.append(den[1] ** 2)
system = signal.TransferFunction(numerador, denominador)
tiempo, respuesta = signal.step(system)
 
damping_ratio = den[2] ** 2

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



