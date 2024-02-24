continuar = True
while continuar:
    respuesta = input("¿Desea continuar? (Si/No): ")
    respuesta.lower()
    if respuesta == "no":
        continuar = False
        print("Gracias, vuelva pronto =)")

