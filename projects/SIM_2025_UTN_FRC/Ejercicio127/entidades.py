# ============================
# Clases para la simulación
# ============================
class Equipo:
    def __init__(self, tipo: str, id_num: int, tiempo_llegada: float):
        self.tipo = tipo                  # 'H', 'F', 'B'
        self.id_num = id_num
        self.id = f"{tipo}{id_num}"

        self.tiempo_llegada = tiempo_llegada
        self.estado = "Esperando"

        self.tiempo_inicio_juego = None
        self.tiempo_fin_juego = None
        self.tiempo_espera = 0

    def iniciar_juego(self, tiempo_actual: float):
        self.tiempo_inicio_juego = tiempo_actual
        self.tiempo_espera = tiempo_actual - self.tiempo_llegada
        self.estado = "Jugando"

    def finalizar_juego(self, tiempo_actual: float):
        self.tiempo_fin_juego = tiempo_actual
        self.estado = "Finalizado"

    def __repr__(self):
        return self.id