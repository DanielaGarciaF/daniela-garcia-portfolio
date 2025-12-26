import random
import math
from typing import Tuple

# ============================
# Distribuciones de probabilidad
# ============================

def generar_rnd():
    """Genera un número aleatorio entre 0 y 1"""
    return random.random()

def tiempo_exponencial(rnd: float, media_horas: float) -> float:
    """Distribución exponencial negativa (en minutos)"""
    return -media_horas * 60 * math.log(1-rnd)

def box_muller(rnd1: float, rnd2: float) -> Tuple[float, float]:
    """Método de Box-Muller que devuelve dos números Z0 y Z1"""
    z0 = math.sqrt(-2 * math.log(rnd1)) * math.cos(2 * math.pi * rnd2)
    z1 = math.sqrt(-2 * math.log(rnd1)) * math.sin(2 * math.pi * rnd2)
    return z0, z1

def tiempo_normal_box_muller(z: float, media_horas: float, desviacion_horas: float) -> float:
    """Distribución normal usando resultado de Box-Muller (en minutos)"""
    tiempo = media_horas * 60 + desviacion_horas * 60 * z
    return tiempo

def ocupacion_normal_box_muller(z: float, media_min: float, desviacion_min: float) -> float:
    """Distribución normal para ocupación usando resultado de Box-Muller (en minutos)"""
    tiempo = media_min + desviacion_min * z
    return max(0, tiempo)  # Evitar valores negativos