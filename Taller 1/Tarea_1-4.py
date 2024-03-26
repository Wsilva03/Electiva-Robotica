#actualizado
temperatura = float(-200)

R0 = 100.0  # Resistencia a 0°C para PT100 en Ohmios
#Los siguientes valores se aplican a los RTDs conformes a las normas IEC 60751 y ASTM E1137
A = 3.9083e-3
B = -5.775e-7
C = -4.183e-12

# Calcular la resistencia utilizando la ecuación de temperatura con la formula Ecuación de Callendar-Van Dusen
if temperatura >= 0 :
    R_t = R0 * (1 + A * temperatura + B * (temperatura ** 2))
else :
    R_t = R0 * (1 + A * temperatura + B * (temperatura ** 2) + C * (temperatura-100) *temperatura** 3)
print(f"La resistencia a {temperatura}°C es {R_t:.2f} Ohmios.")