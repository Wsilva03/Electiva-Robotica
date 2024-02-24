import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar las imágenes de los logos
chevrolet_logo = cv2.imread('E:\Pictures\Chevrolet.jpeg')
hyundai_logo = cv2.imread('E:\Pictures\Hyundai.jpeg')
mazda_logo = cv2.imread('E:\Pictures\mazda.jpeg')

# Convertir las imágenes a escala de grises
chevrolet_gray = cv2.cvtColor(chevrolet_logo, cv2.COLOR_BGR2GRAY)
hyundai_gray = cv2.cvtColor(hyundai_logo, cv2.COLOR_BGR2GRAY)
mazda_gray = cv2.cvtColor(mazda_logo, cv2.COLOR_BGR2GRAY)

# Aplicar umbral para obtener los contornos
_, chevrolet_thresh = cv2.threshold(chevrolet_gray, 240, 255, cv2.THRESH_BINARY)
_, hyundai_thresh = cv2.threshold(hyundai_gray, 240, 255, cv2.THRESH_BINARY)
_, mazda_thresh = cv2.threshold(mazda_gray, 240, 255, cv2.THRESH_BINARY)

# Encontrar los contornos en las imágenes umbralizadas
chevrolet_contours, _ = cv2.findContours(chevrolet_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
hyundai_contours, _ = cv2.findContours(hyundai_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
mazda_contours, _ = cv2.findContours(mazda_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Crear una figura para mostrar los contornos
plt.figure(figsize=(12, 8))

# Dibujar los contornos de Chevrolet
plt.subplot(131)
chevrolet_copy = chevrolet_logo.copy()
cv2.drawContours(chevrolet_copy, chevrolet_contours, -1, (0, 255, 0), 2)
plt.imshow(cv2.cvtColor(chevrolet_copy, cv2.COLOR_BGR2RGB))
plt.title('Chevrolet')
plt.axis('off')

# Dibujar los contornos de Hyundai
plt.subplot(132)
hyundai_copy = hyundai_logo.copy()
cv2.drawContours(hyundai_copy, hyundai_contours, -1, (0, 255, 0), 2)
plt.imshow(cv2.cvtColor(hyundai_copy, cv2.COLOR_BGR2RGB))
plt.title('Hyundai')
plt.axis('off')

# Dibujar los contornos de Mazda
plt.subplot(133)
mazda_copy = mazda_logo.copy()
cv2.drawContours(mazda_copy, mazda_contours, -1, (0, 255, 0), 2)
plt.imshow(cv2.cvtColor(mazda_copy, cv2.COLOR_BGR2RGB))
plt.title('Mazda')
plt.axis('off')

plt.show()