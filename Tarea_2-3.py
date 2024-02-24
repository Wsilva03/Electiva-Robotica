import math

print("Calculadora de volúmenes\n1. Prisma\n2. Pirámide\n3. Cono truncado\n4. Cilindro")
opcion = int(input("Seleccione el sólido (1-4): "))

if opcion == 1:
    base = float(input("Ingrese la base del prisma: "))
    altura = float(input("Ingrese la altura del prisma: "))
    volumen = base * altura
    print(f"El volumen del prisma es: {volumen}")
elif opcion == 2:
    base = float(input("Ingrese la base de la pirámide: "))
    altura = float(input("Ingrese la altura de la pirámide: "))
    volumen = (1/3) * base * altura
    print(f"El volumen de la pirámide es: {volumen}")
elif opcion == 3:
    radio_base_mayor = float(input("Ingrese el radio de la base mayor del cono truncado: "))
    radio_base_menor = float(input("Ingrese el radio de la base menor del cono truncado: "))
    altura = float(input("Ingrese la altura del cono truncado: "))
    volumen = (1/3) * math.pi * altura * (radio_base_mayor**2 + radio_base_mayor * radio_base_menor + radio_base_menor**2)
    print(f"El volumen del cono truncado es: {volumen}")
elif opcion == 4:
    radio = float(input("Ingrese el radio del cilindro: "))
    altura = float(input("Ingrese la altura del cilindro: "))
    volumen = math.pi * radio**2 * altura
    print(f"El volumen del cilindro es: {volumen}")
else:
    print("Opción no válida")

print("***PROGRAMA FINALIZADO***")

