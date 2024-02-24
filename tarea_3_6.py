import cv2
import numpy as np
import matplotlib.pyplot as plt

def obtener_contornos(imagen_path):
    # Lee la imagen
    imagen = cv2.imread(imagen_path)

    # Convierte la imagen a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Aplica un umbral (puedes ajustar el valor según tu imagen)
    _, umbral = cv2.threshold(gris, 127, 255, cv2.THRESH_BINARY)

    # Encuentra los contornos en la imagen umbralizada
    contornos, _ = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return contornos

def dibujar_contornos(imagen_path, contornos):
    # Lee la imagen original
    imagen = cv2.imread(imagen_path)

    # Dibuja los contornos en la imagen original
    cv2.drawContours(imagen, contornos, -1, (0, 255, 0), 2)

    # Muestra la imagen con los contornos
    plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
    plt.title('Contornos del Logo')
    plt.axis('off')
    plt.show()

# Ruta de la imagen del logo (reemplaza con la ruta de tu imagen)
ruta_imagen = 'ruta/a/tu/imagen/logo.jpg'

# Obtén los contornos de la imagen
contornos_logo = obtener_contornos(ruta_imagen)

# Dibuja los contornos en la imagen original
dibujar_contornos(ruta_imagen, contornos_logo)

