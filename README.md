Optimizador de Imágenes: Avances y Documentación

Investigación y Avances

1. Soluciones Propuestas

Se han identificado tres enfoques principales para la optimización de imágenes:

a) Reescalado de Imágenes

Reducción de dimensiones (hasta la mitad) manteniendo la legibilidad
Objetivo: Reducir el tamaño del archivo sin comprometer la utilidad
b) Conversión a Blanco y Negro

Cambio de imágenes en color a escala de grises
Justificación: Las imágenes solo requieren ser leídas, no necesitan conservar los colores originales
c) Cambio de Formato de Imagen

Conversión de formatos como JPG a JPEG o WebP
Enfoque en formatos que ofrezcan mejor compresión y compatibilidad
2. Herramientas y Librerías Evaluadas

a) OpenCV (cv2)

Propósito: Procesamiento de imágenes
Observaciones:

Métodos considerados agresivos para el procesamiento
Limitaciones en formatos de salida que pueden no ser óptimos para web
Descarte debido a la complejidad y posibles errores en entornos web
b) Pillow (PIL)

Propósito: Conversión y edición de imágenes
Ventajas:

Sencillez y enfoque en conversión de formatos
Funcionalidades adicionales: recortes, ajustes de color, contraste
Compatibilidad con formatos modernos como WebP
Decisión: Seleccionada como la librería principal por su equilibrio entre funcionalidad y facilidad de uso
3. Resultados y Conclusiones

Pillow ofrece un enfoque más controlado y adecuado para la conversión de imágenes
La compatibilidad con formatos web (como WebP) es crucial para la implementación
Se prioriza la simplicidad y la eficacia en la reducción de tamaño sin perder legibilidad
