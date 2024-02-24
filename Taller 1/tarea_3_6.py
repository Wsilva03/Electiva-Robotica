import cv2
import numpy as np
import matplotlib.pyplot as plt

def obtener_contornos(imagen):
    # Lee la imagen
    img = cv2.imread(imagen)
    if img is None:
        print("Error: No se pudo cargar la imagen.")
        return []

    # Convierte la imagen a escala de grises
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Aplica un filtro Gaussiano para suavizar la imagen
    blur = cv2.GaussianBlur(gris, (5, 5), 0)
    
    # Aplica la umbralización adaptativa
    binaria = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 4)

    # Encuentra los contornos en la imagen binaria
    contornos, _ = cv2.findContours(binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    coordenadas_contornos = []

    # Itera sobre los contornos encontrados
    for contorno in contornos:
        # Calcula el rectángulo delimitador para el contorno
        x, y, w, h = cv2.boundingRect(contorno)
        # Dibuja el contorno en la imagen original (opcional)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Añade las coordenadas del rectángulo delimitador a la lista
        coordenadas_contornos.append((x, y, w, h))

    return img, coordenadas_contornos

# Nombre de la imagen
nombre_imagen = 'D:\Informacion\Downloads\Hyundai.png'

# Obtén la imagen con los contornos dibujados y las coordenadas de los contornos
imagen_con_contornos, coordenadas = obtener_contornos(nombre_imagen)

# Muestra la imagen con los contornos dibujados
plt.imshow(cv2.cvtColor(imagen_con_contornos, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()

# Imprime las coordenadas de los contornos
for i, (x, y, w, h) in enumerate(coordenadas):
    print(f"Contorno {i+1}: (X={x}, Y={y}), Width={w}, Height={h}")
