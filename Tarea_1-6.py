# Datos del cilindro neumático
presion_trabajo = 600000  
diametro_piston = 0.05  

# Calcula el área del pistón (A = pi * radio^2)
area_piston = 3.1416 * (diametro_piston / 2)**2

# Calcula la fuerza de avance y retroceso
fuerza_avance = presion_trabajo*area_piston
fuerza_retroceso = presion_trabajo*area_piston

# Imprime los resultados
print("Fuerza de avance del cilindro:", fuerza_avance, "N")
print("Fuerza de retroceso del cilindro:", fuerza_retroceso, "N")