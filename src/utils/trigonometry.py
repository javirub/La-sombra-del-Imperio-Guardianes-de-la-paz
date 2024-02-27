import math

def calcular_posicion_proyectil(x_centro, y_centro, angulo_rotacion, distancia_cañon):
    """Calcula la posición de un proyectil."""
    x_inicial = x_centro + distancia_cañon * math.cos(angulo_rotacion)
    y_inicial = y_centro - distancia_cañon * math.sin(angulo_rotacion)

    return x_inicial, y_inicial