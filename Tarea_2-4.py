print("Seleccione el tipo de robot:")
print("1. Cilíndrico")
print("2. Cartesiano")
print("3. Esférico")

opcion = int(input("Ingrese el número de la opción deseada (1, 2 o 3): "))

# Obtener el tipo y número de articulaciones
    
if opcion == 1:
    print ("\nContiene tres articulaciones prismáticas\n")
elif opcion == 2:
    print ( "\nContiene tres articulaciones deslizantes\n")
elif opcion == 3:
    print ("\nContiene inicialmente dos articulaciones rotacionales con sus ejes perpendiculares entre sí y la tercera de tipo prismático con su eje perpendicular a las dos primeras\n")

else:
    print("\n **OPCION NO VALIDA**. Debe elegir 1, 2 o 3.\n")
print("***PROGRAMA FINALIZADO***\n")
