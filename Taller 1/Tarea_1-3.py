import math

coordenadas_cartesianas = [4,5,6]
coordenadas_esfericas = []
coordenadas_cilindricas = []

#Coordenadas cartesianas a coordenadas efericas
coordenadas_esfericas.append( math.sqrt((coordenadas_cartesianas[0] ** 2) + (coordenadas_cartesianas[1] ** 2) + (coordenadas_cartesianas[2] ** 2)))
coordenadas_esfericas.append( math.atan(coordenadas_cartesianas[1] / coordenadas_cartesianas[0]))
coordenadas_esfericas.append( math.atan(math.sqrt((coordenadas_cartesianas[0] ** 2) + (coordenadas_cartesianas[1] ** 2)) / coordenadas_cartesianas[2]))

print(f"Coordenadas esfericas \n{coordenadas_esfericas}\n")

#Coordenadas cartesianas a coordenadas cilindricas
coordenadas_cilindricas.append( math.sqrt((coordenadas_cartesianas[0] ** 2) + (coordenadas_cartesianas[1] ** 2)))
coordenadas_cilindricas.append( math.atan(coordenadas_cartesianas[1] / coordenadas_cartesianas[0]))
coordenadas_cilindricas.append(coordenadas_cartesianas[2])

print(f"Coordenadas esfericas \n{coordenadas_cilindricas}\n")