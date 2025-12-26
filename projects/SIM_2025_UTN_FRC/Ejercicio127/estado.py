from typing import List
from distribuciones import (
    generar_rnd,
    box_muller,
    tiempo_exponencial,
    tiempo_normal_box_muller
)
from entidades import Equipo


class EstadoSimulacion:
    """Representa el estado completo de la simulación en un momento dado"""
    def __init__(self, estado_anterior=None):
        # Copiar estado anterior si existe
        if estado_anterior:
            self.reloj = estado_anterior.reloj
            self.evento_actual = estado_anterior.evento_actual
            self.ultima_disciplina = estado_anterior.ultima_disciplina
            self.prox_fin_acondicionamiento = estado_anterior.prox_fin_acondicionamiento

            # RNDs para llegadas
            self.rnd_handball_1 = estado_anterior.rnd_handball_1
            self.rnd_handball_2 = estado_anterior.rnd_handball_2
            self.rnd_football = estado_anterior.rnd_football
            self.rnd_basketball_1 = estado_anterior.rnd_basketball_1
            self.rnd_basketball_2 = estado_anterior.rnd_basketball_2
            
            # Resultados Box-Muller para llegadas
            self.z_handball_0 = estado_anterior.z_handball_0  # z0 (coseno) - para próxima llegada
            self.z_handball_1 = estado_anterior.z_handball_1  # z1 (seno) - guardado para futuras llegadas
            self.z_basketball_0 = estado_anterior.z_basketball_0  # z0 (coseno) - para próxima llegada
            self.z_basketball_1 = estado_anterior.z_basketball_1  # z1 (seno) - guardado para futuras llegadas
            
            # Flags para controlar uso de números Box-Muller en llegadas
            self.hay_z_disponible_handball = estado_anterior.hay_z_disponible_handball
            self.hay_z_disponible_basketball = estado_anterior.hay_z_disponible_basketball
            
            # Tiempos de próxima llegada
            self.tiempo_prox_handball = estado_anterior.tiempo_prox_handball
            self.tiempo_prox_football = estado_anterior.tiempo_prox_football
            self.tiempo_prox_basketball = estado_anterior.tiempo_prox_basketball
            
            # Próximas llegadas
            self.prox_llegada_handball = estado_anterior.prox_llegada_handball
            self.prox_llegada_football = estado_anterior.prox_llegada_football
            self.prox_llegada_basketball = estado_anterior.prox_llegada_basketball
            
            # RNDs para ocupación 
            self.rnd_ocupacion_handball_1 = estado_anterior.rnd_ocupacion_handball_1
            self.rnd_ocupacion_handball_2 = estado_anterior.rnd_ocupacion_handball_2
            self.rnd_ocupacion_football_1 = estado_anterior.rnd_ocupacion_football_1
            self.rnd_ocupacion_football_2 = estado_anterior.rnd_ocupacion_football_2
            self.rnd_ocupacion_basketball_1 = estado_anterior.rnd_ocupacion_basketball_1
            self.rnd_ocupacion_basketball_2 = estado_anterior.rnd_ocupacion_basketball_2
            
            # Flags para saber si TMP2 ya se usó (y debe limpiarse en próxima iteración)
            self.tmp_handball_2_usado = estado_anterior.tmp_handball_2_usado
            self.tmp_football_2_usado = estado_anterior.tmp_football_2_usado if estado_anterior else False
            self.tmp_basketball_2_usado = estado_anterior.tmp_basketball_2_usado if estado_anterior else False

            # Tiempos de ocupación DISPONIBLES 
            self.tmp_handball_1_disponible = estado_anterior.tmp_handball_1_disponible
            self.tmp_handball_2_disponible = estado_anterior.tmp_handball_2_disponible
            self.tmp_football_1_disponible = estado_anterior.tmp_football_1_disponible
            self.tmp_football_2_disponible = estado_anterior.tmp_football_2_disponible
            self.tmp_basketball_1_disponible = estado_anterior.tmp_basketball_1_disponible
            self.tmp_basketball_2_disponible = estado_anterior.tmp_basketball_2_disponible

            # Próximo fin de juego
            self.prox_fin_juego = estado_anterior.prox_fin_juego
            
            # Colas
            self.cola_handball_football = estado_anterior.cola_handball_football.copy()
            self.cola_basketball = estado_anterior.cola_basketball.copy()
            
            # Servidor
            self.estado_servidor = estado_anterior.estado_servidor
            self.tiempo_inicio_servicio = estado_anterior.tiempo_inicio_servicio
            self.equipos_actuales = estado_anterior.equipos_actuales.copy() if estado_anterior.equipos_actuales else []
            self.tiempo_acondicionamiento = estado_anterior.tiempo_acondicionamiento
            
            # Estadísticas
            self.equipos_handball_atendidos = estado_anterior.equipos_handball_atendidos
            self.tiempo_espera_handball = estado_anterior.tiempo_espera_handball
            self.equipos_football_atendidos = estado_anterior.equipos_football_atendidos
            self.tiempo_espera_football = estado_anterior.tiempo_espera_football
            self.equipos_basketball_atendidos = estado_anterior.equipos_basketball_atendidos
            self.tiempo_espera_basketball = estado_anterior.tiempo_espera_basketball
            
            # Lista de equipos
            self.equipos = estado_anterior.equipos.copy()
            
            # Contadores
            self.id_counter_handball = estado_anterior.id_counter_handball
            self.id_counter_football = estado_anterior.id_counter_football
            self.id_counter_basketball = estado_anterior.id_counter_basketball
            
        else:
            # Estado inicial
            self.reloj = 0
            self.evento_actual = "Inicio"
            self.ultima_disciplina = None  # 'H', 'F', 'B'
            self.prox_fin_acondicionamiento = float("inf")

            # Inicializar RNDs para llegadas
            self.rnd_handball_1 = generar_rnd()
            self.rnd_handball_2 = generar_rnd()
            self.rnd_football = generar_rnd()
            self.rnd_basketball_1 = generar_rnd()
            self.rnd_basketball_2 = generar_rnd()
            
            # Generar números Box-Muller para handball
            self.z_handball_0, self.z_handball_1 = box_muller(self.rnd_handball_1, self.rnd_handball_2)
            self.hay_z_disponible_handball = True  # Tenemos z1 disponible para próxima llegada
            
            # Generar números Box-Muller para basketball
            self.z_basketball_0, self.z_basketball_1 = box_muller(self.rnd_basketball_1, self.rnd_basketball_2)
            self.hay_z_disponible_basketball = True  # Tenemos z1 disponible para próxima llegada
            
            # Calcular tiempos de primera llegada usando z0
            self.tiempo_prox_handball = tiempo_normal_box_muller(self.z_handball_0, 12, 2)  # 12±2 horas
            self.tiempo_prox_football = tiempo_exponencial(self.rnd_football, 10)  # 10 horas
            self.tiempo_prox_basketball = tiempo_normal_box_muller(self.z_basketball_0, 8, 2)  # 8±2 horas
            
            # Próximas llegadas
            self.prox_llegada_handball = self.tiempo_prox_handball
            self.prox_llegada_football = self.tiempo_prox_football
            self.prox_llegada_basketball = self.tiempo_prox_basketball
            
            # Ocupación - inicialmente vacíos
            self.rnd_ocupacion_handball_1 = None
            self.rnd_ocupacion_handball_2 = None
            self.rnd_ocupacion_football_1 = None
            self.rnd_ocupacion_football_2 = None
            self.rnd_ocupacion_basketball_1 = None
            self.rnd_ocupacion_basketball_2 = None
            
            # Tiempos de ocupación disponibles (inicialmente vacíos)
            self.tmp_handball_1_disponible = None
            self.tmp_handball_2_disponible = None
            self.tmp_football_1_disponible = None
            self.tmp_football_2_disponible = None
            self.tmp_basketball_1_disponible = None
            self.tmp_basketball_2_disponible = None
            
            self.tmp_handball_2_usado = False
            self.tmp_football_2_usado = False
            self.tmp_basketball_2_usado = False

            # Próximo fin de juego (inicialmente infinito)
            self.prox_fin_juego = float('inf')
            
            # Colas vacías
            self.cola_handball_football = []
            self.cola_basketball = []
            
            # Servidor libre
            self.estado_servidor = "Libre"  # "Libre", "Ocupado_H", "Ocupado_F", "Ocupado_B", "Acondicionamiento"
            self.tiempo_inicio_servicio = 0
            self.equipos_actuales = []
            self.tiempo_acondicionamiento = 0
            
            # Estadísticas iniciales
            self.equipos_handball_atendidos = 0
            self.tiempo_espera_handball = 0
            self.equipos_football_atendidos = 0
            self.tiempo_espera_football = 0
            self.equipos_basketball_atendidos = 0
            self.tiempo_espera_basketball = 0
            
            # Lista de equipos vacía
            self.equipos = []
            
            # Contadores de IDs
            self.id_counter_handball = 1
            self.id_counter_football = 1
            self.id_counter_basketball = 1