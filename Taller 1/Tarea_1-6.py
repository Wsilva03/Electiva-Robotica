# Datos del cilindro neumático
presion_trabajo = 600000  
diametro_piston = 0.05 
diametro_vastago = 0.02 

# Calcula el área del pistón (A = pi * radio^2)
area_piston = 3.1416 * (diametro_piston / 2)**2
# Calcula el área del vastago (A = pi * radio^2)
area_vastago = 3.1416 * (diametro_vastago / 2)**2


# Calcula la fuerza de avance y retroceso
fuerza_avance = presion_trabajo * area_piston
fuerza_retroceso = presion_trabajo * (area_piston - area_vastago)

# Imprime los resultados
print("Fuerza de avance del cilindro:", fuerza_avance, "N")
print("Fuerza de retroceso del cilindro:", fuerza_retroceso, "N")